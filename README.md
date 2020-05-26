# Cookiecutter for Python Package

Table of contents

- [Cookiecutter for Python Package](#cookiecutter-for-python-package)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Usage](#usage)
  - [Similar Templates](#similar-templates)

## Introduction

This template use cookiecutter to greate required files and directories for your python packages.

-   GitHub repo: https://github.com/trieuphatluu/cookiecutter_pypackage
-   Free software: BSD license

## Features

-   Create project template for python package.
-   Generate the following files and folders for your python package

```bash
\USERS\YOUR_PROJECT_NAME
│   .editorconfig
│   .gitignore
│   AUTHORS.rst
│   LICENSE
│   Makefile
│   README.md
│   requirements.txt
│   setup.py
├───tests
│       test_your_project_name.py
│       __init__.py
└───your_project_name
    │   __init__.py
    │   __main__.py
    └───utils_dir
            utils.py
            __init__.py
```

## Usage

1. Install the latest Cookiecutter if you haven't installed it yet.

```bash
pip install -U cookiecutter
```

2. Run cookiecutter command

```bash
cookiecutter https://github.com/trieuphatluu/cookiecutter_pypackage.git
```

3. Provide your inputs. The values in the square brackets [] are default values

```bash
full_name [Trieu Phat Luu]:
email [tpluu2207@gmail.com]:
github_username [trieuphatluu]:
project_name [Your Project Name]:
project_slug [your_project_name]:
project_short_description [Description]:
pypi_username [trieuphatluu]:
version [0.1.0]:
use_pytest [n]:
create_author_file [y]:
Select open_source_license:
1 - MIT license
2 - BSD license
3 - ISC license
4 - Apache Software License 2.0
5 - GNU General Public License v3
6 - Not open source
Choose from 1, 2, 3, 4, 5, 6 [1]:
```

## Similar Templates

-   `Nekroze/cookiecutter-pypackage`\_: A fork of this with a PyTest test runner,
    strict flake8 checking with Travis/Tox, and some docs and `setup.py` differences.

-   `tony/cookiecutter-pypackage-pythonic`_: Fork with py2.7+3.3 optimizations.
    Flask/Werkzeug-style test runner, `_compat` module and module/doc conventions.
    See `README.rst` or the `github comparison view`_ for exhaustive list of
    additions and modifications.

-   `ardydedase/cookiecutter-pypackage`\_: A fork with separate requirements files rather than a requirements list in the `setup.py` file.

-   `lgiordani/cookiecutter-pypackage`_: A fork of Cookiecutter that uses Punch_ instead of bump2version\_ and with separate requirements files.

-   `briggySmalls/cookiecutter-pypackage`_: A fork using Pipenv_ for package management, with linting, formatting and more.
