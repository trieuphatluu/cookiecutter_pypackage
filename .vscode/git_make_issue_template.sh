#!/bin/bash
# DEFINES
WORKSPACE_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd )"
PROJECT_NAME="${PWD##*/}"
# ----------------------------------INCLUDE---------------------------------------
source $WORKSPACE_FOLDER/.vscode/print.sh
# ----------------------------------DEFINE----------------------------------------
print "Make git issue template"
print ${WORKSPACE_FOLDER}
INPUT_FILEPATH=${WORKSPACE_FOLDER}/.vscode/git_issue_template.json
OUTPUT_FILEPATH=${WORKSPACE_FOLDER}/.vscode/git_issue_copy.json
cp ${INPUT_FILEPATH} ${OUTPUT_FILEPATH}
code ${OUTPUT_FILEPATH}
