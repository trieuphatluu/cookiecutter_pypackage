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
            exit 1
        fi
    fi
}

# Step 1. Install prerequisites

# Step 2. Get ESP-IDF
# Make esp Directory
make_folder ${ESP_DIR}
# Clone esp-idf from github
cd ${ESP_DIR}
if [ -d "${ESP_IDF_DIR}" ]; then
    print "Folder ${ESP_IDF_DIR} already exists."
else
    print "clone https://github.com/espressif/esp-idf.git"
    git clone -b ${ESP_VERSION} --recursive https://github.com/espressif/esp-idf.git
fi
# Step 3. Set up the tools
# Run install.sh file
cd ${ESP_IDF_DIR}
bash ./install.sh
