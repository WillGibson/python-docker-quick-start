#!/usr/bin/env bash

set -e

arguments="$*"
dockerComposeArgs=""

if [[ "$arguments" == *"--recreate-containers"* ]]; then
   dockerComposeArgs="$dockerComposeArgs --force-recreate"
fi

docker-compose up -d $dockerComposeArgs
docker-compose exec python python --version
docker-compose exec python bash
