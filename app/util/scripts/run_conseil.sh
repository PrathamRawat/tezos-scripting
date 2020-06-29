#!/bin/bash

docker run -e XTZ_Host=localhost -e XTZ_Port="$2" -e XTZ_Network="$3" -e API_PORT="$4" -e DB_Database="conseil-$1" "conseil-$1" conseil-lorre

docker run -e XTZ_Host=localhost -e XTZ_Port="$2" -e XTZ_Network="$3" -e API_PORT="$4" -e DB_Database="conseil-$1" "conseil-$1" "conseil-$1" conseil-api