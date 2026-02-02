# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "requests>=2.32.5",
# ]
# ///
import requests

print(type(requests.get("https://astral.sh")))
