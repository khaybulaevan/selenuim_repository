import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost:8080/litecart/admin/")
    time.sleep(1)
    username = driver.find_element_by_name("username")
    username.clear()
    username.send_keys("admin")
    password = driver.find_element_by_name("password")
    password.clear()
    password.send_keys("admin")
    time.sleep(2)
    login_button = driver.find_element_by_name('login')
    login_button.click()
    link = driver.find_element_by_link_text('Appearence')
    link.click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.title_is("Template | My Store"))

