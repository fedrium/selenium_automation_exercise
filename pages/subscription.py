from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Sub:
    SUBSCRIPTION_TEXT = (By.XPATH, "//h2[contains(., 'Subscription')]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[id='susbscribe_email']")
    EMAIL_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    SUCCESS_MESSAGE = (By.XPATH, "//div[contains(., 'You have been successfully subscribed!')]")
    CART_BUTTON = (By.CSS_SELECTOR, "a[href='/view_cart']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def go_to_website(self):
        self.driver.get("https://automationexercise.com")

    def verify_on_home(self):
        WebDriverWait(self.driver, 10).until(
            EC.title_is("Automation Exercise")
        )
        return True
    
    def verify_subscription_text(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUBSCRIPTION_TEXT)
        )
    
    def enter_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.EMAIL_SUBMIT_BUTTON).click()

    def verify_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        )
    
    def click_on_cart(self):
        self.driver.find_element(*self.CART_BUTTON).click()