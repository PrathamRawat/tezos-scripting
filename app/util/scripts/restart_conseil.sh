#!/bin/bash

docker start -e XTZ_Host="localhost" -e XTZ_Port="$2" -e XTZ_Network="$3" -e API_PORT="$4" -e DB_User="conseil" -e DB_Password="conseil" -e DB_Database="conseil_$1" -e DB_Port="5432" -e DB_Host="localhost" --name "conseil-lorre-$1" --network="host" -d "cryptonomictech/conseil:latest" "lorre"

docker start -e XTZ_Host="localhost" -e XTZ_Port="$2" -e XTZ_Network="$3" -e API_PORT="$4" -e DB_User="conseil" -e DB_Password="conseil" -e DB_Database="conseil_$1" -e DB_Port="5432" -e DB_Host="localhost" --name "conseil-api-$1" --network="host" -d "cryptonomictech/conseil:latest" "conseil"