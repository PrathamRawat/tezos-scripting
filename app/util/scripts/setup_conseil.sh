#!/bin/bash

docker pull cryptonomictech/conseil:latest

createdb "conseil_$1"

psql "conseil_$1" -f util/data/conseil.sql

# Create postgres user for conseil
psql -d "conseil_$1" -U $(whoami) -c "CREATE ROLE conseil WITH LOGIN SUPERUSER CREATEDB PASSWORD 'conseil';"

#docker run -e XTZ_Host=localhost -e XTZ_Port="$2" -e XTZ_Network="$3" -e API_PORT="$4" -e DB_Database="conseil-$1" "conseil-$1" conseil-lorre

#docker run -e XTZ_Host=localhost -e XTZ_Port="$2" -e XTZ_Network="$3" -e API_PORT="$4" -e DB_Database="conseil-$1" "conseil-$1" "conseil-$1" conseil-api