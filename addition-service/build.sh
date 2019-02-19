#!/bin/sh

cp ../requirements.txt ./requirements.txt
docker build -t addition-service .
rm ./requirements.txt