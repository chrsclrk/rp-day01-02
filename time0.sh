#!/usr/bin/env bash

##VARIABLES
REPOSITORY='chrsclrk/rp-day01-02'
DESCRIPTION='Day01-02: Real Python sample program second_brain.'


# Create the remote repo — empty (no README, .gitignore, or license)
gh repo create $REPOSITORY \
  --public \
  --description "$DESCRIPTION"

# Initialise the local repo with an explicit branch name
git init --initial-branch=main

# Git requies at the minimum one file staged to make a commit.
git add README.md

# Initial commit
git commit --message "First commit."

# Wire the remote
git remote add origin git@github.com:$REPOSITORY.git

# Push and track
git push --set-upstream origin main

# Pull from origin
git pull --no-rebase origin main

# Summary
printf '\n*** Summary ***\n'
printf '\n+++ git status +++\n'
git status
printf '\n+++ git remote --verbose +++\n'
git remote --verbose
