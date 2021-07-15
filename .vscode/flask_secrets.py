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
import secrets

# GUI and User Interfaces Packages
import pyperclip


print("Generate Secret Key")
key = secrets.token_hex(16)
pyperclip.copy(key)
print("DONE: Secret Key has been saved to clipboard")
