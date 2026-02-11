from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    #Go to signup page and input username and email
    NAME_INPUT = (By.CSS_SELECTOR, "[data-qa='signup-name']")
    EMAIL_INPUT = (By.CSS_SELECTOR, '[data-qa="signup-email"]')
    SIGNUP_BUTTON = (By.CSS_SELECTOR, "[data-qa='signup-button']")
    SIGNUP_HEADER = (By.XPATH, "//h2[text()='New User Signup!']")
    ACCOUNT_INFO_HEADER = (By.XPATH, "//h2[.//b[text()='Enter Account Information']]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def to_signup_page(self): #go to signup page#
        self.driver.get("https://automationexercise.com")
        login_button = self.driver.find_element(By.CSS_SELECTOR, ("a[href='/login']"))
        login_button.click()

    def wait_for_signup_header(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SIGNUP_HEADER)
        )

    def wait_for_account_info_header(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ACCOUNT_INFO_HEADER)
    )

    def signup(self, username, email): #inputs new email and username#
        self.wait_for_signup_header()
        self.driver.find_element(*self.NAME_INPUT).send_keys(username)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.SIGNUP_BUTTON).click()

    #Entering Account information
    TITLE_MR = (By.ID, "id_gender1")
    TITLE_MRS = (By.ID, "id_gender2")
    PASSWORD = (By.CSS_SELECTOR, "input[type='password']")
    DAY = (By.ID, "days")
    MONTH = (By.ID, "months")
    YEAR = (By.ID, "years")
    NEWSLETTER = (By.ID, "newsletter")
    OPTIN = (By.ID, "optin")

    def select_title(self, title): #click on the title
        if title == "Mr":
            self.driver.find_element(*self.TITLE_MR).click()
        else:
            self.driver.find_element(*self.TITLE_MRS).click()

    def select_dob(self, day, month, year):
        Select(self.driver.find_element(*self.DAY)).select_by_visible_text(day)
        Select(self.driver.find_element(*self.MONTH)).select_by_visible_text(month)
        Select(self.driver.find_element(*self.YEAR)).select_by_visible_text(year)


    def enter_account_information(self):
        self.select_title("Mr")
        self.driver.find_element(*self.PASSWORD).send_keys("oooo0000")
        self.select_dob("2", "December", "2003")
        self.driver.find_element(*self.NEWSLETTER).click()
        self.driver.find_element(*self.OPTIN).click()

    #Entering Address
    FIRST_NAME = (By.CSS_SELECTOR, ("input[data-qa='first_name']"))
    LAST_NAME = (By.CSS_SELECTOR, ("input[data-qa='last_name']"))
    COMPANY = (By.CSS_SELECTOR, ("input[data-qa='company']"))
    ADDRESS = (By.CSS_SELECTOR, ("input[data-qa='address']"))
    ADDRESS2 = (By.CSS_SELECTOR, ("input[data-qa='address2']"))
    COUNTRY = (By.CSS_SELECTOR, ("select[data-qa='country']"))
    STATE = (By.CSS_SELECTOR, ("input[data-qa='state']"))
    CITY = (By.CSS_SELECTOR, ("input[data-qa='city']"))
    ZIPCODE = (By.CSS_SELECTOR, ("input[data-qa='zipcode']"))
    MOBILE_NUMBER = (By.CSS_SELECTOR, ("input[data-qa='mobile_number']"))
    CREATE_BUTTON = (By.CSS_SELECTOR, ("button[data-qa='create-account']"))
    ACCOUNT_CREATED = (By.XPATH, ("//h2[.//b[text()= 'Account Created!']]"))

    def enter_address(self, first_name, last_name, company, address, address2, country, state, city, zipcode, mobile_number):
        self.driver.find_element(*self.FIRST_NAME).send_keys(first_name)
        self.driver.find_element(*self.LAST_NAME).send_keys(last_name)
        self.driver.find_element(*self.COMPANY).send_keys(company)
        self.driver.find_element(*self.ADDRESS).send_keys(address)
        self.driver.find_element(*self.ADDRESS2).send_keys(address2)
        Select(self.driver.find_element(*self.COUNTRY)).select_by_visible_text(country)
        self.driver.find_element(*self.STATE).send_keys(state)
        self.driver.find_element(*self.CITY).send_keys(city)
        self.driver.find_element(*self.ZIPCODE).send_keys(zipcode)
        self.driver.find_element(*self.MOBILE_NUMBER).send_keys(mobile_number)

    def signup_button_click(self):
        self.driver.find_element(*self.CREATE_BUTTON).click()

    def wait_for_account_created(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ACCOUNT_CREATED)
        )
    
    #Verify and Delete account
    CON_BUTTON = (By.CSS_SELECTOR, "a[data-qa=continue-button]")
    LOGGED_IN = (By.XPATH, "//a[contains(., 'Logged in as')]")
    DELETE = (By.CSS_SELECTOR, "a[href='/delete_account']")
    ACC_DELETED = (By.XPATH, "//h2[.//b[text()='Account Deleted!']]")

    def wait_for_logged_in(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LOGGED_IN)
        )

    def click_continue(self):
        self.driver.find_element(*self.CON_BUTTON).click()

    def delete_account(self):
        self.driver.find_element(*self.DELETE).click()

    def wait_for_acc_deleted(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.ACC_DELETED)
        )
    
    #Login Page
    LOGOUT = (By.CSS_SELECTOR, "a[href='/logout']")
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Login to your account']")
    LOGIN_EMAIL = (By.CSS_SELECTOR, "input[data-qa='login-email']")
    LOGIN_PASSWORD = (By.CSS_SELECTOR, "input[data-qa='login-password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[data-qa='login-button']")
    LOGIN_ERROR = (By.XPATH, "//p[contains(., 'Your email or password is incorrect!')]")
    EMAIL_EXIST_ERROR = (By.XPATH, "//p[contains(., 'Email Address already exist!')]")

    def logout_click(self):
        logout = self.wait.until(
        EC.element_to_be_clickable(self.LOGOUT)
        )
        logout.click()

    def wait_for_login_header(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LOGIN_HEADER)
        )
    
    def login_account(self, email, password):
        self.driver.find_element(*self.LOGIN_EMAIL).send_keys(email)
        self.driver.find_element(*self.LOGIN_PASSWORD).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def wait_for_login_error(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.LOGIN_ERROR)
        )
    
    def verify_exist_error(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.EMAIL_EXIST_ERROR)
        )
