# commands.sh

# pyton venv
python3 -m venv .venv
source .venv/bin/activate
deactivate
pip freeze > requirements.txt


# set PYTHONPATH into .venv
source .venv/bin/activate && export PYTHONPATH="$(pwd)/src" && echo $PYTHONPATH


# and after i can use only
python -m xs14.main


