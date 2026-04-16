inventory = {
    "apple":  {"price": 1.2,  "stock": 50, "category": "fruit"},
    "banana": {"price": 0.5,  "stock": 3,  "category": "fruit"},
    "milk":   {"price": 2.0,  "stock": 20, "category": "dairy"},
    "cheese": {"price": 5.5,  "stock": 1,  "category": "dairy"},
    "bread":  {"price": 1.8,  "stock": 15, "category": "bakery"},
    "butter": {"price": 3.2,  "stock": 0,  "category": "dairy"},
}

# Step 1 — Warm up
for key, data in inventory.items():
    print(f"{key} - {data['price']} — in stock: {data['stock']}")

# Step 2 — Low stock alert
def low_stock(inventory, threshold):
    result = []
    for key, data in inventory.items():
        stock = data['stock']
        if stock <= threshold:
            result.append(key)
    return result

print(low_stock(inventory, 5))

#Step 3 — Category filter
def by_category(inventory, category):
    new_dict = {}
    for key, data in inventory.items():
        dict_category = data['category']
        if dict_category == category:
            new_dict[key] = data
    return new_dict

print(by_category(inventory, "dairy"))

#Step 4 — Restock
def restock(inventory, item, amount):
    if item in inventory: 
        data = inventory[item]
        old_stock = data['stock']
        data['stock'] += amount
        return f"{item} stock: {old_stock} -> {data['stock']}"
    return f"Warning: {item} not found"
        
print(restock(inventory, "milk", 10))
print(restock(inventory, "milk", 10))

#Step 5 - Total value
def total_value(inventory):
    total = 0 
    for key, data in inventory.items():
        total += data['stock'] * data['price']
    return total

print(total_value(inventory))

#Step 6 - Priciest category
def priciest_category(inventory):
    
    category_by_price = {}
    best_avg = 0
    best_category = ''
    
    for data in inventory.values():
        category = data['category']
        price = data['price']
        if category not in category_by_price:
            category_by_price.update({category: {"sum": price, "count": 1}})
        else:
            category_by_price[category]["sum"] += price
            category_by_price[category]["count"] += 1
        
    for category, data in category_by_price.items():
        average = data['sum'] / data['count']
        if average > best_avg:
            best_avg = average
            best_category = category
    
    return best_category


print(priciest_category(inventory))
