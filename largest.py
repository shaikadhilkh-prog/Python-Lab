a = float(input("\nEnter the first number: "))
b = float(input("\nEnter the second number: "))
c = float(input("\nEnter the third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print(f"The largest number is: {largest}")