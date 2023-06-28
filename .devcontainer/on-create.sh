#!/bin/bash

# Update the submodules, if present
git submodule update --init --recursive

## We cleanup git's 'blame' feature by ignoring certain commits (typically
## commits that have reformatted files)
git config --global blame.ignoreRevsFile .git-blame-ignore-revs
