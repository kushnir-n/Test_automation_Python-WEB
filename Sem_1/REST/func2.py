import json
import requests
import yaml

with open ("D:\Python_WEB_hw\Sem_1\REST\config.yaml", "r") as f:
    d = yaml.safe_load(f)

def registry():
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'name': d["username"],
        'email': d["email"],
        'password': d["password"],
    }

    res = requests.post(url=d["url_reg"], data=json.dumps(data), headers=headers)
    return res.json()["data"]["Token"]

def auth():
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'email': d["email"],
        'password': d["password"],
    }
    res = requests.post(url=d["url_auth"], headers=headers, data=json.dumps(data))
    return res.status_code

#auth()