dict1 = {'apple': 5, 'cherry': 2, 'banana': 4}
dict2 = {'orange': 3, 'banana': 1}

sorted_dict = dict(sorted(dict1.items()))
print("1. Sorted dictionary (by key):", sorted_dict)

merged_dict = dict1 | dict2
print("2. Merged dictionary:", merged_dict)

text = "hello"
frequency = {}
for char in text:
    frequency[char] = frequency.get(char, 0) + 1
print("3. Frequency Count of 'hello':", frequency)

setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

common_elements = setA.intersection(setB)
print("4. Common elements (Intersection):", common_elements)

unique_to_A = setA.difference(setB)
print("5. Unique to setA (Difference):", unique_to_A)

all_unique_elements = setA.symmetric_difference(setB)
print("6. All unique elements (Symmetric Difference):", all_unique_elements)