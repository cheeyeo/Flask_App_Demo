#!/bin/bash

set -e

psql -V ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  CREATE USER chee;
  CREATE DATABASE example;
  GRANT ALL PRIVILEGES ON DATABASE example TO chee;
EOSQL