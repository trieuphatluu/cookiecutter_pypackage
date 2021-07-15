#!/bin/bash
# DEFINES
WORKSPACE_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd )"
PROJECT_NAME="${PWD##*/}"
# ----------------------------------INCLUDE---------------------------------------
source $WORKSPACE_FOLDER/.vscode/print.sh
source $WORKSPACE_FOLDER/.vscode/esp_idf_env.sh
# ----------------------------------DEFINE----------------------------------------
IDF_PATH=${ESP_IDF_DIR}
export PYTHONPATH="$IDF_PATH/tools:$IDF_PATH/tools/ci/python_packages:$PYTHONPATH"
print $(idf.py --version)
# 
source $HOME/.espressif/python_env/idf4.3_py3.8_env/Scripts/activate

cd ${ESP_IDF_DIR}/tools/ci/python_packages/ttfw_idf
pip install -r requirements.txt

cd ${ESP_IDF_DIR}/examples/system/ota/simple_ota_example
python example_test.py build 8070