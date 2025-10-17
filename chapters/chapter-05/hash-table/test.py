#Testing all examples from the chapter Hash Tables
prices = {}

prices["apple"] = 1.25
prices["banana"] = 0.80
prices["grapes"] = 2.50

print("Price of apple:", prices["apple"])

if "banana" in prices:
    print("Banana is in the table!")

prices["apple"] = 1.30
print("Updated price of apple:", prices["apple"])

del prices["grapes"]
print("After deleting grapes:", prices)

for fruit, price in prices.items():
    print(f"{fruit}: ${price}")

if "apple" in prices:
    print("Apple already exists — avoid duplicates!")

key = "banana"
print(f"Hash value for '{key}':", hash(key))
print(f"Hash value for '{key}' again:", hash(key))  
