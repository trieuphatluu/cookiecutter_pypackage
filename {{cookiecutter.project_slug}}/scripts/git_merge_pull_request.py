#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
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


# =====================================DEFINES=================================
OWNER = "luutp"
REPO = "esp32stepperdriver"
GIT_AUTH = os.environ.get("GIT_AUTH")
DEFAULT_BRANCH = "develop"

script_dir = os.path.abspath(os.path.dirname(__file__))

# =====================================START=========================================
def git_get_current_branch():
    current_branch = subprocess.check_output("git branch --show-current")
    current_branch = str(current_branch, "utf-8").strip()
    return current_branch


def list_pull_request():
    url = f"https://api.github.com/repos/{OWNER}/{REPO}/pulls"
    token = {
        "Authorization": f"token {GIT_AUTH}",
        "Accept": "application/vnd.github.inertia-preview+json",
    }
    data_dict = {
        "base": "develop",
        "sort": "created",
    }
    outputs = None
    try:
        r = requests.get(url, data=json.dumps(data_dict), headers=token, timeout=10)
        if r.status_code == 304:
            print(f"FAILED. Status: {r.status_code} Not Modified")
            print(f"{r.text}")
        elif r.status_code == 422:
            print(f"FAILED. Status: {r.status_code} Unprocessable Entity")
            print(f"{r.text}")
        else:
            outputs = r.json()
            print(f"Status code: {r.status_code}")
            print("SUCCESSFUL!")

    except Exception as e:
        print(e)
    return outputs


def merge_pull_request():
    outputs = list_pull_request()
    latest_pull_request = outputs[0]
    pull_number = latest_pull_request.get("number")
    commit_title = f"Merge pull request {pull_number}" + latest_pull_request.get(
        "title"
    )

    url = f"https://api.github.com/repos/{OWNER}/{REPO}/pulls/{pull_number}/merge"
    token = {
        "Authorization": f"token {GIT_AUTH}",
        "Accept": "application/vnd.github.inertia-preview+json",
    }
    data_dict = {
        "merge_method": "merge",
        "commit_title": commit_title,
    }
    try:
        r = requests.put(url, data=json.dumps(data_dict), headers=token, timeout=10)
        if r.status_code == 403:
            print(f"FAILED. Status: {r.status_code} Forbidden")
            print(f"{r.text}")
        elif r.status_code == 404:
            print(f"FAILED. Status: {r.status_code} Not Found")
            print(f"{r.text}")
        elif r.status_code == 405:
            print(f"FAILED. Status: {r.status_code} Method Not Allow")
            print(f"{r.text}")
        elif r.status_code == 200:
            outputs = r.json()
            print(f"Status code: {r.status_code}")
            print("SUCCESSFUL!")

    except Exception as e:
        print(e)

    return r.status_code


def delete_current_branch():
    current_branch = git_get_current_branch()
    subprocess.check_output(f"git checkout {DEFAULT_BRANCH}")
    subprocess.check_output(f"git pull")
    subprocess.check_output(f"git branch -D {current_branch}")
    subprocess.check_output(f"git push origin --delete {current_branch}")


def main():
    r = merge_pull_request()
    if r == 200:
        delete_current_branch()


# =====================================DEBUG===================================

if __name__ == "__main__":
    main()
