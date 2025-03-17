#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset

# Debugging: Print environment variables before running Python
echo "🔍 Checking environment variables..."
echo "POSTGRES_DB=${POSTGRES_DB}"
echo "POSTGRES_USER=${POSTGRES_USER}"
echo "POSTGRES_PASSWORD=${POSTGRES_PASSWORD}"
echo "POSTGRES_HOST=${POSTGRES_HOST}"
echo "POSTGRES_PORT=${POSTGRES_PORT}"

python << END
import sys
import time
import os
import psycopg2

SUGGEST_UNRECOVERABLE_AFTER = 30  # Max wait time before failure
start = time.time()

while True:
    try:
        print(" Attempting to connect to PostgreSQL with:")
        print(f"  DB: {os.getenv('POSTGRES_DB')}")
        print(f"  USER: {os.getenv('POSTGRES_USER')}")
        print(f"  HOST: {os.getenv('POSTGRES_HOST')}")
        print(f"  PORT: {os.getenv('POSTGRES_PORT')}")

        conn = psycopg2.connect(
            dbname=os.getenv("POSTGRES_DB"),
            user=os.getenv("POSTGRES_USER"),
            password=os.getenv("POSTGRES_PASSWORD"),
            host=os.getenv("POSTGRES_HOST"),
            port=os.getenv("POSTGRES_PORT"),
        )
        print(" Successfully connected to PostgreSQL!")
        conn.close()
        break  # Exit loop after successful connection
    except psycopg2.OperationalError as error:
        print(f" PostgreSQL connection failed: {error}")
        if time.time() - start > SUGGEST_UNRECOVERABLE_AFTER:
            print(" This is taking too long. Exiting.")
            sys.exit(1)  # Ensure script exits if DB never becomes available
        time.sleep(3)
END

echo "✅ Running start.sh..."
exec /start.sh  # 🔥 This ensures `start.sh` actually runs!
