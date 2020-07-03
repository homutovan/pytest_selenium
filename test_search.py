from ya_search import Search_helper
from conftest import browser

def test_yandex_search_field(browser):
    yandex_main_page = Search_helper(browser)
    yandex_main_page.go_to_site()
    assert yandex_main_page.check_search_field()
    
def test_yandex_suggest_popup(browser):
    yandex_main_page = Search_helper(browser)
    yandex_main_page.enter_word('Тензор')
    assert yandex_main_page.check_suggest_popup
    
def test_yandex_serp_list(browser):
    yandex_main_page = Search_helper(browser)
    yandex_main_page.send_enter()
    assert yandex_main_page.check_serp_list()
    
def test_yandex_link_tensor_ru(browser):
    yandex_main_page = Search_helper(browser)
    assert len(yandex_main_page.check_link('tensor.ru', 5)) == 5
    
def test_yandex_link_tensor(browser):
    yandex_main_page = Search_helper(browser)
    assert len(yandex_main_page.check_link('tensor', 5)) == 5
