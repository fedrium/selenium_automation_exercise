from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SideBar:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    CATEGORY_TITLE = (By.XPATH, "//h2[text()='Category']")
    WOMEN_CATEGORY = (By.CSS_SELECTOR, "a[href='#Women']")
    MEN_CATEGORY = (By.CSS_SELECTOR, "a[href='#Men']")
    LEFT_SIDEBAR = (By.CSS_SELECTOR, ".left-sidebar")
    WOMEN_TOP = (By.CSS_SELECTOR, "a[href='/category_products/2']")
    WOMEN_PRODUCTS_TITLE = (By.XPATH, "//h2[text()='Women - Tops Products']")
    MEN_JEANS = (By.CSS_SELECTOR, "a[href='/category_products/6']")
    MEN_PRODUCTS_TITLE = (By.XPATH, "//h2[text()='Men - Jeans Products']")

    def go_to_website(self):
        self.driver.get("https://automationexercise.com")

    def verify_on_home(self):
        WebDriverWait(self.driver, 10).until(
            EC.title_is("Automation Exercise")
        )
        return True

    def verify_categories_visible(self):
        # Wait until sidebar is visible
        self.wait.until(EC.visibility_of_element_located(self.LEFT_SIDEBAR))

        # Assertions
        assert self.driver.find_element(*self.CATEGORY_TITLE).is_displayed(), \
            "Category title is not visible"

        assert self.driver.find_element(*self.WOMEN_CATEGORY).is_displayed(), \
            "Women category is not visible"

        assert self.driver.find_element(*self.MEN_CATEGORY).is_displayed(), \
            "Men category is not visible"
        
    def click_on_women(self):
        self.driver.find_element(*self.WOMEN_CATEGORY).click()

    def click_on_women_sub(self):
        self.wait.until(
            EC.visibility_of_element_located(self.WOMEN_TOP)
        )
        self.driver.find_element(*self.WOMEN_TOP).click()

    def verify_women_category(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.WOMEN_PRODUCTS_TITLE)
        )
    
    def click_on_men(self):
        self.driver.find_element(*self.MEN_CATEGORY).click()

    def click_on_men_sub(self):
        self.wait.until(
            EC.visibility_of_element_located(self.MEN_JEANS)
        )
        self.driver.find_element(*self.MEN_JEANS).click()

    def verify_men_category(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.MEN_PRODUCTS_TITLE)
        )
    
class Brands:

    BRANDS = (By.XPATH, "//h2[text()='Brands']")
    POLO_HEADER = (By.XPATH, "//h2[text()='Brand - Polo Products']")
    HnM_HEADER = (By.XPATH, "//h2[text()='Brand - H&M Products']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def verify_brands(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.BRANDS)
        )
    
    def click_on_brands(self, brands):
        brand_link = f"a[href='/brand_products/{brands}']"
        self.driver.find_element(By.CSS_SELECTOR, brand_link).click()

    def verify_on_Polo(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.POLO_HEADER)
        )
    
    def verify_on_HM(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.HnM_HEADER)
        )
    
