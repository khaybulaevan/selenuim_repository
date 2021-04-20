import pytest
from selenium import webdriver
import  time

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(chrome_options=options)
    request.addfinalizer(wd.quit)
    return wd


def test_sticker(driver):
    driver.get("http://localhost:8080/litecart/en/")
    driver.implicitly_wait(10)
    home_page_products = driver.find_elements_by_css_selector("#box-campaigns ul.listing-wrapper.products li")
    num_of_product = []
    link_of_product_page = []
    product_name = []
    product_price = []
    product_price_discount = []

    product_price_style_text = []
    product_price_style_size = []
    product_price_discount_style_weihgt = []
    product_price_discount_style_size = []
    i = 1
    for product in home_page_products:
        num_of_product.append(i)
        link_of_product_page.append(product.find_element_by_css_selector('a.link').get_attribute("href"))
        product_name.append(product.find_element_by_css_selector('div.name').text)
        product_price.append(product.find_element_by_css_selector('div.price-wrapper s').text)
        product_price_discount.append(product.find_element_by_css_selector("div.price-wrapper strong").text)
        # Стили на главной странице
        product_price_style_text.append(product.find_element_by_css_selector("s.regular-price").value_of_css_property('text-decoration'))
        product_price_style_size.append(product.find_element_by_css_selector("s.regular-price").value_of_css_property('font-size'))
        product_price_discount_style_weihgt.append(product.find_element_by_css_selector("strong.campaign-price").get_attribute("tagName"))
        product_price_discount_style_size.append(product.find_element_by_css_selector("strong.campaign-price").value_of_css_property("font-size"))
        time.sleep(1)
        print("\nProduct " + str(i))
        print(product_name)
        print(product_price)
        print(product_price_discount)
        print(product_price_style_text)
        print(product_price_style_size)
        print(product_price_discount_style_size)
        print(product_price_discount_style_weihgt)
        i += i
    print(link_of_product_page)


    for j in range(len(num_of_product)):
        # Переход по ссылке товара
        driver.get(link_of_product_page[j])
        product_page_name = driver.find_element_by_css_selector("h1.title").get_attribute("textContent")
        product_page_price = driver.find_element_by_css_selector('s.regular-price').get_attribute("textContent")
        product_page_price_discount = driver.find_element_by_css_selector('strong.campaign-price').get_attribute("textContent")

        # Стили на странице товара
        product_page_price_style_text = driver.find_element_by_css_selector("s.regular-price").value_of_css_property('text-decoration')
        product_page_price_style_size = driver.find_element_by_css_selector("s.regular-price").value_of_css_property('font-size')
        product_page_price_discount_style_weihgt = driver.find_element_by_css_selector("strong.campaign-price").get_attribute('tagName')
        product_page_price_discount_style_size = driver.find_element_by_css_selector("strong.campaign-price").value_of_css_property("font-size")
        #
        print("Product from product page")
        print(product_page_name)
        print(product_page_price)
        print(product_page_price_discount)
        print(product_page_price_style_text)
        print(product_page_price_style_size)
        print(product_page_price_discount_style_size)
        print(product_page_price_discount_style_weihgt)

        assert product_name[j] == product_page_name
        assert product_price[j] == product_page_price
        assert product_price_discount_style_weihgt[j] == product_page_price_discount_style_weihgt
        assert product_price_style_size[j] == product_page_price_style_size
        assert product_price_discount_style_size[j] == product_page_price_discount_style_size
        assert product_price_discount[j] == product_page_price_discount
        assert product_price_style_text[j] == product_page_price_style_text

