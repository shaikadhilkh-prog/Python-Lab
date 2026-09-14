# 1. CREATE: Initialize a small, simple data collection using lists
inventory = [
    [101, "Laptop", 1200],
    [102, "Mouse", 25],
    [103, "Keyboard", 75]
]

print("=== MINI INVENTORY MANAGER ===")

# --- USER INPUT DEMOS FOR EVERY FEATURE ---

# A. CREATE (Add a new item via user input)
print("\n[1. CREATE] Add a new product:")
new_id = int(input("Enter unique ID (e.g., 104): "))
new_name = input("Enter product name: ")
new_price = int(input("Enter price ($): "))
inventory.append([new_id, new_name, new_price]) # Built-in list method

# B. SEARCH (Find an item using list comprehension)
print("\n[2. SEARCH] Find a product:")
search_id = int(input("Enter ID to look up: "))
found = [item for item in inventory if item[0] == search_id]
print(f"Result: {found[0] if found else 'Not Found'}")

# C. UPDATE (Modify an existing item dynamically)
print("\n[3. UPDATE] Edit a product's price:")
update_id = int(input("Enter ID to update: "))
for item in inventory:
    if item[0] == update_id:
        item[2] = int(input(f"Enter new price for {item[1]}: $"))
        print(f"Updated successfully: {item}")

# D. FILTER (Extract a targeted sub-list using list comprehension)
print("\n[4. FILTER] Filter by budget:")
max_budget = int(input("Show items cheaper than ($): "))
affordable_items = [item for item in inventory if item[2] < max_budget]
print(f"Filtered Results: {affordable_items}")

# E. MANIPULATE (Sort using built-in methods and delete via list comprehension)
print("\n[5. MANIPULATE] Deleting an item and sorting:")
delete_id = int(input("Enter ID to delete permanently: "))
inventory = [item for item in inventory if item[0] != delete_id] # Deleting/filtering out

# Built-in sorting manipulation based on the price index [2]
inventory.sort(key=lambda x: x[2]) 

# Final Output Display
print("\n=== FINAL MANIPULATED INVENTORY (Sorted by Price) ===")
for item in inventory:
    print(f"ID: {item[0]} | Name: {item[1]} | Price: ${item[2]}")