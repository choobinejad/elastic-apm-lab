#!/bin/sh

sh ./build-stack.sh
docker stack deploy -c docker-compose.yml mathstack