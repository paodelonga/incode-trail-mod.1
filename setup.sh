#!/usr/bin/bash

# Project
_HERE="$PWD"


# Root
touch requirements{-dev,-app,}.in

_ROOT_FILES=(
  "$HOME/pyproject.toml"
  "$HOME/.editorconfig"
)

for _FILE in ${_ROOT_FILES[@]}; do
  _FILENAME=$(echo "$_FILE" | sed 's/.*\///')

  if ! [[ -r "$_HERE/$_FILENAME" ]]; then
    cp "$_FILE" "$_HERE/$_FILENAME"
  fi
done


# # Application
# mkdir -p $_APP_PATH/{config,database}
# touch $_APP_PATH/VERSION.txt
# touch $_APP_PATH/__main__.py
# touch $_APP_PATH/{config,database,}/__init__.py


# Git
if ! [[ -r "$_HERE/.gitignore" ]]; then
  wget -q 'https://github.com/github/gitignore/raw/main/Python.gitignore' \
    -O "$_HERE/.gitignore"
fi
