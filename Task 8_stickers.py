import pytest
from selenium import webdriver

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
    duck_amount = driver.find_elements_by_css_selector("ul.listing-wrapper.products li")
    print("Общее количесво товара:"+str(len(duck_amount)))
    for duck in duck_amount:
        sticker = duck.find_elements_by_xpath(".//div[starts-with(@class,'sticker')]")
        #print(len(sticker))
        assert len(sticker) == 1
        print("У товара один стикер")