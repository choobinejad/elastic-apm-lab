#!/bin/sh

cd ./addition-service
sh build.sh
cd ../subtraction-service
sh build.sh
cd ../multiplication-service
sh build.sh
cd ../division-service
sh build.sh
cd ../math-service
sh build.sh