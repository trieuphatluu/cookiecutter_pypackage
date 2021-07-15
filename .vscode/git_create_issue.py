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
import argparse
import os

# FileIO Packages
import json

# Web pages and URL Related
import requests

# GUI and User Interfaces Packages
import pyautogui

# Utilities
import time


# =====================================DEFINES=================================

GIT_AUTH = os.environ.get("GIT_AUTH")

script_dir = os.path.abspath(os.path.dirname(__file__))

REPO = os.path.basename(os.path.dirname(script_dir))

# =====================================START=========================================

# Web pages and URL Related
# ======================================================================================
# MAIN


def load_json(json_filepath):
    output = None
    if not os.path.isfile(json_filepath):
        print(f"{json_filepath} is not a file")
        return output

    print(f"START-Loading json file: {json_filepath}")
    start_time = time.time()
    with open(json_filepath, "r") as fid:
        output = json.load(fid)

    elapsed_time = time.time() - start_time
    hours, rem = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(rem, 60)
    msg = "DONE-" "Elapsed Time: {hours:0>2}:{mins:0>2}:{secs:0>2}\t".format(
        hours=int(hours), mins=int(minutes), secs=int(seconds),
    )
    print(msg)
    return output


def save_json(json_data, json_filepath):
    with open(json_filepath, "w") as fid:
        json.dump(json_data, fid)


def parse_issue_config(issue_filepath):
    issue_config = load_json(issue_filepath)
    body_contents = issue_config["body"]
    body_str = ""
    for l in body_contents:
        body_str = body_str + f"{l}\r\n"
    issue_config["body"] = body_str
    return issue_config


def get_args_parser():
    parser = argparse.ArgumentParser(
        prog=os.path.basename(os.path.abspath(__file__)),
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Additional Info",
    )
    parser.add_argument(
        "--verbose", action="store_true", required=False, help="verbose"
    )
    parser.add_argument(
        "-f",
        type=str,
        default="git_issue_template.json",
        help="input issue config filepath",
    )
    return parser


def get_latest_issue_id():
    issue_id = None
    url = f"https://api.github.com/repos/luutp/{REPO}/issues"
    token = {
        "Authorization": f"token {GIT_AUTH}",
        "Accept": "application/vnd.github.inertia-preview+json",
    }
    data_dict = {
        "sort": "created",
        "per_page": 2,
    }
    try:
        r = requests.get(url, data=json.dumps(data_dict), headers=token)
        print(f"Status code: {r.status_code}")
        latest_issue = r.json()[0]
        issue_id = latest_issue["id"]
    except Exception as e:
        print(e)
    return issue_id


def list_project_columns(project_id):
    url = f"https://api.github.com/projects/{project_id}/columns"
    # url = f"https://api.github.com/luutp/projects"
    token = {
        "Authorization": f"token {GIT_AUTH}",
        "Accept": "application/vnd.github.inertia-preview+json",
    }
    outputs = None
    try:
        r = requests.get(url, headers=token, timeout=10)
        if r.status_code == 304:
            print(f"FAILED. Status: {r.status_code} Not Modified")
            print(f"{r.text}")
        elif r.status_code == 401:
            print(f"FAILED. Status: {r.status_code} Unauthorized")
            print(f"{r.text}")
        elif r.status_code == 403:
            print(f"FAILED. Status: {r.status_code} Forbidden")
            print(f"{r.text}")
        elif r.status_code == 200:
            outputs = r.json()
            print(f"Status code: {r.status_code}")
            print("SUCCESSFUL!")
    except Exception as e:
        print(e)
    return outputs


def create_project_card(column_id, issue_id):
    url = f"https://api.github.com/projects/columns/{column_id}/cards"
    token = {
        "Authorization": f"token {GIT_AUTH}",
        "Accept": "application/vnd.github.inertia-preview+json",
    }
    data_dict = {"content_id": issue_id, "content_type": "Issue"}
    r = requests.post(url, data=json.dumps(data_dict), headers=token)
    print(f"Status code: {r.status_code}")
    print(r.text)
    print("DONE")


def main(args):
    column_id = 15043895
    # https://github.com/luutp/printstore/projects/1#column-15043895
    # Parse input arguments
    config_filepath = args.f

    url = f"https://api.github.com/repos/luutp/{REPO}/issues"
    token = {"Authorization": f"token {GIT_AUTH}"}

    print("Create github issue")
    config_dict = parse_issue_config(config_filepath)
    print(config_dict)

    r = requests.post(url, data=json.dumps(config_dict), headers=token, timeout=10)
    print(f"Status code: {r.status_code}")

    # Remove file
    os.remove(config_filepath)
    # Close IDE
    pyautogui.hotkey("ctrl", "w", interval=0.15)
    # Get latest issue ID
    issue_id = get_latest_issue_id()
    if issue_id is not None:
        create_project_card(column_id, issue_id)


# =====================================DEBUG===================================

if __name__ == "__main__":
    args = get_args_parser().parse_args()
    main(args)
