# sandbox.py

from xs14.ingest import read_json_file
from xs14.validate import validate_raw

# from xs14.validate import

json_path = "data/users_raw.json"
result = read_json_file(json_path)

validated = validate_raw(result)
print(validated)
