#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
utils.py
Description
-------------------------------------------------------------------------------------------------------------------

Author: Trieu Phat Luu
Contact: tpluu2207@gmail.com
Created on: 05/25/2020 10:09:31
"""
# =================================================================================================================
# IMPORT PACKAGES
#%%
import os, sys
import inspect

# FileIO
import requests
import json
import yaml
import pickle
import pandas as pd

# 	Utilities
from tqdm import tqdm
import time
from datetime import datetime
import logging
import functools

ymd = datetime.now().strftime("%y%m%d")
# =============================================================================
def get_varargin(kwargs, inputkey, defaultValue):
    outputVal = defaultValue
    for key, value in kwargs.items():
        if key == inputkey:
            outputVal = value
        else:
            pass
    return outputVal


class colorFormatter(logging.Formatter):
    """Logging Formatter to add colors and count warning / errors"""

    grey = "\x1b[38;21m"
    yellow = "\x1b[33;21m"
    red = "\x1b[31;21m"
    bold_red = "\x1b[31;1m"
    Bold = " \x1b[1m"
    Cyan = " \x1b[38;5;122m"
    Magenta = " \x1b[38;5;200m"
    reset = "\x1b[0m"
    # msgformat = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"
    msgformat = "{bold}%(asctime)s|%(filename)s:%(lineno)d|%(levelname)s|{reset}{magenta} %(message)s".format(
        bold=Bold, reset=reset, magenta=Magenta
    )
    FORMATS = {
        logging.DEBUG: grey + msgformat + reset,
        logging.INFO: Cyan + msgformat + reset,
        logging.WARNING: yellow + msgformat + reset,
        logging.ERROR: red + msgformat + reset,
        logging.CRITICAL: bold_red + msgformat + reset,
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt="%y%m%d-%I:%M")
        return formatter.format(record)


def logging_setup(**kwargs):
    # 	Logging
    stream_hdl = logging.StreamHandler(sys.stdout)
    stream_hdl.setFormatter(colorFormatter())
    logger = logging.getLogger()
    logger.addHandler(stream_hdl)
    logger.setLevel(logging.INFO)
    # Only keep one logger
    for h in logger.handlers[:-1]:
        logger.removeHandler(h)
    return logger


logger = logging_setup()
# =================================================================================================================
# DECORATOR
def timeit(method):
    @functools.wraps(method)
    def timed(*args, **kwargs):
        start_time = time.time()
        logger.info("START: {}".format(method.__name__))
        result = method(*args, **kwargs)
        elapsed_time = time.time() - start_time
        hours, rem = divmod(elapsed_time, 3600)
        minutes, seconds = divmod(rem, 60)
        msg = (
            "DONE: {func_name}.\t"
            "Elapsed Time: {hours:0>2}:{mins:0>2}:{secs:0>2}\t".format(
                func_name=method.__name__,
                hours=int(hours),
                mins=int(minutes),
                secs=int(seconds),
            )
        )
        logger.info(msg)
        return result

    return timed


def log_info(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        logger.info("START: {}".format(func.__name__))
        for key, val in kwargs.items():
            logger.info("**kwargs: {}: {}".format(key, val))
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            logger.error(e)
            logger.info(e)
            return None
        msg = "DONE: {func_name}.\t".format(func_name=func.__name__)
        logger.info(msg)
        return result

    return inner


# =================================================================================================================
# FILE IO
@log_info
def read_txt(**kwargs):
    filepath = get_varargin(kwargs, "filepath", None)
    ext = os.path.splitext(os.path.basename(filepath))[1]
    output = None
    if ext == ".txt":
        # open the file as read only
        with open(filepath, "r") as fid:
            output = fid.read()
    else:
        logger.warning("{} is not .txt".format(ext))
    return output


@log_info
def save_yaml(inputdata, **kwargs):
    filename = get_varargin(kwargs, "filepath", "./untitiled.yaml")
    with open(filename, "w") as fid:
        yaml.dump(inputdata, fid)


@log_info
def load_yaml(yaml_filepath):
    with open(yaml_filepath, "r") as fid:
        try:
            output = yaml.safe_load(fid)
            return output
        except yaml.YAMLError as exc:
            print(exc)


@log_info
def save_json(inputdata, **kwargs):
    """Save dict to .json file

    Arguments:

        inputdata {[dict]} -- [data so save]
        kwargs:
            filepath: str -- .json filepath. Default: './untitile.json'
            overwrite: bool -- option to overwrite existing file. Default: False
    """
    # Parse input arguments
    filepath = get_varargin(kwargs, "filepath", "./untitiled.json")
    overwrite_opt = get_varargin(kwargs, "overwrite", False)
    if os.path.exists(filepath) and overwrite_opt is False:
        logger.info("File exists: {}. Skip saving".format(filepath))
        return
    # Save json file
    with open(filepath, "w") as fid:
        json.dump(inputdata, fid)


@log_info
def read_json(**kwargs):
    """Load .json file

    Arguments:

        Options:
            filepath: -- str. .json filepath

    Returns:
        [dict] -- .json data
    """
    filename = get_varargin(kwargs, "filepath", "./untitiled.json")
    with open(filename, "r") as fid:
        data = fid.read()
    return data


@log_info
def save_pickle(input_list, **kwargs):
    """Save data to pickle file

    Arguments:

        input_list {[type]} -- [description]
        kwargs:
            filepath -- str. path to save pickle file. Default. './untitled.pickle'
    """
    filename = get_varargin(kwargs, "filepath", "./untitled.pickle")
    with open(filename, "wb") as fid:
        for var in input_list:
            pickle.dump(var, fid)


@log_info
def read_pickle(**kwargs):
    filename = get_varargin(kwargs, "filepath", "./untitiled.json")
    with open(filename, "rb") as fid:
        data = pickle.load(fid)
    return data


@log_info
def read_df(**kwargs):
    """Load .csv or .xlxs file to pandas dataframe

    Input:

        fullfilename: fullpath to input data file in .csv or .xlsx format
        Options:
            skiprows: row index to skip
            sheet_name -- str/int. List of str/int are used to request multiple sheets

    Returns:

        df: pandas dataframe
    """
    fullfilename = get_varargin(kwargs, "filepath", None)
    skiprows = get_varargin(kwargs, "skiprows", None)
    filename, file_ext = os.path.splitext(fullfilename)
    sheetname = get_varargin(kwargs, "sheet_name", 0)
    # try:
    if file_ext == ".csv":
        df = pd.read_csv(fullfilename, skiprows=skiprows)
    else:
        df = pd.read_excel(fullfilename, sheet_name=sheetname, skiprows=skiprows)
    return df


def pickle_data(list_of_var, **kwargs):
    filename = get_varargin(kwargs, "filename", "untitled.pickle")
    with open(filename, "wb") as fid:
        for var in list_of_var:
            pickle.dump(var, fid)


# =================================================================================================================
@timeit
def unzip_file(filename, **kwargs):
    """
    unzip file
    Options:
        output -- str. Directory path. Default. Same as input filename
        remove -- Boolean. Option to delete zip file. Default. True
    """
    output_dir = get_varargin(kwargs, "output", os.path.dirname(filename))
    del_zip = get_varargin(kwargs, "remove", True)
    import zipfile

    with zipfile.ZipFile(filename, "r") as fid:
        fid.extractall(output_dir)
    if del_zip is True:
        os.remove(filename)


@log_info
def makedir(inputDir):
    if not os.path.exists(inputDir):
        logger.info("Making directory: {}".format(os.path.abspath(inputDir)))
        os.makedirs(inputDir)
    else:
        logger.info(
            "mkdir: Directory already exist: {}".format(os.path.abspath(inputDir))
        )


def list_fulldir(rootdir, **kwargs):
    get_latest = get_varargin(kwargs, "get_latest", False)
    dirlist = [os.path.join(rootdir, f) for f in os.listdir(rootdir)]
    dirlist = [f for f in dirlist if os.path.isdir(f)]
    if get_latest is True:
        return sorted(dirlist)[-1]
    else:
        return dirlist


# Select files from input_directory
def select_files(root_dir, **kwargs):
    """
    Select files in root_directory
    Options:
        and_key -- list. list of keys for AND condition. Default: None
        or_key -- list. List of keys for OR condition. Default: None
        ext -- str. File extension. Default: 'all'
    Returns:
        [list] -- list of selected files
    """
    # Input arguments
    and_key = get_varargin(kwargs, "and_key", None)
    or_key = get_varargin(kwargs, "or_key", None)
    sel_ext = get_varargin(kwargs, "ext", ["all"])
    depth = get_varargin(kwargs, "depth", "all")
    #
    def check_andkeys(filename, and_keys):
        status = True
        if and_keys is not None and not all(
            key.lower() in filename.lower() for key in and_keys
        ):
            status = False
        return status

    def check_orkeys(filename, or_keys):
        status = True
        if or_keys is not None and not any(
            key.lower() in filename.lower() for key in or_keys
        ):
            status = False
        return status

    fullfile_list = []
    if depth == "all":
        for path, subdirs, files in os.walk(root_dir):
            for name in files:
                fullfile_list.append(os.path.join(path, name))
    elif depth == "root":
        for name in os.listdir(root_dir):
            fullfile_list.append(os.path.join(root_dir, name))
    else:
        pass
    sel_files = []
    for fullfile in fullfile_list:
        filename, ext = os.path.splitext(os.path.split(fullfile)[1])
        if set([ext]).issubset(set(sel_ext)) or sel_ext[0] == "all":
            and_check = check_andkeys(fullfile, and_key)
            or_check = check_orkeys(fullfile, or_key)
            if and_check and or_check:
                sel_files.append(fullfile)
    return sel_files


# =================================================================================================================
# UTILS
# =================================================================================================================
def elapsed_time(start_time, **kwargs):
    elapsed_time = time.time() - start_time
    hours, rem = divmod(elapsed_time, 3600)
    minutes, seconds = divmod(rem, 60)
    return hours, minutes, seconds


# Download file from url
@timeit
def download_url(url, to_file, **kwargs):
    skip_on_avai = get_varargin(kwargs, "skip_on_avai", True)
    if skip_on_avai is True:
        if os.path.exists(to_file):
            logger.info("File exists: {}. Skip downloading".format(to_file))
            return -1
    logger.info("Downloading to: {}".format(to_file))
    r = requests.get(url, stream=True)
    # Total size in bytes.
    total_size = int(r.headers.get("content-length", 0))
    block_size = 1024  # 1 Kibibyte
    t = tqdm(total=total_size, unit="iB", unit_scale=True)
    makedir(os.path.dirname(to_file))
    with open(to_file, "wb") as fid:
        for data in r.iter_content(block_size):
            t.update(len(data))
            fid.write(data)
    t.close()
    print("\n")


def get_class_info(obj, **kwargs):
    input_type = get_varargin(kwargs, "type", "attrs")
    include_keys = get_varargin(kwargs, "include_keys", None)
    exclude_keys = get_varargin(kwargs, "exclude_keys", None)

    def get_attr_members(obj):
        members = inspect.getmembers(obj)
        attr_members = []
        for mem in members:
            if not inspect.isfunction(mem[1]) and not inspect.ismethod(mem[1]):
                attr_members.append(mem)
        return attr_members

    def get_method_members(obj):
        method_members = inspect.getmembers(obj, inspect.ismethod)
        return method_members

    def get_function_members(obj):
        function_members = inspect.getmembers(obj, inspect.isfunction)
        return function_members

    def get_attr_names(obj):
        attr_members = get_attr_members(obj)
        attr_names = [mem[0] for mem in attr_members]
        return attr_names

    def get_function_names(members):
        function_members = get_function_members(obj)
        function_names = [mem[0] for mem in function_members]
        return function_names

    def get_method_names(members):
        method_members = get_method_members(obj)
        method_names = [mem[0] for mem in method_members]
        return method_names

    def match_key(input_list, **kwargs):
        include_keys = get_varargin(kwargs, "include_keys", None)
        exclude_keys = get_varargin(kwargs, "exclude_keys", None)

        def check_andkeys(input_str, include_keys):
            status = True
            if (include_keys is not None) and (
                not all(key.lower() in input_str.lower() for key in include_keys)
            ):
                status = False
            return status

        def check_notkeys(input_str, exclude_keys):
            status = True
            if exclude_keys is not None:
                status = not (check_andkeys(input_str, exclude_keys))
            return status

        match_list = [
            item
            for item in input_list
            if check_andkeys(item, include_keys) and check_notkeys(item, exclude_keys)
        ]
        return match_list

    if input_type == "attrs":
        return match_key(
            get_attr_names(obj), include_keys=include_keys, exclude_keys=exclude_keys
        )
    elif input_type == "methods":
        return match_key(
            get_method_names(obj), include_keys=include_keys, exclude_keys=exclude_keys
        )
    elif input_type == "functions":
        return match_key(
            get_function_names(obj),
            include_keys=include_keys,
            exclude_keys=exclude_keys,
        )
    else:
        pass


# =================================================================================================================
def get_obj_params(obj):
    """
    Get names and values of all parameters in `obj`'s __init__
    """
    try:
        # get names of every variable in the argument
        args = inspect.getargspec(obj.__init__)[0]
        args.pop(0)  # remove "self"

        # get values for each of the above in the object
        argdict = dict([(arg, obj.__getattribute__(arg)) for arg in args])
        return argdict
    except:
        raise ValueError("object has no __init__ method")


def print_ndarray(input_mat):
    """Print ndarray in python as matrix in Matlab

    Args:
        input_mat ([type]): [description]
    """
    print(
        "\n".join(
            ["\t".join(["{:.1f}".format(item) for item in row]) for row in input_mat]
        )
    )


#%%
def main(**kwargs):
    pass


if __name__ == "__main__":
    main()
