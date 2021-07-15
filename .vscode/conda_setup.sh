#!/bin/bash
# DEFINES
WORKSPACE_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd )"
# Get project name from path (basename)
PROJECT_NAME="${PWD##*/}"
PIP_REQUIREMENTS=$WORKSPACE_FOLDER/requirements.txt
# Get Conda Env Name
if [ "$1" != "" ]; then
    CONDA_ENV="$1"
else
    echo "Select Conda Environment:"
    read CONDA_ENV
fi
echo "Setup Conda $CONDA_ENV Environment"
# ======================================================================================
# Create Conda environment
conda create -y -n $CONDA_ENV python=3.7
conda env list
# Activate
source ~/anaconda3/etc/profile.d/conda.sh
conda activate $CONDA_ENV
# Conda Install
conda install -y nodejs -n $CONDA_ENV
conda install -y tensorflow-gpu -n $CONDA_ENV
conda install -y -c conda-forge ipympl -n $CONDA_ENV
# pip install
echo "Installing PIP requirements"
/home/$USER/anaconda3/envs/$CONDA_ENV/bin/pip install -r $PIP_REQUIREMENTS
# update ipympl for interactive plot
/home/$USER/anaconda3/envs/$CONDA_ENV/bin/pip install git+https://github.com/matplotlib/jupyter-matplotlib.git#egg=ipympl