#!/bin/bash
touch .env
cp .env.example .env 
docker-compose -f docker-compose-local.yml up --build --abort-on-container-exit imalive-tests
