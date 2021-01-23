from instaloader import *
import json
import pickle
import os
L = Instaloader(
	dirname_pattern = 'post' ,
	filename_pattern = '{shortcode}', 
	save_metadata = False, 
	download_comments = False, 
	download_geotags = False, 
	post_metadata_txt_pattern = '',
	max_connection_attempts = 16,
	download_video_thumbnails = False,
)
data = {}
def create_album(title):
    from gphotospy import authorize
    from gphotospy.media import Media
    from gphotospy.album import Album
    CLIENT_SECRET_FILE = "gphoto_oauth.json"
    service = authorize.init(CLIENT_SECRET_FILE)
    album_manager = Album(service)

    new_album = album_manager.create(title)
    id_album = new_album.get("id")
    return id_album
def gphoto_upload(album_id, file):
    from gphotospy import authorize
    from gphotospy.media import Media
    from gphotospy.album import Album
    CLIENT_SECRET_FILE = "gphoto_oauth.json"
    service = authorize.init(CLIENT_SECRET_FILE)
    album_manager = Album(service)
    media_manager = Media(service)
    media_manager.stage_media(file)
    media_manager.batchCreate(album_id=album_id)
USER = 'mad_imo'
PASS = 'Muradow2003'
#L.login(USER, PASS)
L.load_session_from_file(USER)
profile = Profile.from_username(L.context, 'pirnazar_muradow')
users = profile.get_followees()

with open('data.pickle', 'rb') as f:
    data = pickle.load(f)
ids = []
for i in data:
    ids.append(i)


for id in ids:
    # profile = Profile.from_id(L.context, id)
    # posts = profile.get_posts()
    # L.download_stories([id])
    # L.posts_download_loop(posts, 'post')
    for r, d, f in os.walk('post'):
        for file in f:
            gphoto_upload(data[id]['album_id'], f'post/{file}')
            #os.system(f'rm post/{file}')
    break


