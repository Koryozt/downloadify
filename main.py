import requests
import json
import base64
import argparse
import yt_dlp
import urllib
import subprocess
import re
import socket
import os

# 6fAcSQBDK5W8Wm7v2Zqu4t

AUTH_URL = 'https://accounts.spotify.com/api/token'
API_BASE = "https://api.spotify.com/v1/"
YOUTUBE_SEARCH_QUERY_URL = 'https://www.youtube.com/results?search_query='

def main():

    ap = argparse.ArgumentParser()
    ap.add_argument('-pid', '--playlist_id', required = True, help = 'Spotify playlist id to download')
    ap.add_argument('-dir', '--directory', required=True, help = "The directory to save the downloaded files")

    args = vars(ap.parse_args())

    playlist_id = args['playlist_id']
    directory = args['directory']

    with open('client.txt') as f:
        lines = f.readlines()
        client_id = lines[0].strip().split(':')[1]
        client_secret = lines[1].strip().split(':')[1]

    credentials = f'{client_id}:{client_secret}'

    encoded_credentials =  base64.b64encode(credentials.encode('utf-8')).decode('utf-8')

    auth_headers = {
        'Authorization': 'Basic ' + encoded_credentials
    }	

    payload = {
        'grant_type': 'client_credentials'
    }

    auth_options = {
        'url': AUTH_URL,
        'headers': auth_headers,
        'form': payload
    }

    try:	
        auth_response = (requests.post(
            url= auth_options['url'],
            headers=auth_options['headers'],
            data=auth_options['form'])).json()

        token = auth_response['token_type'] + ' ' + auth_response['access_token']

    except requests.HTTPError as e:
        print(e)

    request_url = API_BASE + f'playlists/{playlist_id}'

    request_headers = {
        'Authorization': token
    }

    try:
        playlist = json.loads((requests.get(
            url= request_url,
            headers= request_headers
        )).text)

    except requests.HTTPError as e:
        print(e)

    name = playlist['name']
    count = playlist['tracks']['total']
    tracks_group = playlist['tracks']['items']

    tracks = list()

    for track_item in tracks_group:
        track_name = track_item['track']['name']
        track_artist = track_item['track']['artists'][0]['name']

        tracks.append(f'{track_name} by {track_artist} lyrics')

    print(f"Playlist: {name} \n"+ 
        f"Track count: {count}")

    for track in tracks:
        search_q = urllib.parse.urlencode({'search_query':track})
        body = (requests.get(YOUTUBE_SEARCH_QUERY_URL + search_q))
        video_href = re.findall(r"watch\?v=(\S{11})", body.text)
        
        try:
            video_url = 'https://www.youtube.com/watch?v=' + video_href[0]

            if directory == '.' or not directory:
                filename = f'./downloads/{name}/{track}.mp3'
            else:
                filename = directory + f'./{name}/{track}.mp3'

            if os.path.exists(filename):
                print(f'{filename} already exists')
                continue
            
            video_info = yt_dlp.YoutubeDL().extract_info(url = video_url,download=False)

            options={
                'format':'bestaudio/best',
                'keepvideo':False,
                'outtmpl':filename,
            }

            with yt_dlp.YoutubeDL(options) as ydl:
                ydl.download([video_info['webpage_url']])

            print(f'Download complete... {filename}')

        except IndexError as e:
            print(e)

if __name__ == '__main__':
	main()