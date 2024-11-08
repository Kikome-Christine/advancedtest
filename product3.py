import matplotlib.pyplot as plt
from product import DiscountedProduct   

# Visualization function
def visualize_price_change(product):
    original_price = product.get_price()
    discounted_price = product.final_price()

    prices = [original_price, discounted_price]
    labels = ['Original Price', 'Discounted Price']

    plt.bar(labels, prices, color=['blue', 'orange'])
    plt.ylabel('Price (UGX)')  # Changed to UGX for consistency
    plt.title(f'Price Change for {product.get_name()}')  # Use get_name() for consistency

    plt.ylim(0, max(prices) + 20)
    
    for i in range(len(prices)):
        plt.text(i, prices[i] + 1, f'UGX{prices[i]:.2f}', ha='center')  # Format for UGX with two decimal places

    plt.show()

# Example usage with visualization
product = DiscountedProduct("Laptop", 147, 47)  # Created instance of DiscountedProduct
visualize_price_change(product)


 