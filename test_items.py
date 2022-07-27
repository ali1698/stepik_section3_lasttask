import pytest
import time
from selenium import webdriver

def test_link(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    assert browser.find_element_by_css_selector(".btn-add-to-basket"), "Button not found"
    time.sleep(30)

