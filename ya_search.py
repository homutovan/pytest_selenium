from base_app import Base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

time = 5

class Yandex_seacrh_locators:
    LOCATOR_YANDEX_SEARCH_FIELD = (By.ID, 'text')
    LOCATOR_YANDEX_NAVIGATION_BAR = (By.CLASS_NAME, 'home-tabs3__link')
    LOCATOR_YANDEX_SUGGEST_POPUP = (By.CLASS_NAME, 'mini-suggest__popup_visible')
    LOCATOR_YANDEX_SERP_LIST = (By.CSS_SELECTOR, '.serp-list.serp-list_left_yes')
    LOCATOR_YANDEX_SERP_ITEM = (By.CLASS_NAME, 'serp-item')
    LOCATOR_YANDEX_IMAGE_LINK = (By.CSS_SELECTOR, 'a[data-id="images"]')
    
def check_transition(decor_foo):
    def wrapped(self, *args, **kwargs):
        old_handles = self.get_handles()
        
        result = decor_foo(self, *args, **kwargs)
        
        new_handles = self.get_handles()
        
        if (len(new_handles) > len(old_handles)):
            self.swich_tab(new_handles[-1])
            
        return result
    return wrapped
    
class Search_helper(Base_page):
    
    def check_search_field(self):
        return self.find_element(Yandex_seacrh_locators.LOCATOR_YANDEX_SEARCH_FIELD)

    def enter_word(self, word):
        search_field = self.find_element(Yandex_seacrh_locators.LOCATOR_YANDEX_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field
    
    def check_suggest_popup(self):
        return self.check_element(Yandex_seacrh_locators.LOCATOR_YANDEX_SUGGEST_POPUP, time=time)
    
    def check_serp_list(self):
        return self.check_element(Yandex_seacrh_locators.LOCATOR_YANDEX_SERP_LIST, time=time)
    
    def send_enter(self):
        return self.check_search_field().send_keys(Keys.ENTER)

    def check_navigation_bar(self):
        all_list = self.find_elements(Yandex_seacrh_locators.LOCATOR_YANDEX_NAVIGATION_BAR, time=time)
        return [elem.text for elem in all_list if len(elem.text) > 0]
    
    def check_link(self, link, slice):
        elem_list = self.find_elements(Yandex_seacrh_locators.LOCATOR_YANDEX_SERP_ITEM, time=time)[:slice]
        return [elem for elem in elem_list if self.find_elements_by_link(elem, link)]
    
    def check_serp_items(self):
        return self.find_elements(Yandex_seacrh_locators.LOCATOR_YANDEX_SERP_ITEM, time=time)
    
    @check_transition
    def click_image(self):
        return self.find_element(Yandex_seacrh_locators.LOCATOR_YANDEX_IMAGE_LINK, time=time).click()