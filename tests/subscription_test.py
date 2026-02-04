from pages.subscription import Sub

def test_subscription(driver):
    sub = Sub(driver)

    sub.go_to_website()
    assert sub.verify_on_home()

    sub.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    sub.enter_email("testmail@gmail.com")
    assert sub.verify_success_message().is_displayed()

def test_subscription_cart(driver):
    sub = Sub(driver)

    sub.go_to_website()
    assert sub.verify_on_home()

    sub.click_on_cart()

    sub.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    sub.enter_email("testmail@gmail.com")
    assert sub.verify_success_message().is_displayed()