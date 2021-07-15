#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
git_label.py
---------------------------------------------------------------------------------------
Author: Trieu Phat Luu
Contact: tpluu2207@gmail.com
Created on: 06/17/2020 03:36:18
"""

#%%
# =====================================IMPORT PACKAGES=================================
# Standard Packages
import os
import subprocess

# FileIO Packages
import json

# Web pages and URL Related
import requests

# GUI and User Interfaces Packages

# Utilities


# =====================================DEFINES=================================
OWNER = "luutp"
REPO = "esp32stepperdriver"
GIT_AUTH = os.environ.get("GIT_AUTH")

script_dir = os.path.abspath(os.path.dirname(__file__))

# =====================================START=========================================

# Web pages and URL Related
# ======================================================================================
# MAIN


def git_get_current_branch():
    current_branch = subprocess.check_output("git branch --show-current")
    current_branch = str(current_branch, "utf-8").strip()
    return current_branch


def create_pull_request():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/pulls"
    token = {
        "Authorization": f"token {GIT_AUTH}",
        "Accept": "application/vnd.github.inertia-preview+json",
    }

    current_branch = git_get_current_branch()
    print("Create pull request")
    data_dict = {
        "title": f"{current_branch}",
        "head": f"luutp:{current_branch}",
        "base": "develop",
    }
    print(data_dict)
    try:
        r = requests.post(url, data=json.dumps(data_dict), headers=token, timeout=10)
        if r.status_code == 422:
            print("FAILED. Status: 422 Unprocessable Entity")
            print(f"{r.text}")
        elif r.status_code == 403:
            print("FAILED. Status: 403 Forbidden")
            print(f"{r.text}")
        else:
            print(f"Status code: {r.status_code}")
            print("SUCCESSFUL!")

    except Exception as e:
        print(e)


def main():
    create_pull_request()


# =====================================DEBUG===================================

if __name__ == "__main__":
    main()
