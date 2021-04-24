import pytest
from selenium import webdriver
import time
import os

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

def find_and_fill(driver, element_name, value):
    driver.find_element_by_name(element_name).click()
    driver.find_element_by_name(element_name).clear()
    driver.find_element_by_name(element_name).send_keys(value)

def test_add_new_product(driver):
    driver.get("http://localhost:8080/litecart/admin/")
    #time.sleep(1)
    find_and_fill(driver, element_name='username', value="admin")
    find_and_fill(driver, element_name="password", value="admin")
    #time.sleep(2)
    driver.find_element_by_name('login').click()
    driver.implicitly_wait(10)
    menu_catalog = driver.find_element_by_link_text("Catalog")
    menu_catalog.click()
    driver.implicitly_wait(10)
    time.sleep(1)
    driver.find_element_by_css_selector('[href$="edit_product"]').click()
    # Заполнение вкладки General
    driver.implicitly_wait(10)
    #("label input:not([checked=checked]")
    driver.find_element_by_css_selector("[type='radio'][name='status'][value='1']").click()
    driver.implicitly_wait(10)
    find_and_fill(driver, element_name="name[en]", value="New Dack")
    time.sleep(1)
    driver.implicitly_wait(10)
    find_and_fill(driver, element_name="code", value="123rew")
    time.sleep(1)
    driver.find_element_by_css_selector("[type='checkbox'][value='0']").click()
    driver.find_element_by_css_selector("[type='checkbox'][value='1']").click()
    time.sleep(1)
    find_and_fill(driver, element_name="quantity", value="10" )
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector("[name='sold_out_status_id'] option[value='2']").click()
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector("[name='new_images[]']").send_keys(os.path.abspath("../product_image.png"))
    time.sleep(3)
    driver.find_element_by_name("date_valid_from").click()
    driver.find_element_by_name('date_valid_from').send_keys("20-04-2021")
    time.sleep(1)
    driver.find_element_by_name("date_valid_to").click()
    driver.find_element_by_name("date_valid_to").send_keys("25-04-2021")
    # Заполнение вкладки Information
    #('form div ul li:nth-child(2) a')
    driver.find_element_by_xpath("//a[contains(text(), 'Information')]").click()
    time.sleep(2)
    #information_page.get_attribute("href")
    #driver.execute_script("arguments[0].style.opacity = 1", information_page)
    driver.find_element_by_css_selector("[name='manufacturer_id'] option[value='1']").click()
    time.sleep(1)
    find_and_fill(driver, element_name="short_description[en]", value="new duck")
    time.sleep(1)
    driver.find_element_by_css_selector('.trumbowyg-editor').send_keys("mynewduck")
    # Заполнение вкладки Prices
    driver.find_element_by_xpath("//a[contains(text(), 'Price')]").click()
    find_and_fill(driver, element_name="purchase_price", value="10")
    time.sleep(2)
    driver.implicitly_wait(10)
    find_and_fill(driver, element_name="prices[USD]", value="20.0000")
    time.sleep(2)
    find_and_fill(driver, element_name="prices[EUR]", value="0.0000")
    time.sleep(2)
    driver.find_element_by_css_selector("[name='save']").click()
    time.sleep(2)
















