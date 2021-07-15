#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
screen_capture.py
Description:

Author: PhatLuu
Contact: tpluu2207@gmail.com
Created on: 2021/03/27
"""

#%%
# ================================IMPORT PACKAGES====================================

# Standard Packages
import os
import shutil
import sys

# Visualization Packages
import cv2

# GUI and User Interfaces Packages
import pyautogui
import pyperclip

# Utilities
import time
from datetime import datetime


# =====================================START===========================================

user_dir = os.path.abspath(os.path.expanduser("~"))
script_dir = os.path.dirname(sys.argv[0])
project_dir = os.path.dirname(script_dir)

# set output_dir based on active VS code windows
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


output_dir = os.path.join(user_dir, "Downloads")
timestamp = datetime.now().strftime("%y%m%d_%H%M%S")
filename = f"T{timestamp}_screenshot.png"
temp_fullscreen = os.path.join(output_dir, "temp_screenshot.png")
window_name = "Image Capture"

onClick = False
point1 = (0, 0)


def click(event, x, y, flags, params):

    global onClick, point1

    img, output_filepath = params

    if event == cv2.EVENT_LBUTTONDOWN:
        # if mousedown, store the x,y position of the mous
        onClick = True
        point1 = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE and onClick:
        # when dragging pressed, draw rectangle in image
        img_copy = img.copy()
        cv2.rectangle(img_copy, point1, (x, y), (0, 0, 255), 2)
        cv2.imshow(window_name, img_copy)
    elif event == cv2.EVENT_LBUTTONUP:
        # on mouseUp, create subimage
        try:
            onClick = False
            sub_img = img[point1[1] : y, point1[0] : x]
            print(f"Write image to: {output_filepath}")
            cv2.imwrite(output_filepath, sub_img)
            cv2.destroyAllWindows()
            # remove fullscreen file
            os.remove(temp_fullscreen)
        except:
            cv2.destroyAllWindows()
            os.remove(temp_fullscreen)


def paste_mkdocs_link(filename):
    basefilename, ext = os.path.splitext(filename)
    mkdocs_link = (
        f'<div style="text-align:left">\r\n'
        f'\t<img src="images/{filename}" width=60% alt="{basefilename}"">\r\n'
        f"\t<figcaption>{basefilename}</figcaption>\r\n"
        f"</div>"
    )
    pyperclip.copy(mkdocs_link)
    # pyautogui.click()
    # pyautogui.hotkey("ctrl", "v", interval=0.15)


def main():
    # Close bash window if exists
    time.sleep(0.5)
    wins = pyautogui.getAllTitles()
    for win in wins:
        if "/usr/bin/bash" in win:
            pyautogui.getWindowsWithTitle(win)[0].minimize()
    time.sleep(0.5)
    # Obtain output_dir based on active VS Code window
    # pyautogui.click()
    # time.sleep(1.0)
    # wins = pyautogui.getAllTitles()
    # for winname in wins:
    #     if "Visual Studio Code" in winname:
    #         win = pyautogui.getWindowsWithTitle(winname)[0]
    #         if win.isActive:
    #             project_name = winname.split(sep=" - ")[1]
    #             project_name = project_name.split(sep=" ")[0]
    #             output_dir = os.path.join(user_dir, f"{project_name}/docs/images")
    #             makedir(output_dir)

    output_dir = os.path.join(project_dir, "docs/images")
    makedir(output_dir)

    output_filepath = os.path.join(output_dir, filename)

    # Take screen shot
    pyautogui.screenshot(temp_fullscreen)
    img = cv2.imread(temp_fullscreen, 1)

    # Display image
    cv2.namedWindow(window_name)
    cv2.moveWindow(window_name, 0, 0)

    cv2.imshow(window_name, img)
    img_win = pyautogui.getWindowsWithTitle(window_name)[0]
    img_win.minimize()  # pyautogui bug: win.isMaximized is True but it's minimized
    time.sleep(0.5)
    img_win.maximize()

    # Set mouse callback to click function
    params = [img, output_filepath]
    cv2.setMouseCallback(window_name, click, params)

    cv2.waitKey(0)

    paste_mkdocs_link(os.path.basename(output_filepath))


# ==========================DEBUG===================================

if __name__ == "__main__":
    main()
