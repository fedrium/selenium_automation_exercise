from pages.sign_up import LoginPage

def test_homepage(driver):
    signup_page = LoginPage(driver) #create class

    signup_page.to_signup_page() #click on signup/login button
    assert signup_page.wait_for_signup_header().is_displayed() #Verify 'New User Signup!' is visible

    signup_page.signup("abc123", "testuser69@gmail.com") #signup with these credentials
    assert signup_page.wait_for_account_info_header().is_displayed() #Verify that 'ENTER ACCOUNT INFORMATION' is visible

    #Keys in credentials for sign up
    signup_page.enter_account_information()
    signup_page.enter_address("John", "Doe", "Wayne Enterprise", "Night Street", "The Road", "United States", "Gotham", "Arkham", "11111", "0123456789")

    #Clicks the sign up button and Verify that 'ACCOUNT CREATED!' is visible
    signup_page.signup_button_click()
    assert signup_page.wait_for_account_created().is_displayed()

    signup_page.click_continue() #Click 'Continue' button
    assert signup_page.wait_for_logged_in().is_displayed()

    signup_page.delete_account() #Click 'Delete Account' button
    assert signup_page.wait_for_acc_deleted().is_displayed() #Verify that 'ACCOUNT DELETED!' is visible and click 'Continue' button
    signup_page.click_continue()

    

