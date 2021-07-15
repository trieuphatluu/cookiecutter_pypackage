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

# Utilities
import time


# =====================================DEFINES========================================
user_dir = os.path.abspath(os.path.expanduser("~"))
script_dir = os.path.dirname(sys.argv[0])
docs_dir = os.path.join(os.path.dirname(script_dir), "docs")
images_dir = os.path.join(docs_dir, "images")

# =====================================MAIN==========================================
def main(**kwargs):
    youtube_url = pyperclip.paste()

    video_ID = youtube_url.split("/")[-1]
    mkdocs_link = (
        f"[![YOUTUBE_LINK]("
        f"https://img.youtube.com/vi/{video_ID}/0.jpg)]("
        f"{youtube_url})"
    )
    pyperclip.copy(mkdocs_link)
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "v", interval=0.15)


# =====================================DEBUG=========================================

if __name__ == "__main__":
    main()
