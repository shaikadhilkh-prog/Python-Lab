# Helper to convert user string input like "apple:5, banana:2" into a proper dictionary
def input_dictionary(prompt):
    print(prompt)
    user_str = input("Format (key:value, key:value): ")
    result_dict = {}
    if user_str.strip():
        # Split by comma to separate pairs
        pairs = user_str.split(",")
        for pair in pairs:
            if ":" in pair:
                key, val = pair.split(":", 1)
                # Strip spaces and convert numeric values if possible
                key = key.strip()
                val = val.strip()
                try:
                    val = float(val) if '.' in val else int(val)
                except ValueError:
                    pass # Keep as string if it's not a number
                result_dict[key] = val
    return result_dict

# Helper to convert user string input like "1, 2, 3" or "a, b, c" into a set
def input_set(prompt):
    user_str = input(f"{prompt} (separated by commas): ")
    if not user_str.strip():
        return set()
    # Clean up whitespace from each element
    elements = [item.strip() for item in user_str.split(",")]
    return set(elements)


# ==========================================
# 1. DICTIONARY OPERATIONS (Merge & Sort)
# ==========================================
print("=== 1. DICTIONARY OPERATIONS ===")
dict1 = input_dictionary("Enter elements for Dictionary 1:")
dict2 = input_dictionary("Enter elements for Dictionary 2:")

# A. Merging
merged_dict = dict1 | dict2
print(f"\nMerged Dictionary: {merged_dict}")

# B. Sorting
if merged_dict:
    sorted_by_keys = dict(sorted(merged_dict.items()))
    print(f"Sorted by Keys:    {sorted_by_keys}")
    
    # Attempt sorting by values (works best if all values are of comparable types)
    try:
        sorted_by_values = dict(sorted(merged_dict.items(), key=lambda item: item[1]))
        print(f"Sorted by Values:  {sorted_by_values}")
    except TypeError:
        print("Could not sort by values: Mixed data types present.")


# ==========================================
# 2. FREQUENCY COUNTING
# ==========================================
print("\n=== 2. FREQUENCY COUNTING ===")
list_input = input("Enter items to count frequency (separated by commas): ")
text_list = [item.strip() for item in list_input.split(",") if item.strip()]

frequency_dict = {}
for item in text_list:
    frequency_dict[item] = frequency_dict.get(item, 0) + 1

print(f"Frequency Count: {frequency_dict}")


# ==========================================
# 3. SET OPERATIONS
# ==========================================
print("\n=== 3. SET OPERATIONS ===")
set_A = input_set("Enter Set A elements")
set_B = input_set("Enter Set B elements")

print(f"\nSet A: {set_A}")
print(f"Set B: {set_B}")

# A. Merging Sets (Union)
print(f"Merged Sets (Union): {set_A.union(set_B)}")

# B. Common Elements (Intersection)
print(f"Common Elements (Intersection): {set_A.intersection(set_B)}")

# C. Unique Elements (Difference & Symmetric Difference)
print(f"Unique to Set A: {set_A.difference(set_B)}")
print(f"Unique to either set: {set_A.symmetric_difference(set_B)}")