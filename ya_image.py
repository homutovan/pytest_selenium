from base_app import Base_page
from selenium.webdriver.common.by import By

time = 5

class Yandex_image_locators:
    LOCATOR_YANDEX_IMAGE_CARD = (By.CSS_SELECTOR, '.cl-card-teaser')
    LOCATOR_YANDEX_IMAGE = (By.CLASS_NAME, 'image__image')
    LOCATOR_YANDEX_NEXT = (By.CLASS_NAME, 'cl-viewer-navigate__item_right')
    LOCATOR_YANDEX_PREV = (By.CLASS_NAME, 'cl-viewer-navigate__item_left')
    
class Image_helper(Base_page):
  
    def click_image_card(self):
        return self.find_element(Yandex_image_locators.LOCATOR_YANDEX_IMAGE_CARD, time=time).click()
    
    def check_image(self):
        return self.find_element(Yandex_image_locators.LOCATOR_YANDEX_IMAGE, time=time).is_displayed()
    
    def show_next_image(self):
        return self.find_element(Yandex_image_locators.LOCATOR_YANDEX_NEXT, time=time).click()
    
    def show_prev_image(self):
        return self.find_element(Yandex_image_locators.LOCATOR_YANDEX_PREV, time=time).click()