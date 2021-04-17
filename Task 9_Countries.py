import pytest
from selenium import webdriver
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd

#---------------------------------- Part 1----------------------------------------
def test_countries(driver):
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
    driver.get("http://localhost:8080/litecart/admin/?app=countries&doc=countries")
    time.sleep(3)
    all_countries = driver.find_elements_by_css_selector("tr.row")
    print("Общее количество стран:"+str(len(all_countries)))
    #countries = driver.find_elements_by_css_selector('tr.row td:nth-child(5)')
    country_list = []
    zones_count = []
    index_for_link = []
    acronym_countries = []
    countries = driver.find_elements_by_css_selector("table.dataTable tr.row")
    i = 0
    # Cтолбцы текущего тега tr
    for elements in countries:
        column = elements.find_elements_by_tag_name('td')
        country_list.append(column[4].get_attribute("textContent"))
        zones_count.append(column[5].get_attribute("textContent"))
        acronym_countries.append((column[3]).get_attribute("textContent"))
        if int(column[5].text) > 0:
            index_for_link.append(i)
        i = i + 1
    sorted_country_list = sorted(country_list)
    assert country_list == sorted_country_list
    print("Страны: " + str(country_list))
    print("Зоны: " + str(zones_count))
    print("Количесвто зон у стран: " + str(index_for_link))
    print("Акронимы стран: " + str(acronym_countries))
    # Cортировка зон
    for i in index_for_link:
        zone_page = ("http://localhost:8080/litecart/admin/?app=countries&doc=edit_country&country_code=" + str(acronym_countries[i]))
        print(zone_page)
    for i in range(len(zone_page)):
        geozones_list_zone = []
        #driver.get(zone_page[i])
        # Список зон
        geozones_selects = driver.find_elements_by_css_selector("tbody tr tr:not(.header) td:nth-child(3)")
        for geozones in geozones_selects:
            geozones_list_zone.append(geozones.text)
            # Сравнение списка зон на странице и отсортированного списка
            sorted_geozones_list = sorted(geozones_list_zone)
            #print(geozones_list_zone)
            assert geozones_list_zone ==sorted_geozones_list


#----------------------------- Part 2 --------------------------------------
#
def test_geozones(driver):
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
    driver.get("http://localhost:8080/litecart/admin/?app=geo_zones&doc=geo_zones")
    time.sleep(1)
    driver.implicitly_wait(10)
    geozones_list = []
    geo_links = driver.find_elements_by_css_selector("tr.row td:not([style*='text']) a")
    for link in geo_links:
        geozones_list.append(link.get_attribute('href'))
        #print(geozones_list)
    for i in range(len(geozones_list)):
        geozones_list_zone = []
        driver.get(geozones_list[i])
        geozones_selects = driver.find_elements_by_css_selector("tbody tr tr:not(.header) td:nth-child(3)")
        for geozones in geozones_selects:
            geozones_list_zone.append(geozones.text)
        sorted_geozones_list = sorted(geozones_list_zone)
        print(geozones_list_zone)
        assert geozones_list_zone == sorted_geozones_list
        time.sleep(1)


#

