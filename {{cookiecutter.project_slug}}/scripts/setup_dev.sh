#!/bin/bash
# Setup Develop for all packages in src dir
parent_path=$( cd "$(dirname "${BASH_SOURCE[0]}")/.." ; pwd -P )
echo "$parent_path"

for path in $parent_path/src/*; do
    [ -d "${path}" ] || continue # if not a directory, skip
    package_name="$(basename "${path}")"
    cd $path
    echo python setup.py develop for $package_name
    python setup.py develop
done
