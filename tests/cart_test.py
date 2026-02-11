from pages.product import Product
from pages.cart import Cart
from pages.product import Product_quantity
from pages.cart import RemoveFromCart

def test_add_products_in_cart(driver):
    product = Product(driver)

    product.go_to_website()
    assert product.verify_on_home()

    product.click_on_products_button() #Click 'Products' button

    cart = Cart(driver)

    cart.add_to_cart(0) #Hover over first product and click 'Add to cart'
    cart.click_continue_shopping() #Click 'Continue Shopping' button

    cart.add_to_cart(1) #Hover over second product and click 'Add to cart'
    cart.click_view_cart() #Click 'View Cart' button

    cart.verify_cart_items(0, "Rs. 500", "1", "Rs. 500") #Verify both products are added to Cart
    cart.verify_cart_items(1, "Rs. 400", "1", "Rs. 400") #Verify their prices, quantity and total price

def test_product_quantity(driver):
    product = Product(driver)

    product.go_to_website()
    assert product.verify_on_home()

    product.enter_product_details() #Click 'View Product' for any product on home page
    assert product.verify_product_details() #Verify product detail is opened

    quantity = Product_quantity(driver)
    quantity.increase_quantity("4") #Increase quantity to 4
    quantity.add_to_cart_and_view_cart() #Click 'Add to cart' button

    cart = Cart(driver)
    cart.verify_cart_items(0, "Rs. 500", "4", "Rs. 2000") #Verify that product is displayed in cart page with exact quantity

def test_remove_from_cart(driver):
    product = Product(driver)

    product.go_to_website()
    assert product.verify_on_home()

    cart = Cart(driver)

    cart.add_to_cart(0) #Add products to cart
    cart.click_continue_shopping()

    cart.add_to_cart(1)
    cart.click_continue_shopping()

    cart.click_cart_from_home() #Click 'Cart' button
    assert cart.verify_on_cart_page().is_displayed() #Verify that cart page is displayed
 
    remove = RemoveFromCart(driver) #Click 'X' button corresponding to particular product
    remove.delete_product("2")
    remove.delete_product("1")

    assert remove.verify_cart_is_empty().is_displayed() #Verify that product is removed from the cart
 