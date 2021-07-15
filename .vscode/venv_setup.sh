#!/bin/bash
# DEFINES
WORKSPACE_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd )"
PROJECT_NAME="${PWD##*/}"
# Select Python Inteperter
python3=$HOME/AppData/Local/Programs/Python/Python38/python.exe
# Get project name from path (basename)
PROJECT_NAME="${PWD##*/}"
PIP_REQUIREMENTS=$WORKSPACE_FOLDER/requirements.txt

CLEAR="\e[0m"
BOLD="\e[1m"
UNDERLINE="\e[4m"
BLINK="\e[5m"
RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[33m"
BLUE="\e[34m"
MAGENTA="\e[35m"
CYAN="\e[36m"
BG_RED="\e[41m"
BG_GREEN="\e[42m"
BG_YELLOW="\e[43m"
BG_BLUE="\e[44m"
BG_MAGENTA="\e[45m"
BG_CYAN="\e[46m"

# -------------------------------------START---------------------------------------
function print(){
    if [[ "$#" == 1 ]]; then
        echo -e "$MAGENTA $1 $CLEAR"
    else
        echo -e "$1 $2 $CLEAR"
    fi
}

# Create python venv
make_folder() {
    # Creates a folder and checks if it exists.
    local folder=$1
    if [ -d "${folder}" ]; then
        print "Folder ${folder} already exists. Skipping folder creation."
    else
        print "Creating folder ${folder}."
        if mkdir ${folder}; then
            print "Successfully created folder ${folder}."
        else
            print "Failed to create folder ${folder}. Exiting."
        fi
    fi
}

# -------------------------------------MAIN---------------------------------------
# Get VENV_NAME
if [ "$1" != "" ]; then
    VENV_NAME="$1"
else
    print "Select Environment Name:"
    read VENV_NAME
fi
print "Setup $VENV_NAME Environment"

## Add user to sudo
# sudo usermod -aG sudo $USER

# # Create python venv
cd ~ && make_folder venv
cd venv
if [[ -d "$VENV_NAME" ]]; then
    print "$VENV_NAME venv exist"
else
    print "create $VENV_NAME virtual env"
    make_folder $VENV_NAME
    ${python3} -m venv ~/venv/$VENV_NAME
fi

# Activate python env
if [[ ${OSTYPE} == msys ]]; then
    print "Windows OS"
    source ~/venv/$VENV_NAME/Scripts/activate
elif [[ ${OSTYPE} == linux ]]; then
    print "Linux OS"
    source ~/venv/$VENV_NAME/bin/activate
else
    print "Unknown"
fi

# install requirements
print "pip install -r requirements.txt"
if [[ ${OSTYPE} == msys ]]; then
    print "Windows OS"
    ~/venv/$VENV_NAME/Scripts/pip install -r ${PIP_REQUIREMENTS}
elif [[ ${OSTYPE} == linux ]]; then
    print "Linux OS"
    ~/venv/$VENV_NAME/bin/pip install -r ${PIP_REQUIREMENTS}
else
    print "Unknown"
fi