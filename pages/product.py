from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Product:
    PRODUCTS_BUTTON = (By.CSS_SELECTOR, "a[href='/products']")
    ALL_PRODUCTS_PAGE = (By.XPATH, "//h2[contains(., 'All Products')]")
    PRODUCTS = (By.CSS_SELECTOR, ".features_items .product-image-wrapper")
    PRODUCT_DETAILS_BUTTON = (By.CSS_SELECTOR, "a[href='/product_details/1']")
    PRODUCT_NAME = (By.XPATH, "//div[@class='product-information']//h2")
    CATEGORY = (By.XPATH, "//div[@class='product-information']//p[contains(., 'Category')]")
    PRICE = (By.XPATH, "//span[contains(., 'Rs. ')]")
    AVAILABILITY = (By.XPATH, "//b[contains(., 'Availability')]")
    CONDITION = (By.XPATH, "//b[contains(., 'Condition')]")
    BRAND = (By.XPATH, "//b[contains(., 'Brand')]")

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
    
    def click_on_products_button(self):
        self.driver.find_element(*self.PRODUCTS_BUTTON).click()
    
    def verify_on_products_page(self):
        return self.wait.until(EC.visibility_of_element_located(self.ALL_PRODUCTS_PAGE))
    
    #check if there are products
    def check_for_products(self):
        products = self.driver.find_elements(*self.PRODUCTS)
        return len(products)
    
    #clicks the first product detail
    def enter_product_details(self):
        self.driver.find_element(*self.PRODUCT_DETAILS_BUTTON).click()

    #Checks for the product details
    def verify_product_details(self):
        self.wait.until(EC.visibility_of_element_located(self.PRODUCT_NAME))
        self.wait.until(EC.visibility_of_element_located(self.CATEGORY))
        self.wait.until(EC.visibility_of_element_located(self.PRICE))
        self.wait.until(EC.visibility_of_element_located(self.AVAILABILITY))
        self.wait.until(EC.visibility_of_element_located(self.CONDITION))
        self.wait.until(EC.visibility_of_element_located(self.BRAND))
        return True

class Search:
    SEARCH_BAR = (By.ID, "search_product")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[id='submit_search']")
    SERACHED_ITEMS_HEADER = (By.XPATH, "//h2[contains(., 'Searched Products')]")
    PRODUCT_TITLES = (By.CSS_SELECTOR,".single-products .productinfo p")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_on_search_bar(self, product_name):
        self.driver.find_element(*self.SEARCH_BAR).send_keys(product_name)
        self.driver.find_element(*self.SEARCH_BUTTON).click()

    def wait_for_searched_item(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.SERACHED_ITEMS_HEADER)
        )
    
    #Grabs all queried items and return
    def query_searched_items(self, product_name):
        products = self.wait.until(
            EC.visibility_of_all_elements_located(self.PRODUCT_TITLES)
        )

        return [el.text for el in products]
    
class Product_quantity:
    QUANTITY = (By.CSS_SELECTOR, "input[id='quantity']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn.btn-default.cart")
    VIEW_CART = (By.CSS_SELECTOR, "a[href='/view_cart']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def increase_quantity(self, amount):
        self.driver.find_element(*self.QUANTITY).clear()
        self.driver.find_element(*self.QUANTITY).send_keys(amount)

    def add_to_cart_and_view_cart(self):
        self.driver.find_element(*self.ADD_TO_CART_BUTTON).click()
        time.sleep(0.5)
        self.wait.until(
            EC.element_to_be_clickable(self.VIEW_CART)
        )
        self.driver.find_element(*self.VIEW_CART).click()
