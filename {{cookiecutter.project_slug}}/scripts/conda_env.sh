#!/bin/bash
# -------------------------------------DEFINE---------------------------------------
WORKSPACE_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd )"
# Get project name from path (basename)
PROJECT_NAME="${PWD##*/}"
PIP_REQUIREMENTS=$WORKSPACE_FOLDER/requirements.txt
CONDA_DIR="$HOME/Anaconda3"

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
# Get Conda Env Name
if [ "$1" != "" ]; then
    CONDA_ENV="$1"
else
    print "Select Conda Environment:"
    read CONDA_ENV
fi
export PATH=${CONDA_DIR}/Scripts:$PATH
source ${CONDA_DIR}/etc/profile.d/conda.sh
conda activate
print "conda version: $(conda --version)"
print "Setup Conda $CONDA_ENV Environment"
# ======================================================================================
# Create Conda environment
## Add Anaconda to PATH and update
if [[ -d "${CONDA_DIR}/envs/${CONDA_ENV}" ]]; then
    print "${CONDA_ENV} Exist"
else
    print "conda create -y -n ${CONDA_ENV} python=3.7"
    conda create -y -n $CONDA_ENV python=3.7
    conda env list
fi
# Activate
conda activate $CONDA_ENV
# pip install
print "Installing PIP requirements"
${CONDA_DIR}/envs/${CONDA_ENV}/Scripts/pip install -r $PIP_REQUIREMENTS