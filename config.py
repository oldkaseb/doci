import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "123456789"))
ADMINS_FILE = "admins.json"
USERS_FILE = "users.json"