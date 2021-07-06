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

# FileIO Packages
import json

# Web pages and URL Related
import requests


# =====================================DEFINES=================================

GIT_AUTH = os.environ.get("GIT_AUTH")

labels = [
    {
        "name": ":hammer_and_wrench: Hardware",
        "description": "Hardware Design",
        "color": "92deca",
    },
    {"name": ":computer: Interface", "description": "Interface", "color": "92deca"},
    {
        "name": ":hourglass_flowing_sand: Priority-Low",
        "description": "Low priority",
        "color": "92deca",
    },
    {
        "name": ":hourglass_flowing_sand: Priority-Medium",
        "description": "Medium priority",
        "color": "fbca04",
    },
    {
        "name": ":hourglass_flowing_sand: Priority-High",
        "description": "High priority",
        "color": "ff3300",
    },
    {"name": ":dolphin: Docker", "description": "Docker related", "color": "92deca"},
    {"name": ":bug: Bugs", "description": "Bug to be fixed", "color": "cc6600"},
    {"name": ":fire: Remove", "description": "Remove codes/files", "color": "92deca"},
    {
        "name": ":racehorse: Performance",
        "description": "Performance",
        "color": "92deca",
    },
    {"name": ":question: Questions", "description": "Questions", "color": "cfd3d7"},
    {
        "name": ":floppy_disk: Datasets",
        "description": "Issues/Features related to deep learning dataset",
        "color": "add8e6",
    },
    {"name": ":trophy: Features", "description": "Complete", "color": "add8e6"},
    {"name": ":sparkles: New Features", "description": "New", "color": "add8e6"},
    {"name": ":wrench: Utilities", "description": "Utilities", "color": "cfd3d7"},
    {
        "name": ":chart_with_upwards_trend: Analytics",
        "description": "Data analytics and signal processing",
        "color": "92deca",
    },
    {
        "name": ":bar_chart: Visualization",
        "description": "Visualization",
        "color": "add8e6",
    },
    {
        "name": ":memo: Docs",
        "description": "Documentation or user guide",
        "color": "cfd3d7",
    },
    {
        "name": ":earth_americas: Web",
        "description": "Web or URL related",
        "color": "add8e6",
    },
]

script_dir = os.path.abspath(os.path.dirname(__file__))

# =====================================START=========================================


def requests_content(url, headers=None):
    # Web pages and URL Related
    from requests.exceptions import HTTPError

    content = None
    try:
        if headers is None:
            r = requests.get(url)
        else:
            r = requests.get(url, headers=headers)
        # If the response was successful, no Exception will be raised
        r.raise_for_status()
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Python 3.6
    except Exception as err:
        print(f"Other error occurred: {err}")  # Python 3.6
    else:
        print("Success!")
        content = r.json()
    return content


def get_all_label_names(url, auth):
    contents = requests_content(url, headers=auth)
    label_names = []
    for label in contents:
        label_names.append(label["name"])
    return label_names


def delete_label(url, auth, name):
    msg = f"{url}/{name}"
    print(f"requests.delete: {msg}")
    response = requests.delete(msg, headers=auth, timeout=10)
    print(f"{response.status_code}. {response.text}")


def delete_all_labels(url, auth):
    label_names = get_all_label_names(url, auth)
    for name in label_names:
        delete_label(url, auth, name)


def create_label(url, auth, label):
    response = requests.post(url, data=json.dumps(label), headers=auth, timeout=10)
    print(f"Create label: {label}")
    if response.status_code != 200 and response.status_code != 201:
        print(f"FAILED: {response.status_code}. {response.text}")
    else:
        print(f"DONE: {response.status_code}!")


def create_git_labels(url, auth, labels):
    for label in labels:
        create_label(url, auth, label)


# Web pages and URL Related
# ======================================================================================
# MAIN


def main():
    url = "https://api.github.com/repos/luutp/esp32stepperdriver/labels"
    token = {"Authorization": f"token {GIT_AUTH}"}
    print(token)
    print("Removing all current labels")
    delete_all_labels(url, token)
    print("Update git label config")
    create_git_labels(url, token, labels)


# DEBUG
if __name__ == "__main__":
    main()
