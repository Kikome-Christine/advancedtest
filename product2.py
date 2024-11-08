from product import DiscountedProduct
from product import Product

# 20% discount
def test_discount_application():
    product = DiscountedProduct("Test Product", 100, 20)  
    assert product.final_price() == 80.0, "Discount application failed!"

def test_price_setting():
    product = Product("Test Product", 100)
    product.set_price(150)
    assert product.get_price() == 150, "Price setting failed!"

# Running regression tests
test_discount_application()
test_price_setting()
print("All regression tests passed!")