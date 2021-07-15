#!/bin/bash
# DEFINES
WORKSPACE_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd )"
PROJECT_NAME="${PWD##*/}"
# ----------------------------------INCLUDE---------------------------------------
source $WORKSPACE_FOLDER/.vscode/print.sh
source $WORKSPACE_FOLDER/.vscode/esp_idf_env.sh
# ----------------------------------DEFINE----------------------------------------

print $(idf.py --version)
# 
cd ${WORKSPACE_FOLDER}
idf.py build

# Flash
bash ./scripts/esp_idf_flash.sh 

# Monitor

idf.py monitor
