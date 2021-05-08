from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest
import string
import random
import time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(chrome_options=options)
    request.addfinalizer(wd.quit)
    return wd

def find_and_fill (driver,selector_name, value):
    driver.find_element_by_name(selector_name).click()
    driver.find_element_by_name(selector_name).clear()
    driver.find_element_by_name(selector_name).send_keys(value)

domains = ['yandex.ru', 'mail.ru', 'gmail.com', 'hotnail.com', 'yahoo.com']
letters = string.ascii_lowercase[:12]
def random_donain(domains):
    return  random.choice(domains)
def random_name(letters, lenght):
    return ''.join(random.choice(letters) for i in range(lenght))
def random_email (nb,lenght):
    return [random_name(letters, lenght) + "@" + random_donain(domains) for i in range(nb)]
def generated_mail():
    return random_email(1, 7)

def test_registration(driver):
    mail = generated_mail()
    driver.get("http://localhost/litecart/en/")
    link_registration = driver.find_element_by_css_selector("table tbody tr:nth-child(5) a").get_attribute('href')
    driver.get(str(link_registration))
    find_and_fill(driver, 'tax_id', '12345')
    find_and_fill(driver, "firstname", "Adi")
    find_and_fill(driver, "lastname", "Darov")
    find_and_fill(driver, "address1", "Bragg Avenue, 22")
    find_and_fill(driver, "address2", "Bragg Avenue, 22")
    find_and_fill(driver, "postcode", "56438")
    find_and_fill(driver, 'city', "Birmingham")
    driver.find_element_by_css_selector(".select2-selection__rendered").click()
    search_country = driver.find_element_by_css_selector("input.select2-search__field")
    search_country.send_keys("United States" + Keys.ENTER)
    find_and_fill(driver, "email", (mail[0]))
    find_and_fill(driver, 'phone', "+1375759667")
    find_and_fill(driver, 'password', 'M57163222080')
    find_and_fill(driver, "confirmed_password", "M57163222080")
    driver.find_element_by_name("create_account").click()
    time.sleep(1)
    driver.implicitly_wait(10)
    # Выход
    driver.find_element_by_link_text("Logout").click()
    # Повторный вход
    driver.implicitly_wait(10)
    find_and_fill(driver, "email", (mail[0]))
    time.sleep(0.5)
    driver.implicitly_wait(10)
    find_and_fill(driver, "password", "M57163222080")
    driver.find_element_by_name("login").click()
    # Повторный выход
    driver.find_element_by_link_text("Logout").click()

