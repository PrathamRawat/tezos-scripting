#!/bin/bash

docker run -e XTZ_Host="localhost" -e XTZ_Port="$2" -e XTZ_Network="$3" -e API_PORT="$4" -e DB_Database="conseil_$1" --name "conseil-lorre-$1" -d "cryptonomictech/conseil:latest" "lorre"

docker run -e XTZ_Host="localhost" -e XTZ_Port="$2" -e XTZ_Network="$3" -e API_PORT="$4" -e DB_Database="conseil_$1" --name "conseil-api-$1" -d "cryptonomictech/conseil:latest" "conseil"