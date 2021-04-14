import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver(request):
    wd = webdriver.Edge()
    request.addfinalizer(wd.quit)
    return wd

def test_all_sections(driver):
    driver.get("http://localhost:8080/litecart/admin/")
    #time.sleep(1)
    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("admin")
    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("admin")
    #time.sleep(2)
    login_button = driver.find_element_by_name('login').click()
    driver.implicitly_wait(10)
    menu = driver.find_elements_by_css_selector("li#app-")
    sub_menu = driver.find_elements_by_css_selector("ul.docs li")
    for i in range(len(menu)):
        menu = driver.find_elements_by_css_selector("li#app-")
        menu[i].click()
        try:
            heading = driver.find_element_by_tag_name('h1')
        except:
            NoSuchElementException
        time.sleep(0.1)
        driver.implicitly_wait(10)
        # подменю
        sub_menu = driver.find_elements_by_css_selector("ul.docs li")
        for j in range(len(sub_menu)):
            sub_menu = driver.find_elements_by_css_selector("ul.docs li")
            sub_menu[j].click()
            driver.implicitly_wait(10)
            try:
                heading = driver.find_element_by_tag_name('h1')
            except:
                NoSuchElementException
    WebDriverWait(driver, 5).until(EC.title_is("vQmods | My Store"))



