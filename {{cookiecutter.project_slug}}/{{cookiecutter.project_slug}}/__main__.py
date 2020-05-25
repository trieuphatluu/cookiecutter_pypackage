#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
{{cookiecutter.project_slug}}.py
{{cookiecutter.project_short_description}}
-------------------------------------------------------------------------------------------------------------------

Author: {{cookiecutter.full_name}}
Contact: {{cookiecutter.email}}
Created on: {% now 'utc-6', '%m/%d/%Y %H:%M:%S'%}
'''
# =================================================================================================================
# IMPORT PACKAGES
#%%
from __future__ import print_function
import os
import inspect, sys
import argparse
#	File IO
import json
import yaml
#	Data Analytics
import pandas as pd
import numpy as np
import random
#	Visualization Packages
import matplotlib.pyplot as plt
import skimage.io as skio
#	Utilities
from tqdm import tqdm
import time
from datetime import datetime
# Custom import
from {{cookiecutter.project_slug}}.utils_dir import utils
from {{cookiecutter.project_slug}}.utils_dir.utils import timeit, get_varargin, log_info
from {{cookiecutter.project_slug}}.utils_dir.utils import logger as logging
#%%
# =================================================================================================================
# MAIN
def main(**kwargs):
	logging.info('Hello world!')
# =================================================================================================================
# DEBUG
if __name__ == '__main__':
	main()
