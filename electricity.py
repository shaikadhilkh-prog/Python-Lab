def calculate_electricity_bill():
    print("--- Electricity Bill Calculator ---")
    
    try:
        # Get input from the user
        user_input = input("Enter the number of units consumed: ")
        units = float(user_input)
        
        # Check for negative values
        if units < 0:
            raise ValueError("Units consumed cannot be negative.")
            
    except ValueError as e:
        # Catch non-numeric inputs and explicit negative value errors
        print(f"\n[Error] Invalid input: {e}")
        print("Please enter a valid, positive numerical value.")
        
    else:
        # This block executes ONLY if no exceptions were raised
        # Tiered pricing structure:
        # First 100 units: ₹4.50 per unit
        # Next 200 units (101-300): ₹6.00 per unit
        # Above 300 units: ₹8.50 per unit
        
        bill_amount = 0.0
        
        if units <= 100:
            bill_amount = units * 4.50
        elif units <= 300:
            bill_amount = (100 * 4.50) + ((units - 100) * 6.00)
        else:
            bill_amount = (100 * 4.50) + (200 * 6.00) + ((units - 300) * 8.50)
            
        print(f"\n--- Bill Summary ---")
        print(f"Units Consumed: {units:.2f}")
        print(f"Total Amount Due: ₹{bill_amount:.2f}")
        
    finally:
        # This block always executes, regardless of errors
        print("\nThank you for using the Electricity Bill Calculator system.")

# Run the program
if __name__ == "__main__":
    calculate_electricity_bill()
