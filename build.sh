#!/bin/bash
#pip install sunvox-dll-python
pip install --ignore-installed  --install-option="--prefix=$(pwd)" SunVOSC
pip install --upgrade pip enum34
7z a installer.7z enum pythonosc sunvox main.py test.sunvox
echo "now run 7z SFX builder"
