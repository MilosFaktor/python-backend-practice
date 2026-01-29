# commands.sh

# pyton venv
python3 -m venv .venv
source .venv/bin/activate
deactivate
pip freeze > requirements.txt

# python module run
PYTHONPATH=src python -m xs14.main
PYTHONPATH=src python sandbox.py

# set PYTHONPATH into .venv
source .venv/bin/activate && export PYTHONPATH="$(pwd)/src" && echo $PYTHONPATH

# and after i can use only
python -m xs14.main
python sandbox.py

