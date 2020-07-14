#!/bin/bash

docker pull cryptonomictech/conseil:latest

docker pull postgres

docker run -d --name "conseil-postgres-$1" -e POSTGRES_SUPERUSER="conseil" -e POSTGRES_PASSWORD="conseil" -e POSTGRES_DB="conseil" -p "$2:5432" postgres

sleep 5s

docker cp "./util/data/conseil.sql" "conseil-postgres-$1:/conseil.sql"

docker exec -u postgres "conseil-postgres-$1" psql conseil -f "/conseil.sql"