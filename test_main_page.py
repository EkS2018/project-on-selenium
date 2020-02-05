import pytest
from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import time

def test_should_be_login_page(browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_url()
        page.should_be_login_form()
        page.should_be_register_form()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
        link = "http://selenium1py.pythonanywhere.com/ru/"
        page = BasketPage(browser, link)
        page.open()
        page.go_to_basket_page()
        page.should_be_basket_empty()
        
        
        
