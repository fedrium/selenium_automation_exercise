from pages.side_bar import SideBar, Brands
from pages.product import Product

def test_categories(driver):
    sidebar = SideBar(driver)

    sidebar.go_to_website()
    assert sidebar.verify_on_home()

    sidebar.verify_categories_visible()
    sidebar.click_on_women()
    sidebar.click_on_women_sub()
    assert sidebar.verify_women_category().is_displayed()

    sidebar.click_on_men()
    sidebar.click_on_men_sub()
    assert sidebar.verify_men_category().is_displayed()

def test_brands(driver):
    product = Product(driver)

    product.go_to_website()
    assert product.verify_on_home()

    product.click_on_products_button()
    assert product.verify_on_products_page().is_displayed()
    
    brands = Brands(driver)
    assert brands.verify_brands().is_displayed()

    brands.click_on_brands("Polo")
    assert brands.verify_on_Polo().is_displayed()
    assert product.check_for_products() > 0

    brands.click_on_brands("H&M")
    assert brands.verify_on_HM().is_displayed()
    assert product.check_for_products() > 0
