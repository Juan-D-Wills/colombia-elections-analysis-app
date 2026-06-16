# !/bin/bash

# Run postgres container
docker run  --name postgres-db \
            -e POSTGRES_PASSWORD=123 \
            -e POSTGRES_DB=colombia_elections \
            -v $(pwd)/data/raw/presidential/:/tmp/presidential/ \
            -v $(pwd)/data/raw/senate/:/tmp/senate/ \
            -v $(pwd)/db.init/:/docker-entrypoint-initdb.d/ \
            -v pgdata:/var/lib/postgresql/data \
            --expose 5432 \
            -d \
            --rm \
            postgres:17

# Show logs
docker logs -f postgres-db

# Enter postgres-db container
docker exec -it postgres-db bash
docker exec -it postgres-db psql -U postgres -d colombia_elections

# Stop postgres-db container
docker stop postgres-db && docker container prune -f

# Restart postgres-db container
docker restart postgres-db