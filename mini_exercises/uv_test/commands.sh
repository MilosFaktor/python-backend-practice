# uv commands.sh

uv python list
uv python install <version>
uv python find <version>
uv python uninstall <version>


uv init
uv add -r requirements.txt # install depends from the requirements.txt if there is some
uv add requests
uv add --script example.py requests # managing dependancies for a single file and dont add to pyproject.toml
uv remove requests

uv tree # tree of dependencies

uv sync
uv run main.py

# install tool
uv tool install ruff # installs tool globally reusable 
which ruff
# remove tool
uv tool uninstall ruff

# testing tools without install
uv tool run ruff check
uvx ruff check # shortcut of the line above
which ruff

uv tool list
uv tool upgrade --all