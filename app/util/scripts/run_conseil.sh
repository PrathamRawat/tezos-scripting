#!/bin/bash

docker run -e XTZ_Host=localhost -e XTZ_Port="$2" -e XTZ_Network="$3" -e API_PORT="$4" -e DB_Database="conseil_$1" "cryptonomictech/conseil" "conseil-lorre" --name "conseil-lorre-$1"

docker run -e XTZ_Host=localhost -e XTZ_Port="$2" -e XTZ_Network="$3" -e API_PORT="$4" -e DB_Database="conseil_$1" "cryptonomictech/conseil" "conseil-api" --name "conseil-api-$1"