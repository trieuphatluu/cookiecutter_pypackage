#!/bin/bash
# DEFINES
WORKSPACE_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd )"
PROJECT_NAME="${PWD##*/}"
# ----------------------------------INCLUDE---------------------------------------
source $WORKSPACE_FOLDER/scripts/print.sh
# ----------------------------------DEFINE----------------------------------------
OWNER=luutp
REPO=esp32stepperdriver
CURRENT_BRANCH=$(git branch --show-current)
print ${CURRENT_BRANCH}
# print "Make git issue template"
# print ${WORKSPACE_FOLDER}
# INPUT_FILEPATH=${WORKSPACE_FOLDER}/scripts/git_issue_template.json
# OUTPUT_FILEPATH=${WORKSPACE_FOLDER}/scripts/git_issue_copy.json
# cp ${INPUT_FILEPATH} ${OUTPUT_FILEPATH}
# code ${OUTPUT_FILEPATH}
curl \
    -X POST \
    -H "Accept: application/vnd.github.v3+json" \
    https://api.github.com/repos/${OWNER}/${REPO}/pulls \
    -d '{"head":${CURRENT_BRANCH},"base":"develop"}'