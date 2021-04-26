import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(chrome_options=options)
    request.addfinalizer(wd.quit)
    return wd


def test_basket(driver):
    driver.get("http://localhost:8080/litecart/en/")
    for i in range(1,4):
        products = driver.find_elements_by_css_selector("div#box-most-popular ul.listing-wrapper.products li:nth-child(1)")
        for product in products:
            product.click()
            driver.find_element_by_css_selector("[name=add_cart_product]").click()
            wait = WebDriverWait(driver, 10)
            wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "span.quantity"), str(i)))
        driver.get("http://localhost:8080/litecart/en/")
    driver.get("http://localhost:8080/litecart/en/checkout")
    driver.find_element_by_css_selector("ul.shortcuts li:nth-child(1)").click() # Остановить карусель
    table_of_products = driver.find_elements_by_css_selector("td.unit-cost")
    for i in range(len(table_of_products)):
        driver.find_element_by_name("remove_cart_item").click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.staleness_of(table_of_products[i]))










