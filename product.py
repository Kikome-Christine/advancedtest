class Product:
    def __init__(self, name, price):
        self.name = name
        self.__price = price  

    def get_name(self):
        return self.name  # Fixed attribute name
    
    def get_price(self):
        return self.__price

    def set_price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = price

    def apply_discount(self, discount_percentage):
        discount_amount = (discount_percentage / 100) * self.__price
        return self.__price - discount_amount


class DiscountedProduct(Product):
    def __init__(self, name, price, discount_percentage):
        super().__init__(name, price)   
        self.discount_percentage = discount_percentage

    def get_discount_percentage(self):
        return self.discount_percentage  # Added getter for discount percentage

    def final_price(self):
        return self.apply_discount(self.discount_percentage)


# Example usage with student number last two digits as input
student_number_last_two_digits = 47   
product_name = "Laptop"
product_price = 100 + student_number_last_two_digits   

# Create a product instance
product = DiscountedProduct(product_name, product_price, student_number_last_two_digits)   
print(f"Product Name: {product.get_name()}")
print(f"Original Price: UGX{product.get_price()}")
print(f"Discount Percentage: {product.get_discount_percentage()}%")
print(f"Final Price after discount: UGX{product.final_price()}")
