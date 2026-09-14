user_input = input("Enter comma-separated numbers: ")
generated_list = [num.strip() for num in user_input.split(',') if num .strip()]
generated_tuple = tuple(generated_list)
print("List:", generated_list)
print("Tuple:", generated_tuple)
if generated_list:
    print("Total number of elements:", len(generated_list))
    print("First element:", generated_list[0])
    print("Last element:", generated_list[-1])
    print("List in reverse order:", generated_list[::-1])