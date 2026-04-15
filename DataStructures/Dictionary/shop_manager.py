inventory = {
    "apple":  {"price": 1.2,  "stock": 50, "category": "fruit"},
    "banana": {"price": 0.5,  "stock": 3,  "category": "fruit"},
    "milk":   {"price": 2.0,  "stock": 20, "category": "dairy"},
    "cheese": {"price": 5.5,  "stock": 1,  "category": "dairy"},
    "bread":  {"price": 1.8,  "stock": 15, "category": "bakery"},
    "butter": {"price": 3.2,  "stock": 0,  "category": "dairy"},
}

# Step 1 — Warm up
for key, info in inventory.items():
    print(f"{key} - {info['price']} — in stock: {info['stock']}")

# Step 2 — Low stock alert
def low_stock(inventory, threshold):
    result = []
    for key, info in inventory.items():
        stock = info['stock']
        if stock <= threshold:
            result.append(key)
    return result

print(low_stock(inventory, 5))

#Step 3 — Category filter
def by_category(inventory, category):
    new_dict = {}
    for key, info in inventory.items():
        dict_category = info['category']
        if dict_category == category:
            new_dict[key] = info
    return new_dict

print(by_category(inventory, "dairy"))

#Step 4 — Restock
def restock(inventory, item, amount):
    if item in inventory: 
        info = inventory[item]
        old_stock = info['stock']
        info['stock'] += amount
        return f"{item} stock: {old_stock} -> {info['stock']}"
    return f"Warning: {item} not found"
        
print(restock(inventory, "milk", 10))
print(restock(inventory, "milk", 10))

#Step 5 - Total value
def total_value(inventory):
    total = 0 
    for key, info in inventory.items():
        total += info['stock'] * info['price']
    return total

print(total_value(inventory))

#Step 6 - Priciest category
def priciest_category(inventory):
    category_by_price = {}
    count = 0 # you should fix the count where ***
    for info in inventory.values():
        price_sum = info['price']
        if info['category'] not in category_by_price:
            category_by_price.update({info['category']: {"sum": info['price'], "count": count}}) # ***
        else:
            category_by_price.update({info['category']: info['price'] + price_sum})
    return category_by_price

print(priciest_category(inventory))
