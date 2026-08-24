import json
from pathlib import Path

def read_json_file(filename):
    file_path = Path(__file__).resolve().parent.parent / "data" / filename

    with open(file_path, "r") as f:
        return json.load(f)

def load_login_data():
    data = read_json_file("login_data.json")
    u = data["valid_credentials"]
    valid_credentials = [(u["username"], u["password"])]
    invalid_credentials = [(u["username"], u["password"]) for u in data["invalid_credentials"]]

    return valid_credentials, invalid_credentials

def load_employee_data():
    data = read_json_file("employee_data.json")
    return [(emp["first_name"], emp["last_name"]) for emp in data]

def load_admin_data():
    return read_json_file("admin_data.json")



