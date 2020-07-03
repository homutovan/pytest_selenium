from ya_search import Search_helper
from ya_image import Image_helper
from conftest import browser
import pytest

def test_yandex_image_link(browser):
    yandex_main_page = Search_helper(browser)
    yandex_main_page.go_to_site()
    assert 'Картинки' in yandex_main_page.check_navigation_bar()
    
def test_transition_to_image(browser):
    yandex_main_page = Search_helper(browser)
    yandex_main_page.click_image()
    assert yandex_main_page.get_current_url() == 'https://yandex.ru/images/'
    
def test_displayed_image(browser):
    yandex_img_page = Image_helper(browser)
    yandex_img_page.click_image_card()
    assert yandex_img_page.check_image()
    
def test_show_next(browser):
    yandex_img_page = Image_helper(browser)
    pytest.shared = yandex_img_page.get_current_url()
    yandex_img_page.show_next_image()
    assert pytest.shared != yandex_img_page.get_current_url()
    
def test_show_prew(browser):
    yandex_img_page = Image_helper(browser)
    yandex_img_page.show_prev_image()
    assert pytest.shared == yandex_img_page.get_current_url()