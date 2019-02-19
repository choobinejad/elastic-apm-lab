#!/bin/sh

cp ../requirements.txt ./requirements.txt
docker build -t math-service .
rm ./requirements.txt