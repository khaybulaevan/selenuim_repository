import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(chrome_options=options)
    request.addfinalizer(wd.quit)
    return wd


def test_registration(driver):
    driver.get("http://localhost:8080/litecart/en/")
    link_registration = driver.find_element_by_css_selector("table tbody tr:nth-child(5) a").get_attribute('href')
    driver.get(str(link_registration))
    time.sleep(0.5)
    tax_id = driver.find_element_by_name('tax_id')
    tax_id.clear()
    tax_id.send_keys("12345")
    first_name = driver.find_element_by_name("firstname").send_keys("Adi")
    time.sleep(0.5)
    last_name = driver.find_element_by_name("lastname").send_keys("Darov")
    time.sleep(0.5)
    address1 = driver.find_element_by_name("address1").send_keys("Bragg Avenue, 22")
    time.sleep(0.5)
    address2 = driver.find_element_by_name("address2").send_keys("Bragg Avenue, 22")
    time.sleep(0.5)
    postcode = driver.find_element_by_name("postcode").send_keys("56438")
    time.sleep(0.5)
    city = driver.find_element_by_name('city').send_keys("Birmingham")
    time.sleep(0.5)
    country = driver.find_element_by_css_selector(".select2-selection__rendered")
    country.click()
    serch_country = driver.find_element_by_css_selector("input.select2-search__field")
    serch_country.send_keys("United States" + Keys.ENTER)
    time.sleep(0.5)
    еmail = driver.find_element_by_name("email").send_keys("adidarovbragg@gmail.com")
    time.sleep(0.5)
    phone = driver.find_element_by_name('phone')
    phone.clear()
    phone.send_keys("+1375759667")
    time.sleep(0.5)
    desired_password = driver.find_element_by_name('password')
    desired_password.clear()
    desired_password.send_keys('M57163222080')
    time.sleep(0.5)
    confirmed_password = driver.find_element_by_name("confirmed_password")
    confirmed_password.clear()
    confirmed_password.send_keys("M57163222080")
    button_create_account = driver.find_element_by_name("create_account").click()
    driver.implicitly_wait(10)
    time.sleep(2)
    # Выход
    logout = driver.find_element_by_link_text("Logout").click()
    # Повторный вход
    time.sleep(1)
    driver.implicitly_wait(10)
    email_address = driver.find_element_by_name("email")
    email_address.clear()
    email_address.send_keys("adidarovbragg@gmail.com")
    time.sleep(0.5)
    driver.implicitly_wait(10)
    password_page = driver.find_element_by_name("password")
    password_page.clear()
    password_page.send_keys("M57163222080")
    # Повторный выход
    time.sleep(2)
    logout = driver.find_element_by_name("login").click()

