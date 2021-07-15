#!/bin/bash
WORKSPACE_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd )"
PROJECT_NAME="${PWD##*/}"
# ----------------------------------INCLUDE---------------------------------------
source $WORKSPACE_FOLDER/.vscode/print.sh
export PATH=$HOME/Anaconda3/Scripts:$PATH
source $HOME/Anaconda3/etc/profile.d/conda.sh
ENV_NAME=conda_esp32
conda activate ${ENV_NAME}
# VENV_NAME=esp32
# source $HOME/venv/${VENV_NAME}/Scripts/activate

# ----------------------------------DEFINE----------------------------------------
PIP_REQUIREMENTS=$WORKSPACE_FOLDER/requirements.txt

# ======================================================================================

# pip install
cd ${WORKSPACE_FOLDER}
print $(which python)
print $(which pip)
print "Installing PIP requirements"
pip install -r $PIP_REQUIREMENTS