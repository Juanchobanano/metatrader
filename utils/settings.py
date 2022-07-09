import json
ACCOUNTS_PATH = "./credentials/accounts.json"
SERVER = "MetaQuotes-Demo"
with open(ACCOUNTS_PATH, "r") as f:
    accounts = json.load(f)["accounts"]