from pages.sign_up import LoginPage

def test_login_correct(driver):
    signup_page = LoginPage(driver) #create class

    signup_page.to_signup_page() #go to singup page
    signup_page.signup("abc123", "test_user_67@gmail.com")
    signup_page.enter_account_information() #enter credentials
    signup_page.enter_address()
    signup_page.signup_button_click()
    assert signup_page.wait_for_account_created().is_displayed()
    
    signup_page.click_continue()
    signup_page.logout_click()
    assert signup_page.wait_for_login_header().is_displayed()

    signup_page.login_account("test_user_67@gmail.com", "oooo0000") #Enters correct email & password and click login
    assert signup_page.wait_for_logged_in().is_displayed()

    signup_page.delete_account() #Click 'Delete Account' button
    assert signup_page.wait_for_acc_deleted().is_displayed() #Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    signup_page.click_continue()
    
def test_login_incorrect(driver):
    signup_page = LoginPage(driver) #create class

    signup_page.to_signup_page() #go to singup page
    assert signup_page.wait_for_login_header().is_displayed()

    signup_page.login_account("static_test_user_1@gmail.com", "incorrectpassword") #Enters correct email & password and click login
    assert signup_page.wait_for_login_error().is_displayed()

def test_logout_user_(driver):
    signup_page = LoginPage(driver)

    signup_page.to_signup_page() #go to singup page
    assert signup_page.wait_for_login_header().is_displayed()

    signup_page.login_account("static_test_user_1@gmail.com", "oooo0000")
    assert signup_page.wait_for_logged_in().is_displayed()

    signup_page.logout_click()
    assert signup_page.wait_for_login_header().is_displayed()

def test_existing_user(driver):
    signup_page = LoginPage(driver)

    signup_page.to_signup_page() #go to singup page
    assert signup_page.wait_for_signup_header().is_displayed()

    signup_page.signup("abc123", "static_test_user_1@gmail.com")

    assert signup_page.verify_exist_error().is_displayed()



