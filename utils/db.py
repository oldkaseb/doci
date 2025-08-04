import json
import os

DB_PATH = "data/users.json"
ADMINS_PATH = "data/admins.json"
BLOCKED_PATH = "data/blocked.json"

def load_json(path):
    if not os.path.exists(path):
        with open(path, "w") as f:
            json.dump({}, f)
    with open(path, "r") as f:
        return json.load(f)

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def get_users():
    return load_json(DB_PATH)

def save_user(user_id, data):
    users = get_users()
    users[str(user_id)] = data
    save_json(DB_PATH, users)

def get_admins():
    return load_json(ADMINS_PATH)  # چون لیسته، نیازی به .keys() نیست

def add_admin(user_id):
    admins = load_json(ADMINS_PATH)
    admins[str(user_id)] = True
    save_json(ADMINS_PATH, admins)

def remove_admin(user_id):
    admins = load_json(ADMINS_PATH)
    admins.pop(str(user_id), None)
    save_json(ADMINS_PATH, admins)

def is_admin(user_id):
    return str(user_id) in load_json(ADMINS_PATH)

def is_blocked(user_id):
    return str(user_id) in load_json(BLOCKED_PATH)
