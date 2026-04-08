def apply_discount(price, discount):
    if not isinstance(price, (int, float)):
        return"Error: The price should be a number"
    elif not isinstance(discount, (int, float)):
        return"Error: The discount should be a number"
    elif price <= 0:
        return"Error:The price should be greater than 0"
    elif discount <= 0 or discount >= 101:
        return "Error: The discount should be between 0 and 100"
    else:
        final_price =  price - (price/100 * discount)
        return final_price

print(apply_discount(100, 100))
