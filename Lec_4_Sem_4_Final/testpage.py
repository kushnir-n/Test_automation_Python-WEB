import time
import yaml
from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    
class TestSearchLocators:
    ids = dict()
    with open("locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])

class OperationsHelper(BasePage):

#main commands
    def enter_text_into_field(self, locator, word, description_loc=None):
        if description_loc:
            element_name = description_loc
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")
        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True
    
    def click_button(self, locator, description_loc=None):
        if description_loc:
            element_name = description_loc
        else:
            element_name = locator
        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True
    
    def get_text_from_element(self, locator, description_loc=None):
        if description_loc:
            element_name = description_loc
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get test from {element_name}")
            return None
        logging.debug(f"We find {text} in field {element_name}")
        return text

    #enter text
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"], word, description_loc="login field")
    
    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASS_FIELD"], word, description_loc="password field")

    def fill_post_info(self, title=None, description=None, content=None):
        if title:
            self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_TITLE"], title, description_loc="title field")
        if description:
            self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_DESCRIPTION"], description, description_loc="description field")
        if content:
            self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT"], content, description_loc="content field")

    def fill_contact_form(self, name, email, content):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_NAME_FIELD"], name, description_loc="name field")
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_EMAIL_FIELD"], email, description_loc="email field")
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT_FIELD"], content, description_loc="content field")
      
    #click
    def click_login_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"], description_loc="login button")

    def _add_post_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_ADD_POST_BTN"], description_loc="add post button")

    def create_post_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_POST_BTN"], description_loc="create post button")

    def contact_form_open_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_BTN"], description_loc="contact form open button")

    def contact_form_send_btn(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_US_BTN"], description_loc="contact form send button")

    #get text
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_ERROR_FIELD"], description_loc="error text")
    
    def get_auth_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_AUTH"], description_loc="auth text")
    
    def get_title_text(self):
        return self.get_text_from_element(TestSearchLocators.ids["LOCATOR_CHECK_POST"], description_loc="get title text")

    def get_alert(self):
        logging.info("Get alert text")
        text = self.get_alert_text()
        logging.info(text)
        return text