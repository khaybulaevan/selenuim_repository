import pytest
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome(chrome_options=options)
    request.addfinalizer(wd.quit)
    return wd


def find_and_fill(driver, element_name, value):
    driver.find_element_by_name(element_name).click()
    driver.find_element_by_name(element_name).clear()
    driver.find_element_by_name(element_name).send_keys(value)

def test_all_sections(driver):
    driver.get("http://localhost/litecart/admin/")
    find_and_fill(driver, element_name="username", value="admin")
    find_and_fill(driver, element_name="password", value="admin")
    driver.find_element_by_name('login').click()
    driver.implicitly_wait(10)
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    driver.find_element_by_css_selector("tr.row td:nth-child(7)").click()
    all_links = driver.find_elements_by_css_selector("#content form table [target=_blank]")
    print("\nОбщее количество ссылок: " + str(len(all_links)))
    # -----------------Окна------------------
    # Текущее окно
    main_window = driver.current_window_handle
    print("main_window: " + str(main_window))
    # Все открытые окна
    old_windows = driver.window_handles
    print("old_window: " + str(old_windows))
    for i in range(len(all_links)):
        #print("i = " + str(i))
        all_links[i].click()
        wait = WebDriverWait(driver, 10)
        wait.until(EC.new_window_is_opened(old_windows))
        # Все окна после открытия ссылки
        new_windows = driver.window_handles
        print("new_windows" + str(new_windows))
        # Окно открытой ссылки
        new_window = list(set(new_windows).difference(old_windows))
        print("new_window" + str(new_window))
        driver.switch_to_window(new_window[0])
        driver.close()
        driver.switch_to_window(main_window)




