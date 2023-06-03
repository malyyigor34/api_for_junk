#!/bin/sh

docker build -t ihormalyi34/junk_api:v1 .
docker images

docker tag ihormalyi34/junk_api:v1 ihormalyi34/junk_api:v1-release
docker push ihormalyi34/junk_api:v1-release
