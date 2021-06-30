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

# Utilities
import time


# =====================================DEFINES=================================

GIT_AUTH = os.environ.get("GIT_AUTH")

script_dir = os.path.abspath(os.path.dirname(__file__))

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


def main(args):
    # Parse input arguments
    config_filepath = args.f

    url = "https://api.github.com/repos/luutp/esp32stepperdriver/issues"
    token = {"Authorization": f"token {GIT_AUTH}"}

    print("Create github issue")
    config_dict = parse_issue_config(config_filepath)
    print(config_dict)

    response = requests.post(
        url, data=json.dumps(config_dict), headers=token, timeout=10
    )

    os.remove(config_filepath)


# =====================================DEBUG===================================

if __name__ == "__main__":
    args = get_args_parser().parse_args()
    main(args)
