#!/bin/sh

cp ../requirements.txt ./requirements.txt
docker build -t subtraction-service .
rm ./requirements.txt