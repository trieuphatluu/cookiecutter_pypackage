WORKSPACE_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd )"
# Get project name from path (basename)
PROJECT_NAME="${PWD##*/}"
# git init
git init 
git add .
git commit -m "Initialize"
# Create a git repos on Github first before adding remote
# Add remote
git remote add origin https://github.com/trieuphatluu/$PROJECT_NAME.git
# Push
git push origin master