import yaml
from testpage import OperationsHelper
from post_page import OperationsAddPost
from contact_page import OperationsContactForm
import time
import logging

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

login = testdata['login']
password = testdata['password']
alert_text = testdata['alert_text']

def test_step1(browser):
    logging.info("Test 1 starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    time.sleep(1)
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_btn()
    assert testpage.get_error_text() == "401"

def test_step2(browser):
    logging.info("Test 2 starting")
    testpage = OperationsHelper(browser)
    testpage.enter_login(login)
    time.sleep(1)
    testpage.enter_pass(password)
    testpage.click_login_btn()
    assert testpage.auth() == f"Hello, {login}"

def test_step3(browser):
    logging.info("Test 3 starting")
    testpage = OperationsAddPost(browser)
    testpage.add_post()
    time.sleep(1)
    title = "Test1"
    testpage.fill_post_info(title=title, description="Test1", content="Test1")
    time.sleep(1)
    assert testpage.check_post() == title

def test_step4(browser):
    logging.info("Test 4 starting")
    testpage = OperationsAddPost(browser)
    testpage.go_to_site()
    testpage.add_post()
    time.sleep(1)
    title = "Test2"
    testpage.fill_post_info(title=title, description="Test2")
    time.sleep(1)
    assert testpage.check_post() == title

def test_step5(browser):
    logging.info("Test 5 starting")
    testpage = OperationsAddPost(browser)
    testpage.go_to_site()
    testpage.add_post()
    time.sleep(1)
    title = "Test3"
    testpage.fill_post_info(title="Test3", content="Test3")
    time.sleep(1)
    assert testpage.check_post() == title

def test_step6(browser):
    logging.info("Test 6 starting")
    testpage = OperationsAddPost(browser)
    testpage.go_to_site()
    testpage.add_post()
    time.sleep(1)
    title = "Test4"
    testpage.fill_post_info(title='Test4')
    time.sleep(1)
    assert testpage.check_post() == title

def test_step7(browser):
    logging.info("Test 7 starting")
    testpage = OperationsContactForm(browser)
    testpage.go_to_site()
    time.sleep(1)
    testpage.contact_form_open()
    time.sleep(1)
    testpage.fill_contact_form(name='Nata', email='qq@ya.ru', content='Help me')
    time.sleep(1)
    assert testpage.check_text_alert() == alert_text
