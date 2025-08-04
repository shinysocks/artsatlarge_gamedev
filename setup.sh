#!/bin/bash -i
#
#    ▄▄▄· ▄▄▄  ▄▄▄▄▄.▄▄ ·      ▄▄▄· ▄▄▄▄▄    ▄▄▌   ▄▄▄· ▄▄▄   ▄▄ • ▄▄▄ .
#   ▐█ ▀█ ▀▄ █·•██  ▐█ ▀.     ▐█ ▀█ •██      ██•  ▐█ ▀█ ▀▄ █·▐█ ▀ ▪▀▄.▀·
#   ▄█▀▀█ ▐▀▀▄  ▐█.▪▄▀▀▀█▄    ▄█▀▀█  ▐█.▪    ██▪  ▄█▀▀█ ▐▀▀▄ ▄█ ▀█▄▐▀▀▪▄
#   ▐█ ▪▐▌▐█•█▌ ▐█▌·▐█▄▪▐█    ▐█ ▪▐▌ ▐█▌·    ▐█▌▐▌▐█ ▪▐▌▐█•█▌▐█▄▪▐█▐█▄▄▌
#    ▀  ▀ .▀  ▀ ▀▀▀  ▀▀▀▀      ▀  ▀  ▀▀▀     .▀▀▀  ▀  ▀ .▀  ▀·▀▀▀▀  ▀▀▀ 
#                ▄▄ •  ▄▄▄· • ▌ ▄ ·. ▄▄▄ .·▄▄▄▄  ▄▄▄ . ▌ ▐·             
#               ▐█ ▀ ▪▐█ ▀█ ·██ ▐███▪▀▄.▀·██▪ ██ ▀▄.▀·▪█·█▌             
#               ▄█ ▀█▄▄█▀▀█ ▐█ ▌▐▌▐█·▐▀▀▪▄▐█· ▐█▌▐▀▀▪▄▐█▐█•             
#               ▐█▄▪▐█▐█ ▪▐▌██ ██▌▐█▌▐█▄▄▌██. ██ ▐█▄▄▌ ███              
#               ·▀▀▀▀  ▀  ▀ ▀▀  █▪▀▀▀ ▀▀▀ ▀▀▀▀▀•  ▀▀▀ . ▀               
#
# Use the command below to set up your development environment
# $ source <(curl -s shinysocks.net/s/aal)

# install homebrew and python

curl -O shinysocks.net/s/aal.zip
unzip aal.zip

mv aal artsatlarge_gamedev

cd artsatlarge_gamedev

python3 --version || open ./bin/python.pkg

python3 -m venv .venv

. .venv/bin/activate

python3 -m pip install .

# install vscode
cd ./bin/
curl -# -L -o vsc.zip "https://code.visualstudio.com/sha/download?build=stable&os=darwin-universal" | cat
unzip vsc.zip

# https://code.visualstudio.com/docs/editor/portable
# un-quarantine vscode app
xattr -dr com.apple.quarantine Visual\ Studio\ Code.app && rm -rf vsc.zip

cd ..

open ./bin/Visual\ Studio\ Code.app ./src/template.py

