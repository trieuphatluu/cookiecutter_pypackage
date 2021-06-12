#!/bin/bash
# DEFINES
WORKSPACE_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd )"
PROJECT_NAME="${PWD##*/}"

make_git_repo(){
    curl -H "Authorization:token 6c4de563467c2fc0caac7c6c2b16b3c6949e15a3" https://api.github.com/user/repos -d "{\"name\":\"$1\", \"private\": \"true\"}"
}

# -------------------------------------START---------------------------------------

echo ${PROJECT_NAME}

# git init
git init 
git add .
git commit -m ":octocat:. Initialize"
make_git_repo ${PROJECT_NAME}
# Create a git repos on Github first before adding remote
# Add remote
git remote add origin https://github.com/luutp/${PROJECT_NAME}.git
# Push
echo "git push"
git push origin master
git push --set-upstream origin master
# Create develop branch
git checkout -b develop
git push origin master develop