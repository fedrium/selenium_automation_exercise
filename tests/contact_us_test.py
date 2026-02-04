from pages.contact_test_cases import Contact

def test_contact_us(driver):
    contact_us = Contact(driver) #create class

    contact_us.go_to_website()
    assert contact_us.verify_on_home()

    contact_us.navigate_to_contact_us()
    assert contact_us.verify_contact_us_header().is_displayed()

    contact_us.fill_contact_form("a", "static_test_user@gmail.com", "test", "Hello", "/home/cyu-xian/ae/test.txt")
    contact_us.click_submit_button()

    contact_us.click_ok()

    assert contact_us.verify_success_message().is_displayed()

    contact_us.go_to_home()
    assert contact_us.verify_on_home()

def test_test_cases(driver):
    contact_us = Contact(driver) #create class

    contact_us.go_to_website()
    assert contact_us.verify_on_home()

    contact_us.go_to_test_cases()
    assert contact_us.verify_test_case_page().is_displayed()
