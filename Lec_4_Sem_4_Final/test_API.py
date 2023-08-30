import yaml
import requests
import logging

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

def test_step1(login, testtext):
    logging.info("Test 1 starting (API)")
    header = {"X-Auth-Token": login}
    res = requests.get(testdata["address"] + "api/posts", params={"owner":"notMe"}, headers=header)
    listres = [i["title"] for i in res.json()["data"]]
    assert testtext in listres, "Test 1 FAIL (API)"

def test_step2(login):
    logging.info("Test 2 starting (API)")
    header = {"X-Auth-Token": login}
    res1 = requests.post(testdata["address"] + "api/posts", params={"title":"Python", "description":"Python", "content":"Python"}, headers=header)
    res2 = requests.get(testdata["address"] + "api/posts", params={"description":"Python"}, headers=header)
    #print (res2.content)
    assert res1 and res2, "Test 2 FAIL (API)"