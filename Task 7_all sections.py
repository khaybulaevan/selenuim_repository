# Progaram by Naida.Kh
# Version       Date        Info
# 1.0           2021        Initial Version
#
# __________________________________________
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
    Appearance = driver.find_element_by_link_text("Appearence").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
         NoSuchElementException
    driver.implicitly_wait(10)
    Appearance_template = driver.find_element_by_css_selector('#doc-template').click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
         NoSuchElementException
    driver.implicitly_wait(10)
    Appearance_logotype = driver.find_element_by_css_selector("#doc-logotype").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
         NoSuchElementException
    driver.implicitly_wait(10)
    Catalog = driver.find_element_by_link_text("Catalog").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
         NoSuchElementException
    driver.implicitly_wait(10)
    Catalog_catalog = driver.find_element_by_css_selector("#doc-catalog.selected")
    Catalog_catalog.click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
         NoSuchElementException
    driver.implicitly_wait(10)
    Catalog_product_groups = driver.find_element_by_css_selector("#doc-product_groups").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Catalog_option_groups = driver.find_element_by_css_selector("#doc-option_groups").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Catalog_manufacturers = driver.find_element_by_css_selector("#doc-manufacturers").click()
    try:
        heading= driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Catalog_suppliers = driver.find_element_by_css_selector("#doc-suppliers").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Catalog_statuses = driver.find_element_by_css_selector("#doc-delivery_statuses").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Catalog_delivery_statuses = driver.find_element_by_css_selector("#doc-delivery_statuses").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Catalog_sold_out_statuses = driver.find_element_by_css_selector("#doc-sold_out_statuses").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Catalog_quantity_units = driver.find_element_by_css_selector("#doc-quantity_units").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    Catalog_csv = driver.find_element_by_css_selector("#doc-csv").click()
    driver.implicitly_wait(10)
    Countries = driver.find_element_by_link_text("Countries").click()
    driver.implicitly_wait(10)
    Customers = driver.find_element_by_link_text("Customers")
    Customers.click()
    driver.implicitly_wait(10)
    Customers_customers = driver.find_element_by_css_selector("#doc-customers").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Customers_csv = driver.find_element_by_css_selector("#doc-csv").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Customers_newsletter = driver.find_element_by_css_selector("#doc-newsletter").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    Geo_Zones  = driver.find_element_by_link_text("Geo Zones").click()
    driver.implicitly_wait(10)
    Languages = driver.find_element_by_link_text("Languages").click()
    driver.implicitly_wait(10)
    sections_Languages_languages  =driver.find_element_by_css_selector("#doc-languages").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Languages_storage_encoding = driver.find_element_by_css_selector("#doc-storage_encoding").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Modules = driver.find_element_by_link_text("Modules").click()
    driver.implicitly_wait(10)
    Modules_jobs = driver.find_element_by_css_selector("#doc-jobs").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Modules_customer = driver.find_element_by_css_selector("#doc-customer").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Modules_shipping = driver.find_element_by_css_selector("#doc-shipping").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Modules_payment = driver.find_element_by_css_selector("#doc-payment").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Modules_order_total = driver.find_element_by_css_selector("#doc-order_total").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Modules_order_success = driver.find_element_by_css_selector("#doc-order_success").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Modules_order_action = driver.find_element_by_css_selector("#doc-order_action").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Orders = driver.find_element_by_link_text("Orders").click()
    driver.implicitly_wait(10)
    Orders_orders = driver.find_element_by_css_selector("#doc-orders").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Orders_order_statuses = driver.find_element_by_css_selector("#doc-order_statuses").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Pages = driver.find_element_by_link_text("Pages").click()
    driver.implicitly_wait(10)
    Reports = driver.find_element_by_link_text("Reports").click()
    driver.implicitly_wait(10)
    Reports_monthly_sales = driver.find_element_by_css_selector("#doc-monthly_sales").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Reports_most_sold_products = driver.find_element_by_css_selector("#doc-most_sold_products").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Reports_most_shopping_customers = driver.find_element_by_css_selector("#doc-most_shopping_customers").click()
    driver.implicitly_wait(10)
    Settings = driver.find_element_by_link_text("Settings").click()
    driver.implicitly_wait(10)
    Settings_store_info = driver.find_element_by_css_selector("#doc-store_info").click()
    driver.implicitly_wait(10)
    Settings_defaults = driver.find_element_by_css_selector("#doc-defaults").click()
    driver.implicitly_wait(10)
    Settings_doc_general = driver.find_element_by_css_selector("#doc-general").click()
    driver.implicitly_wait(10)
    Settings_listings = driver.find_element_by_css_selector("#doc-listings").click()
    driver.implicitly_wait(10)
    Settings_images = driver.find_element_by_css_selector("#doc-images").click()
    driver.implicitly_wait(10)
    Settings_checkout = driver.find_element_by_css_selector("#doc-checkout").click()
    driver.implicitly_wait(10)
    Settings_advanced = driver.find_element_by_css_selector("#doc-advanced").click()
    driver.implicitly_wait(10)
    Settings_security  =driver.find_element_by_css_selector("#doc-security").click()
    Slides = driver.find_element_by_link_text("Slides").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Translations = driver.find_element_by_link_text("Translations").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Translations_search = driver.find_element_by_css_selector("#doc-search").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Translations_scan = driver.find_element_by_css_selector("#doc-scan").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    Translations_cs= driver.find_element_by_css_selector("#doc-csv").click()
    driver.implicitly_wait(10)
    Users = driver.find_element_by_link_text("Users").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    vQmods = driver.find_element_by_link_text("vQmods").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    driver.implicitly_wait(10)
    vQmods_vqmods = driver.find_element_by_css_selector("#doc-vqmods").click()
    try:
        heading = driver.find_element_by_tag_name('h1')
    except:
        NoSuchElementException
    WebDriverWait(driver, 5).until(EC.title_is("vQmods | My Store"))

