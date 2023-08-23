# Условие: Добавить в задание с REST API ещё один тест, в котором создаётся новый пост, а потом проверяется его наличие на сервере по полю «описание».
# Подсказка: создание поста выполняется запросом к https://test-stand.gb.ru/api/posts с передачей параметров title, description, content.

import yaml
import requests

with open("D:\Python_WEB_hw\Sem_1\HW_Sem1\config.yaml", "r") as f:
    data = yaml.safe_load(f)

def test_step1(login, testtext1):
    header = {"X-Auth-Token": login}
    res = requests.get(data["address"] + "api/posts", params={"owner":"notMe"}, headers=header)
    listres = [i["title"] for i in res.json()["data"]]
    assert testtext1 in listres, "test1 FAIL (HW)"

def test_step2(login):
    header = {"X-Auth-Token": login}
    res1 = requests.post(data["address"] + "api/posts", params={"title":"Python", "description":"Python", "content":"Python"}, headers=header)
    res2 = requests.get(data["address"] + "api/posts", params={"description":"Python"}, headers=header)
    #print (res2.content)
    assert res1 and res2, "test2 FAIL (HW)"