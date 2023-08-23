#Задание
#Условие: Добавить в наш тестовый проект шаг добавления поста после входа. Должна выполняться проверка на наличие названия поста на странице сразу после его создания.
#Совет: не забудьте добавить небольшие ожидания перед и после нажатия кнопки создания поста.

import yaml
from module import Site
import time

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)

site = Site(testdata["address"])
login = testdata['login']
password = testdata['password']
title = testdata['title']
description = testdata['description']
content = testdata['content']

def test_step1(sel_1, sel_2, sel_3, btn_sel, code_res):
    input1 = site.find_element("xpath", sel_1)
    input1.send_keys("test")
    input2 = site.find_element("xpath", sel_2)
    input2.send_keys("test")
    btn = site.find_element("css", btn_sel)
    btn.click()
    err_label = site.find_element("xpath", sel_3)
    res = err_label.text
    assert res == code_res

def test_step2(sel_1, sel_2, result, auth, btn_sel):
    input1 = site.find_element("xpath", sel_1)
    input1.clear()
    input1.send_keys(login)
    input2 = site.find_element("xpath", sel_2)
    input2.clear()
    input2.send_keys(password)
    btn = site.find_element("css", btn_sel)
    btn.click()
    auth = site.find_element("xpath", auth)
    res = auth.text
    #site.close_connection()
    assert res == result

def test_step3(btn_createpost, input_title, input_des, input_cont, btn_savepost, check_post, result1):
    time.sleep(1)
    btn = site.find_element("xpath", btn_createpost)
    time.sleep(1)
    btn.click()
    time.sleep(1)
    input1 = site.find_element("xpath", input_title)
    input1.send_keys(title)
    time.sleep(1)
    input2 = site.find_element("xpath", input_des)
    input2.send_keys(description)
    time.sleep(1)
    input3 = site.find_element("xpath", input_cont)
    input3.send_keys(content)
    time.sleep(1)
    btn = site.find_element("xpath", btn_savepost)
    time.sleep(1)
    btn.click()
    time.sleep(1)
    check_post = site.find_element("xpath", check_post)
    res = check_post.text
    site.close_connection()
    assert res == result1

#login > div.submit.svelte-uwkxn9 > button > div

# css_selector = 'span.mdc-text-field__ripple'
# print(site.get_element_property("css", css_selector, "height"))

# xpath = '//*[@id="login"]/div[3]/button/div'
# print(site.get_element_property('xpath', xpath, 'color'))