#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
mkdocs_paste_image.py
Description:

Author: PhatLuu
Contact: tpluu2207@gmail.com
Created on: 2021/03/16
"""

# ================================IMPORT PACKAGES====================================

# Standard Packages
import argparse
import errno
import os
import re
import shutil
import sys

# Web pages and URL Related
import requests

# GUI and User Interfaces Packages
import pyautogui
import pyperclip


# =====================================DEFINES========================================
user_dir = os.path.abspath(os.path.expanduser("~"))
script_dir = os.path.dirname(sys.argv[0])
docs_dir = os.path.join(os.path.dirname(script_dir), "docs")
images_dir = os.path.join(docs_dir, "images")

# =====================================MAIN==========================================


def get_valid_filename(input_filename):
    """Summary:
    --------
    Return valid filename by removing empty space and special characters

    -------
        input_filename (str): input filename

    Returns:
    --------
        str: valid filename
    """

    input_filename = input_filename.strip().replace(" ", "_")
    return re.sub(r"(?u)[^-\w.]", "", input_filename)


def makedir(inputDir, remove=False):
    """Summary:
    --------
    Make directory
    Inputs:
    -------
    inputDir (str): fullpath to directory to be created
    remove (bool): option to remove current existing folder
    """
    if remove is True and os.path.exists(inputDir):
        print("Remove existing folder")
        shutil.rmtree(inputDir)

    if not os.path.exists(inputDir):
        print(f"Making directory: {inputDir}")
        os.makedirs(inputDir)
    else:
        print(f"mkdir: Directory already exist: {inputDir}")


def download_url_image(image_url, **kwargs):

    saved_dir = kwargs.get("saved_dir", script_dir)

    # Set up the image URL and filename
    filename = get_valid_filename(image_url.split("/")[-1])
    makedir(saved_dir)
    fullfile_path = os.path.join(saved_dir, filename)

    # Open the url image, set stream to True, this will return the stream content.
    print(f"Download url: {image_url}")
    r = requests.get(image_url, stream=True)

    # Check if the image was retrieved successfully
    if r.status_code == 200:
        # Set decode_content value to True, otherwise the downloaded image file's size will be zero
        r.raw.decode_content = True

        # Open a local file with wb ( write binary ) permission.
        with open(fullfile_path, "wb") as f:
            shutil.copyfileobj(r.raw, f)
        print(f"Image sucessfully Downloaded: {fullfile_path}",)
        return 1
    else:
        print("Image Couldn't be retreived")
        return -1


# =====================================MAIN==========================================
def main(**kwargs):
    image_url = pyperclip.paste()
    saved_dir = images_dir

    if download_url_image(image_url, saved_dir=saved_dir):
        filename = get_valid_filename(image_url.split("/")[-1])
        basefilename, ext = os.path.splitext(filename)
        mkdocs_link = (
            f'<div style="text-align:center">\r\n'
            f'  <img src="../images/{filename}" width=85% alt="">\r\n'
            f'  <figcaption style="text-align:center; font-style:italic; font-size: 95%">{filename}</figcaption>\r\n'
            f"</div>\r\n"
        )
        pyperclip.copy(mkdocs_link)
        # pyautogui.click()
        pyautogui.hotkey("ctrl", "v", interval=0.15)
    else:
        print("Failed to paste image")


# =====================================DEBUG=========================================

if __name__ == "__main__":
    main()
