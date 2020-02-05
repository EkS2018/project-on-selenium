import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import time

@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        page = ProductPage(browser, link)
        page.open()
        page.find_and_click_button_1()
        page.solve_quiz_and_get_code()
        page.compare_name_and_price_of_goods()

def test_guest_should_see_login_link_on_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()


@pytest.mark.xfail(reason="this bug will bi fixed later")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = BasketPage(browser, link)
        page.open()
        page.find_and_click_button_2()
        page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = BasketPage(browser, link)
        page.open()
        page.should_not_be_success_message()


@pytest.mark.xfail(reason="this bug will be fixed later")
def test_message_disappeared_after_adding_product_to_basket(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = BasketPage(browser, link)
        page.open()
        page.find_and_click_button_2()
        time.sleep(1)
        page.should_not_be_success_message_2()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page.should_be_basket_empty()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page.should_be_basket_empty()
        

@pytest.mark.login
class TestUserAddToBasketFromProductPage():
        @pytest.fixture(scope="function", autouse=True)
        def setup(self, browser):
                email = str(time.time()) + "@fakemail.org"
                password = "222222121"
                link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
                self.page = LoginPage(browser, link)
                self.page.open()
                self.page.register_new_user(email, password)
                self.page.should_be_authorized_user()

        @pytest.mark.xfail(reason="this bug will be fixed later")        
        def test_user_cant_see_success_message_after_adding_product_to_basket(self, browser):
                link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
                page = BasketPage(browser, link)
                page.open()
                page.find_and_click_button_2()
                page.should_not_be_success_message()

        @pytest.mark.need_review
        def test_user_can_add_product_to_basket(self, browser):
                link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
                page = ProductPage(browser, link)
                page.open()
                page.find_and_click_button_1()
                page.compare_name_and_price_of_goods()
        
