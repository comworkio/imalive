#!/bin/bash

REPO_PATH="/home/centos/imalive/"

cd "${REPO_PATH}" && git pull origin main || :
git push github main 
git push pgitlab main
exit 0
