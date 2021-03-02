import time


def test_should_be_button_add_item_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    browser.get(link)
    time.sleep(5)
    button = browser.find_element_by_class_name("btn-add-to-basket")
    assert button.is_displayed() is True, "Нет кнопки 'Добавить в корзину'"
