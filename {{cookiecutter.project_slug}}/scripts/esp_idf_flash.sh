#!/bin/bash
# DEFINES
WORKSPACE_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd )"
PROJECT_NAME="${PWD##*/}"
# ----------------------------------INCLUDE---------------------------------------
source $WORKSPACE_FOLDER/scripts/print.sh
PYTHON_ENV="${HOME}/.espressif/python_env/idf4.3_py3.8_env"
BUILD_DIR=${WORKSPACE_FOLDER}/build
# ----------------------------------DEFINE----------------------------------------
print "Run esptool to flash"
python=${PYTHON_ENV}/Scripts/python $HOME/esp/esp-idf/components/esptool_py/esptool/esptool.py -p COM12 -b 460800 --before default_reset --after hard_reset --chip esp32 write_flash --flash_mode dio --flash_freq 40m --flash_size detect 0x10000 ${BUILD_DIR}/esp32stepperdriver.bin 0x1000 ${BUILD_DIR}/bootloader/bootloader.bin 0x8000 ${BUILD_DIR}/partition_table/partition-table.bin