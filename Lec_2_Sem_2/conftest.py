import pytest
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

login = testdata['login']
title = testdata['title']

@pytest.fixture()
def sel_1():
    return """//*[@id="login"]/div[1]/label/input"""

@pytest.fixture()
def sel_2():
    return """//*[@id="login"]/div[2]/label/input"""

@pytest.fixture()
def sel_3():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""

@pytest.fixture()
def btn_sel():
    return "button"


@pytest.fixture()
def code_res():
    return "401"

@pytest.fixture()
def auth():
    return '//*[@id="app"]/main/nav/ul/li[3]/a'

@pytest.fixture()
def result():
    return f"Hello, {login}"

@pytest.fixture()
def btn_createpost():
    return """//*[@id="create-btn"]"""

@pytest.fixture()
def input_title():
    return """/html/body/div/main/div/div/form/div/div/div[1]/div/label/input"""

@pytest.fixture()
def input_des():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""

@pytest.fixture()
def input_cont():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""

@pytest.fixture()
def btn_savepost():
    return """//*[@id="create-item"]/div/div/div[7]/div/button/span"""

@pytest.fixture()
def check_post():
    return """//*[@id="app"]/main/div/div[1]/h1"""

@pytest.fixture()
def result1():
    return title
