# This is Downloadify
Downloadify is a python script designed to download every song in a specific spotify playlist, by just providing its Spotify ID.

# Installation

To install downloadify, you must first clone this repository.

```
git clone https://github.com/Koryozt/downloadify
```

Then, run the following command in your terminal with your activated virtual environment.

```
pip install requests
pip install yt-dlp
```
Then, you must create a file called "client.txt" inside the repository folder. Here you will add the following content:
```
Id:Your application's client id
Secret:Your application's client secret
```
If you don't want to create a spotify app to access these values, you can send me an email and I will send to you the required values for the client.txt

These are the requirements for using this script properly.

# How to use it

First, activate your virtual environment. When it's done, type the following command in your shell of preference.

`py main.py -pid "PlaylistID" -dir "Download directory"`

`-pid` or `--playlist_id` is a required argument. You must provide here the ID of the playlist you want to download. To find the Spotify playlist id enter the playlist page, click the (...) button near the play button, and click "Copy Playlist Link" under the Share menu. The playlist id is the string right after playlist/ as marked above.

`-dir` or `--directory` is an optional argument. If empty or it has the value of ".", it will download the tracks in the following path "./Downloads/{Playlist name}/", otherwise, they will be downloaded in the path provided.
<hr />

I hope you find this script useful.
