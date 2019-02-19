#!/bin/sh

cp ../requirements.txt ./requirements.txt
docker build -t division-service .
rm ./requirements.txt