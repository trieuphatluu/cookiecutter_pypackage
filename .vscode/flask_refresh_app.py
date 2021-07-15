#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
flask_secrets.py
Description:

Author: PhatLuu
Contact: tpluu2207@gmail.com
Created on: 2021/07/06
"""

# Standard Packages
#%%
# ================================IMPORT PACKAGES====================================

# GUI and User Interfaces Packages
import pyautogui

# Utilities
import time


SLEEP_TIME = 0.5


try:
    window_name = "Fast3DPrint"
    flask_window = pyautogui.getWindowsWithTitle(window_name)[0]
except:
    try:
        window_name = "127.0.0.1:5000"
        flask_window = pyautogui.getWindowsWithTitle(window_name)[0]
    except Exception as e:
        print(e)
        exit()

# =====================================DEIFNES========================================
if flask_window.isActive is False:
    # Select flask window and refresh
    pyautogui.click(x=flask_window.center.x, y=flask_window.center.y)
    time.sleep(SLEEP_TIME)
    pyautogui.hotkey("f5")
    # Select VSCode Editor
    time.sleep(SLEEP_TIME)
    pyautogui.hotkey("win", "2", interval=0.1)
