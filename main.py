import requests
import json
import base64

# 0uf6Hev3fqAa1V2AZU5Y5i

AUTH_URL = 'https://accounts.spotify.com/api/token'
API_BASE = "https://api.spotify.com/v1/"

def main():

    playlist_id = input("id:")

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

    print(f"Playlist: {name} \n"+ 
        f"Track count: {count}")

    



if __name__ == '__main__':
	main()