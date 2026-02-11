from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Checkout:
    ADDRESS_BOX = (By.ID, "address_delivery")
    MESSAGE = (By.CSS_SELECTOR, "textarea[class='form-control']")
    PLACE_ORDER_BUTTON = (By.CSS_SELECTOR, "a[href='/payment']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_address_line(self):
        address_box = self.driver.find_element(*self.ADDRESS_BOX)

        lines = [
            li.text.strip()
            for li in address_box.find_elements(By.TAG_NAME, "li")
            if li.text.strip() and "address_title" not in li.get_attribute("class")
        ]

        return lines

    
    def send_message(self, message):
        self.driver.find_element(*self.MESSAGE).send_keys(message)
        self.driver.find_element(*self.PLACE_ORDER_BUTTON).click()

    #Payment
    NAME_ON_CARD = (By.CSS_SELECTOR, "input[data-qa='name-on-card']")
    CARD_NUMBER = (By.CSS_SELECTOR, "input[data-qa='card-number']")
    CVC = (By.CSS_SELECTOR, "input[data-qa='cvc']")
    EXPIRY_MONTH = (By.CSS_SELECTOR, "input[data-qa='expiry-month']")
    EXPIRY_YEAR = (By.CSS_SELECTOR, "input[data-qa='expiry-year']")
    PAY_BUTTON = (By.CSS_SELECTOR, "button[data-qa='pay-button']")
    SUCCESS_MESSAGE = (By.XPATH, "//h2[contains(., 'Order Placed!')]")

    def input_payment_method(self, name, card_number, cvc, expiry_month, expiry_year):
        self.driver.find_element(*self.NAME_ON_CARD).send_keys(name)
        self.driver.find_element(*self.CARD_NUMBER).send_keys(card_number)
        self.driver.find_element(*self.CVC).send_keys(cvc)
        self.driver.find_element(*self.EXPIRY_MONTH).send_keys(expiry_month)
        self.driver.find_element(*self.EXPIRY_YEAR).send_keys(expiry_year)

    def click_pay_button(self):
        self.driver.find_element(*self.PAY_BUTTON).click()

    def verify_payment_success(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SUCCESS_MESSAGE)
        )