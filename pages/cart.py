from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

class Cart:
    PRODUCT = (By.CSS_SELECTOR, ".features_items .product-image-wrapper")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".product-overlay .add-to-cart")
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, "//button[contains(., 'Continue Shopping')]")
    VIEW_CART = (By.CSS_SELECTOR, "#cartModal a[href='/view_cart']")
    HOME_VIEW_CART = (By.CSS_SELECTOR, "a[href='/view_cart']")
    ITEMS = (By.CSS_SELECTOR, "tbody tr")
    PRICE = (By.CSS_SELECTOR, "td.cart_price p")
    QUANTITY = (By.CSS_SELECTOR, "td.cart_quantity button")
    TOTAL_PRICE = (By.CSS_SELECTOR, "td.cart_total p")
    CART_PAGE_HEADER = (By.XPATH, "//li[contains(., 'Shopping Cart')]")
    CHECKOUT_BUTTON = (By.CSS_SELECTOR, ".btn.btn-default.check_out")
    REGISTER_CHECKOUT_BUTTON = (By.CSS_SELECTOR, "#checkoutModal a[href='/login']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    def click_cart_from_home(self):
        self.driver.find_element(*self.HOME_VIEW_CART).click()

    def add_to_cart(self, index):
        products = self.wait.until(
            EC.visibility_of_all_elements_located(self.PRODUCT)
        )
        product = products[index]

        #Scrolls to the item
        self.driver.execute_script(
        "arguments[0].scrollIntoView({block: 'center'});",
            product
        )

        #Hovers on the item
        self.actions.move_to_element(product).perform()

        add_to_cart = self.wait.until(
            EC.element_to_be_clickable(
                product.find_element(*self.ADD_TO_CART_BUTTON)
            )
        )
        add_to_cart.click()

    def click_continue_shopping(self):
        self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_SHOPPING_BUTTON)
        )
        self.driver.find_element(*self.CONTINUE_SHOPPING_BUTTON).click()
    
    def click_view_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.VIEW_CART)
        ).click()

    def verify_cart_items(self, index, price, quantity, tp):
        self.wait.until(
            EC.visibility_of_element_located(self.ITEMS)
        )
        rows = self.driver.find_elements(*self.ITEMS)

        items = rows[index]

        item_price = items.find_element(*self.PRICE).text
        item_quantity = items.find_element(*self.QUANTITY).text
        item_tp = items.find_element(*self.TOTAL_PRICE).text

        assert price == item_price
        assert quantity == item_quantity
        assert tp == item_tp

    def verify_on_cart_page(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.CART_PAGE_HEADER)
        )
    
    def click_checkout_button(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def click_register_login_button(self):
        self.driver.find_element(*self.REGISTER_CHECKOUT_BUTTON).click()

class RemoveFromCart:
    CART_EMPTY_MESSAGE = (By.XPATH, "//b[contains(., 'Cart is empty!')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def delete_product(self, product_id):
        selector = f'a.cart_quantity_delete[data-product-id="{product_id}"]'
        btn = self.driver.find_element(By.CSS_SELECTOR, selector)
        btn.click()

    def verify_cart_is_empty(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.CART_EMPTY_MESSAGE)
        )