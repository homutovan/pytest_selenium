from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class Base_page:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://yandex.ru'

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator))
    
    def find_elements_by_link(self, element, link):
        try:
            return element.find_element_by_partial_link_text(link)
        except NoSuchElementException:
            return False
    
    def check_element(self, locator, time=10):
        try:
            return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            return False
            
    def go_to_site(self):
        return self.driver.get(self.base_url)
    
    def get_current_url(self):
        return self.driver.current_url
    
    def get_handles(self):
        return self.driver.window_handles
    
    def swich_tab(self, tab_id):
        return self.driver.switch_to.window(tab_id)