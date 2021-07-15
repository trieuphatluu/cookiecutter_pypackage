#!/bin/bash
# DEFINES
WORKSPACE_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd )"
PROJECT_NAME="${PWD##*/}"
# ----------------------------------INCLUDE---------------------------------------
source $WORKSPACE_FOLDER/.vscode/print.sh
# ----------------------------------DEFINE----------------------------------------
ESP_DIR=$HOME/esp
ESP_VERSION=v4.3
ESP_IDF_DIR=${ESP_DIR}/esp-idf
cd ${ESP_IDF_DIR}
source export.sh
