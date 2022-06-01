import os
import hashlib
import random
import datetime

from werkzeug.utils import secure_filename

from config.config import photosdir, photos_subpath

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def get_path_to_photo(photo_sub_path):
    return photos_subpath + photo_sub_path

def is_allowed_extention(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_photo_to_disk(photo):
    extention = photo.filename.rsplit('.', 1)[1].lower()
    filename_byte = photo.filename.encode()
    hash_filename = str(hashlib.md5(filename_byte).hexdigest()) + '.' + extention
    sub_dir_path = calc_sub_dir_path_and_create_dirs(hash_filename)
    photo_path = os.path.join(photosdir + sub_dir_path, hash_filename)
    photo.save(photo_path)

    return os.path.join(sub_dir_path, hash_filename)

def calc_sub_dir_path_and_create_dirs(hash_filename):
    first_folder_name = get_folder_random_name(hash_filename)
    if not os.path.exists(os.path.join(photosdir, first_folder_name)):
        os.mkdir(os.path.join(photosdir, first_folder_name))
    second_folder_name = get_folder_random_name(hash_filename)
    if not os.path.exists(os.path.join(photosdir, first_folder_name, second_folder_name)):
        os.mkdir(os.path.join(photosdir, first_folder_name, second_folder_name))
    return '/' + first_folder_name + '/' + second_folder_name

def get_folder_random_name(hash_filename):
    now = str(datetime.datetime.now())
    hashed_now = str(hashlib.md5(now.encode()).hexdigest())
    i = random.randint(0, 30)
    j = i + 2

    return hashed_now[i:j]

