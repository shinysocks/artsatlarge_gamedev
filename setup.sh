#!/bin/bash -i

# install homebrew and python
NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install python

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

open Visual\ Studio\ Code.app

