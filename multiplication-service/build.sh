#!/bin/sh

cp ../requirements.txt ./requirements.txt
docker build -t multiplication-service .
rm ./requirements.txt