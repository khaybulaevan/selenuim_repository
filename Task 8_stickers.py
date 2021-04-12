import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    wd = webdriver.Edge()
    request.addfinalizer(wd.quit)
    return wd

def test_sticker(driver):
    driver.get("http://localhost:8080/litecart/en/")
    driver.implicitly_wait(10)
    sticker_sum = 0
    duck_amount = driver.find_elements_by_css_selector("ul.listing-wrapper.products li")
    print("Общее количесво уток:"+str(len(duck_amount)))
    for duck in duck_amount:
        sticker = duck.find_elements_by_xpath(".//div[starts-with(@class,'sticker')]")
        print(len(sticker))
        sticker_sum = sticker_sum+len(sticker)
    assert len(duck_amount) == sticker_sum
