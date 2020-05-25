# Cookiecutter for Python Package

Cookiecutter template for a Python package.

- GitHub repo: https://github.com/trieuphatluu/cookiecutter_pypackage
- Free software: BSD license

## Features

---

- Create project template for python package

## Quickstart

---

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.4.0 or higher)::

    pip install -U cookiecutter

Generate a Python package project::

    cookiecutter https://github.com/trieuphatluu/cookiecutter_pypackage.git

Then:

- Copy to a repos
- Install the dev requirements into a virtualenv. (`pip install -r requirements.txt`)

## Similar Cookiecutter Templates

---

- `Nekroze/cookiecutter-pypackage`\_: A fork of this with a PyTest test runner,
  strict flake8 checking with Travis/Tox, and some docs and `setup.py` differences.

- `tony/cookiecutter-pypackage-pythonic`_: Fork with py2.7+3.3 optimizations.
  Flask/Werkzeug-style test runner, `_compat` module and module/doc conventions.
  See `README.rst` or the `github comparison view`_ for exhaustive list of
  additions and modifications.

- `ardydedase/cookiecutter-pypackage`\_: A fork with separate requirements files rather than a requirements list in the `setup.py` file.

- `lgiordani/cookiecutter-pypackage`_: A fork of Cookiecutter that uses Punch_ instead of bump2version\_ and with separate requirements files.

- `briggySmalls/cookiecutter-pypackage`_: A fork using Pipenv_ for package management, with linting, formatting and more.
