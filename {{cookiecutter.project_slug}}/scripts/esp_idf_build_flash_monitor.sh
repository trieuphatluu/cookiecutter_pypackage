#!/bin/bash
# DEFINES
WORKSPACE_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd )"
PROJECT_NAME="${PWD##*/}"
# ----------------------------------INCLUDE---------------------------------------
source $WORKSPACE_FOLDER/Scripts/print.sh
# ----------------------------------DEFINE----------------------------------------
ESP_DIR=$HOME/esp
ESP_VERSION=v4.3
ESP_IDF_DIR=${ESP_DIR}/esp-idf
# Please refer to 
# Step 4. Set up the environment variables
cd ${ESP_IDF_DIR}
source export.sh

print $(idf.py --version)
# 
cd ${WORKSPACE_FOLDER}
idf.py build

# Flash
bash ./scripts/esp_idf_flash.sh 

# Monitor

idf.py monitor
