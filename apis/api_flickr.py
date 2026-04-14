import os
import time
import flickrapi
import xml.etree.ElementTree as ET
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('FLICKR_API_KEY')
api_secret = os.getenv('FLICKR_API_SECRET')

flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')

flickr.authenticate_via_browser(perms='write')


def get_album(album_title: str, photo_id: str):

    albums = flickr.photosets.getList()

    for album in albums['photosets']['photoset']:

        if album['title']['_content'] == album_title:
            return album['id']

    new_album = flickr.photosets.create(title=album_title, primary_photo_id=photo_id)

    return new_album['photoset']['id']


def upload_photos(dataframe):

    for _, album in dataframe.iterrows():

        album_id = None
        album_title = album['album_title']
        album_directory = album['album_directory']

        for filename in os.listdir(album_directory):

            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):

                file_path = os.path.join(album_directory, filename)

                print(f"Álbum: '{album_title}'  ->  Realizando upload: '{file_path}'")

                response = flickr.upload(filename=file_path, format="rest")
                response = response.decode('utf8')

                response = ET.fromstring(response)
                photo_id = response.find('photoid').text

                if album_id is None:
                    album_id = get_album(album_title, photo_id)

                else:
                    flickr.photosets.addPhoto(photoset_id=album_id, photo_id=photo_id)

                time.sleep(2)
