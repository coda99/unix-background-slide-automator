import os, subprocess
from file import open_file
from file_sys_manipulator import getdirname, getpath

base_path = os.getcwd() 
images_path = base_path + '/images/'
path = getpath()
try:
    dir_name = getdirname()
except NameError:
    pass

"""
    This module grabs the names of images from a pre-defined folder called
    "images" and saves them to a text file "images.txt", after that copies
    all the images found in the folder to the new destination where the
    slides will be called from.

    Args:
        prepare_img():
                    Extract all the image names from the "images" folder and
                    saves them in the "images.txt" file.
        
        move_img():
                    Handles the copying of the images from current folder to
                    destination folder where the slides will be automated from
"""

def prepare_img():
    temp = subprocess.Popen(('ls '+ images_path + ' > images.txt'), shell=True)
    output, err = temp.communicate()


def move_img():
    os.chdir(base_path)

    # Removing all new line characters from List
    newline_rm = str.maketrans('', '', '\n')
    img_list = [s.translate(newline_rm) for s in open_file(f"images.txt")]

    for img in img_list:
        # to try this block of code import shutil
        # try:
        #     os.rename(f"{images_path}{img}", f"{path}/{dir_name}/{img}")
        #     os.replace(f"{images_path}{img}", f"{path}/{dir_name}/{img}")
        #     shutil.move(f"{images_path}{img}", f"{path}/{dir_name}/{img}")
        # except FileNotFoundError:
        #     continue
        try:
            temp = subprocess.Popen((f'sudo cp {images_path}{img} {path}/{dir_name}/{img}'), shell=True)
            output, err = temp.communicate()
        except FileNotFoundError as e:
            print(e)
