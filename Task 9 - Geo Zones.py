import pytest
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(options=options)
    request.addfinalizer(wd.quit)
    return wd


def find_and_fill(driver, element_name, value):
    driver.find_element_by_name(element_name).click()
    driver.find_element_by_name(element_name).clear()
    driver.find_element_by_name(element_name).send_keys(value)
    

def test_geozones(driver):
    driver.get("http://localhost/litecart/admin/")
    find_and_fill(driver, element_name="username", value="admin")
    find_and_fill(driver, element_name="password", value="admin")
    driver.find_element_by_name("login").click()
    driver.implicitly_wait(10)
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    time.sleep(1)
    driver.implicitly_wait(10)
    geozones_list_country = []
    geo_links = driver.find_elements_by_css_selector("tr.row td:not([style*='text']) a")
    print(geo_links)
    for link in geo_links:
        geozones_list_country.append(link.get_attribute('href'))
        print(geozones_list_country)
    for i in range(len(geozones_list_country)):
        geozones_list_new = []
        driver.get(geozones_list_country[i])
        geozones_selects = driver.find_elements_by_css_selector("tbody select:not([class='select2-hidden-accessible']) option[selected='selected']")
        for geozones in geozones_selects:
            geozones_list_new.append(geozones.text)
        sorted_geozones_list = sorted(geozones_list_new)
        # print(str(sorted_geozones_list) + "\n")
        # print(str(geozones_list_new) + "\n")
        assert geozones_list_new == sorted_geozones_list

#