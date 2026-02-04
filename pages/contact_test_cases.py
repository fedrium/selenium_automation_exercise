from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Contact:
    HOME_BUTTON = (By.XPATH, "//a[text()=' Home']")
    CONTACT_US_BUTTON = (By.CSS_SELECTOR, ("a[href='/contact_us']"))
    NAME = (By.CSS_SELECTOR, "input[data-qa='name']")
    EMAIL = (By.CSS_SELECTOR, "input[data-qa='email']")
    SUBJECT = (By.CSS_SELECTOR, "input[data-qa='subject']")
    MESSAGE = (By.CSS_SELECTOR, "textarea[data-qa='message']")
    INPUT = (By.CSS_SELECTOR, "input[type='file']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "input[data-qa='submit-button']")
    CONTACT_US_HEADER = (By.XPATH, "//h2[contains(., 'Get In Touch')]")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(., 'Success! Your details have been submitted successfully.')]")
    HOME_BUTTON_SUCCESS = (By.CSS_SELECTOR, "a[href='/']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_website(self):
        self.driver.get("https://automationexercise.com")

    def go_to_home(self):
        self.driver.find_element(*self.HOME_BUTTON_SUCCESS).click()

    def verify_on_home(self):
        WebDriverWait(self.driver, 10).until(
            EC.title_is("Automation Exercise")
        )
        return True
    
    def navigate_to_contact_us(self):
        self.driver.find_element(*self.CONTACT_US_BUTTON).click()

    def fill_contact_form(self, name, email, subject, message, file_path):
        self.driver.find_element(*self.NAME).send_keys(name)
        self.driver.find_element(*self.EMAIL).send_keys(email)
        self.driver.find_element(*self.SUBJECT).send_keys(subject)
        self.driver.find_element(*self.MESSAGE).send_keys(message)
        self.driver.find_element(*self.INPUT).send_keys(file_path)

    def click_submit_button(self):
        self.driver.find_element(*self.SUBMIT_BUTTON).click()

    def click_ok(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def verify_contact_us_header(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.CONTACT_US_HEADER)
        )
    
    def verify_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        )
    
    TEST_CASES_PAGE = (By.CSS_SELECTOR, "a[href='/test_cases']")
    TEST_CASE_TEST = (By.XPATH, "//b[contains(., 'Test Cases')]")

    def go_to_test_cases(self):
        self.driver.find_element(*self.TEST_CASES_PAGE).click()

    def verify_test_case_page(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.TEST_CASE_TEST)
        )    
