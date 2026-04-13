inventory = {
    "apple":  {"price": 1.2,  "stock": 50, "category": "fruit"},
    "banana": {"price": 0.5,  "stock": 3,  "category": "fruit"},
    "milk":   {"price": 2.0,  "stock": 20, "category": "dairy"},
    "cheese": {"price": 5.5,  "stock": 1,  "category": "dairy"},
    "bread":  {"price": 1.8,  "stock": 15, "category": "bakery"},
    "butter": {"price": 3.2,  "stock": 0,  "category": "dairy"},
}

for key_1, value_1 in inventory.items():
    print(f"{key_1} - {value_1['price']} - in stock: {value_1['stock']}")