# commands.sh

# pyton venv
python3 -m venv .venv
source .venv/bin/activate
deactivate
pip freeze > requirements.txt


# set PYTHONPATH into .venv
source .venv/bin/activate && export PYTHONPATH="$(pwd)/src" && echo $PYTHONPATH


# and after i can use only with 'ok' data as default
python -m xs14.main
# run with bad data
MODE=bad python -m xs14.main


# build docker image
docker build -t milosfaktor/xs14:v1 .
# list docker images 
docker image ls


# run docker -rm flag removes container after execution
# runs with 'ok' data by default
docker run --rm milosfaktor/xs14:v1
# runs with 'bad' data by default
docker run --rm -e MODE=bad milosfaktor/xs14:v1


# list docker containers
docker ps -a
docker rm <container_id>



