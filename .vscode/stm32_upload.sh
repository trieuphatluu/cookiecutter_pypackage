#!/bin/bash
# DEFINE
WORKSPACE_FOLDER="$( cd "$( dirname "${BASH_SOURCE[0]}")/.." >/dev/null 2>&1 && pwd )"
PROJECT_NAME="${PWD##*/}"

CLEAR="\e[0m"
BOLD="\e[1m"
UNDERLINE="\e[4m"
BLINK="\e[5m"
RED="\e[31m"
GREEN="\e[32m"
YELLOW="\e[33m"
BLUE="\e[34m"
MAGENTA="\e[35m"
CYAN="\e[36m"
BG_RED="\e[41m"
BG_GREEN="\e[42m"
BG_YELLOW="\e[43m"
BG_BLUE="\e[44m"
BG_MAGENTA="\e[45m"
BG_CYAN="\e[46m"
# -------------------------------------START---------------------------------------
function print(){
    if [[ "$#" == 1 ]]; then
        echo -e "$MAGENTA $1 $CLEAR"
    else
        echo -e "$1 $2 $CLEAR"
    fi
}

STM32CUBE_DIR="C:\\Program Files\\STMicroelectronics\\STM32Cube\\STM32CubeProgrammer\\bin\\STM32_Programmer_CLI"

cd ${STM32CUBE_DIR}
BUILD_DIR="$(dirname "$SKETCH_FILE")"/build
if [[ ! -e $BUILD_DIR ]]; then
    echo -e mkdir $MAGENTA $BUILD_DIR $CLEAR
    mkdir $BUILD_DIR
else
    echo -e $MAGENTA $BUILD_DIR $CLEAR already exists
fi
STDOUT_FILE=$BUILD_DIR/stdout.txt
STDERR_FILE=$BUILD_DIR/stderr.txt

echo -e Upload $MAGENTA $SKETCH_FILE $CLEAR to $BLUE $COM_PORT $CLEAR
./arduino --upload --board "teensy:avr:teensy31:usb=serial, speed=96,opt=o2std,keys=en-us" --verbose-upload --preferences-file $WORKSPACE_FOLDER/.vscode/arduino_pref_$COM_PORT.txt $SKETCH_FILE 2> $STDERR_FILE > $STDOUT_FILE &
wait $!
FILESIZE=1000
while [ $FILESIZE != $(wc -c <"$STDERR_FILE") ] ; do 
    FILESIZE=$(wc -c <"$STDERR_FILE")
    sleep 4
    echo -e $YELLOW Writing to stdout.txt. File size: $FILESIZE bytes $CLEAR
done

if grep -q "Uploading" $STDERR_FILE; then
    COLOR=$GREEN
    echo -e $COLOR BUILD SUCCESSFUL! $CLEAR
else
    COLOR=$RED
    echo -e $COLOR BUILD FAILED! $CLEAR
fi
while read line; do 
    echo -e $COLOR $line $CLEAR 
done < $STDERR_FILE

cat $STDOUT_FILE

cd $current_dir