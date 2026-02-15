# docker run myimage
docker compose up

# docker build .
# docker run myimage
docker compose up --build

# launch in backround
docker compose up -d

# stop containers
docker compose down

# running containers
docker compose ps


# restart policies
- "no"
- always
- on-failure
- unless-stopped