# Step 1: Define the calculate_discount function
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)  # Calculate the discount amount
        final_price = price - discount_amount  # Subtract the discount from the original price
        return final_price
    else:
        return price  # If the discount is less than 20%, return the original price

# Step 2: Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Step 3: Calculate and print the final price
final_price = calculate_discount(original_price, discount_percent)
print(f"The final price after applying the discount is: {final_price}")
