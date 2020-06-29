#!/bin/bash

docker pull cryptonomictech/conseil:latest

docker rename conseil "conseil-$1"

sudo -i -u postgres

createdb "conseil-$1" --username="user" --password="password"

psql "conseil-$1" -f data/conseil.sql

exit

#docker run -e XTZ_Host=localhost -e XTZ_Port="$2" -e XTZ_Network="$3" -e API_PORT="$4" -e DB_Database="conseil-$1" "conseil-$1" conseil-lorre

#docker run -e XTZ_Host=localhost -e XTZ_Port="$2" -e XTZ_Network="$3" -e API_PORT="$4" -e DB_Database="conseil-$1" "conseil-$1" "conseil-$1" conseil-api