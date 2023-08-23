import pytest
import yaml
import requests

with open("D:\Python_WEB_hw\Sem_1\HW_Sem1\config.yaml", "r") as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def login():
    res1 = requests.post(data["address"] + "gateway/login", data={"username": data["username"], "password": data["password"]})
    print(res1.content)
    return res1.json()["token"]

@pytest.fixture()
def testtext1():
    return 'Title of practice#2'