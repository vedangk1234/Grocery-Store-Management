class GroceryStore:
    def __init__(self):
        self.inventory = []

    def add_product(self, product):
        self.inventory.append(product)

    def sell_product(self):
        if not self.inventory:
            print("No products available.")
        else:
            product = self.inventory.pop(0)
            print(f"Sold product {product}.")

grocery_store = GroceryStore()

# Add products to inventory
grocery_store.add_product("Apples")
grocery_store.add_product("Bananas")
grocery_store.add_product("Oranges")
grocery_store.add_product("Pears")

# Sell products
grocery_store.sell_product() # Sold product Apples.
grocery_store.sell_product() # Sold product Bananas.
grocery_store.sell_product() # Sold product Oranges.
grocery_store.sell_product() # Sold product Pears.

# Try to sell a product when there are none left
grocery_store.sell_product() # No products available.
