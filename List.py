fruits = ["apple", "banana", "cherry"]
print("1.Original list:", fruits)

has_banana = "banana" in fruits
banana_index = fruits.index("banana")
print(f"2. Does the list contain 'banana'? {has_banana} (at index {banana_index})")

fruits[1] = "blueberry"
print("3. After updating index 1:", fruits)

a_fruits = [item for item in fruits if item.startswith("a")]
print("4. Filtered list (starts with 'a'):", a_fruits)

fruits.append("orange")
print("5. After appending 'orange':", fruits)

fruits.remove("cherry")
print("6. After removing 'cherry':", fruits)

fruits.sort()
print("7. After sorting:", fruits)
