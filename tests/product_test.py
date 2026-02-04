from pages.product import Product
from pages.product import Search

def test_all_porducts(driver):
    product = Product(driver)

    product.go_to_website()
    assert product.verify_on_home()

    product.click_on_products_button()
    assert product.verify_on_products_page().is_displayed()

    assert product.check_for_products() > 0

    product.enter_product_details()
    assert product.verify_product_details()

def normalize(text: str) -> str:
    return text.replace(" ", "").replace("-", "").lower()

def test_product_search(driver):
    product = Product(driver)

    product.go_to_website()
    assert product.verify_on_home()

    product.click_on_products_button()
    assert product.verify_on_products_page().is_displayed()

    search = Search(driver)
    search.click_on_search_bar("Tshirt")

    assert search.wait_for_searched_item().is_displayed()    

    query_result = search.query_searched_items("Tshirt")
    for result in query_result:
        assert ('tshirt') in normalize(result), \
            f"'{result}' is not related to tshirt"