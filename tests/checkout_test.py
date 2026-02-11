from pages.cart import Cart
from pages.product import Product
from pages.sign_up import LoginPage
from pages.checkout import Checkout
import time

def test_place_order_register_while_checkout(driver):
    cart = Cart(driver)
    product = Product(driver)

    product.go_to_website()
    assert product.verify_on_home()

    cart.add_to_cart(0)
    cart.click_view_cart()

    assert cart.verify_on_cart_page().is_displayed()
    cart.click_checkout_button()
    cart.click_register_login_button()

    sign_up = LoginPage(driver)
    sign_up.signup("testy", "test_user_6767@gmail.com")
    sign_up.enter_account_information()
    sign_up.enter_address("John", "Doe", "Wayne Enterprise", "Night Street", "The Road", "United States", "Gotham", "Arkham", "11111", "0123456789")

    sign_up.signup_button_click()
    assert sign_up.wait_for_account_created().is_displayed()

    sign_up.click_continue() #Click 'Continue' button
    assert sign_up.wait_for_logged_in().is_displayed() #Verify ' Logged in as username' at top

    cart.click_cart_from_home()
    cart.click_checkout_button()

    expected_lines = [
        "Mr. John Doe",
        "Wayne Enterprise",
        "Night Street",
        "The Road",
        "Arkham Gotham 11111",
        "United States",
        "0123456789"
    ]

    checkout = Checkout(driver)
    result = checkout.verify_address_line()
    assert result == expected_lines

    checkout.send_message("Im buying this")
    checkout.input_payment_method("Bruce Wayne", "1111222233334444", "420", "02", "2026")
    checkout.click_pay_button()

    assert checkout.verify_payment_success().is_displayed()

    sign_up.delete_account()
    assert sign_up.wait_for_acc_deleted().is_displayed()

def test_place_order_register_before_checkout(driver):
    sign_up = LoginPage(driver) #create class

    sign_up.to_signup_page() #click on signup/login button
    assert sign_up.wait_for_signup_header().is_displayed() #Verify 'New User Signup!' is visible

    sign_up.signup("abc123", "test_user_6767@gmail.com") #signup with these credentials
    assert sign_up.wait_for_account_info_header().is_displayed() #Verify that 'ENTER ACCOUNT INFORMATION' is visible

    #Keys in credentials for sign up
    sign_up.enter_account_information()
    sign_up.enter_address("John", "Doe", "Wayne Enterprise", "Night Street", "The Road", "United States", "Gotham", "Arkham", "11111", "0123456789")

    #Clicks the sign up button and Verify that 'ACCOUNT CREATED!' is visible
    sign_up.signup_button_click()
    assert sign_up.wait_for_account_created().is_displayed()

    sign_up.click_continue() #Click 'Continue' button
    assert sign_up.wait_for_logged_in().is_displayed()

    cart = Cart(driver)
    cart.add_to_cart(0)
    cart.click_view_cart()

    assert cart.verify_on_cart_page().is_displayed()
    cart.click_checkout_button()

    expected_lines = [
        "Mr. John Doe",
        "Wayne Enterprise",
        "Night Street",
        "The Road",
        "Arkham Gotham 11111",
        "United States",
        "0123456789"
    ]

    checkout = Checkout(driver)
    result = checkout.verify_address_line()
    assert result == expected_lines

    checkout.send_message("Im buying this")
    checkout.input_payment_method("Bruce Wayne", "1111222233334444", "420", "02", "2026")
    checkout.click_pay_button()

    assert checkout.verify_payment_success().is_displayed()

    sign_up.delete_account()
    assert sign_up.wait_for_acc_deleted().is_displayed()