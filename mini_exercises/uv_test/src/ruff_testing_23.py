import datetime
import json
import os
import uuid
from pathlib import Path
from typing import Dict, List

from flask import Flask, jsonify, request

app = Flask(__name__)


def load_users(file_path: Path) -> List[Dict[str, str]]:
    if not file_path.exists():
        raise FileNotFoundError(f"{file_path} not found")

    with open(file_path) as f:
        return json.load(f)


def create_user(name: str, age: int) -> Dict[str, str]:
    return {
        "id": str(uuid.uuid4()),
        "name": name,
        "age": age,
        "created_at": datetime.datetime.utcnow().isoformat(),
    }


@app.route("/users", methods=["POST"])
def users():
    payload = request.json
    user = create_user(payload["name"], payload["age"])
    return jsonify(user), 201


if __name__ == "__main__":
    data_path = Path(os.getcwd()) / "users.json"
    print(load_users(data_path))
    app.run(debug=True)
