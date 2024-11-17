#Kimora Lee
#M2Pro Instructions
#2024
#Use of decision structures, functions and module import to complete assignments
def getParkingHours():
    """
    Prompts the user for the number of hours parked and returns this value.
    """
    while True:
        try:
            hours = float(input("Enter the number of hours parked: "))
            if hours < 0:
                print("Number of hours cannot be negative. Please try again.")
            else:
                return hours
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calcParkingFee(hours):
    """
    Calculates the parking fee based on the number of hours parked.
    - $2.50/hour
    - Minimum fee is $6.00
    - Maximum fee is $20.00
    """
    rate_per_hour = 2.50
    minimum_fee = 6.00
    maximum_fee = 20.00
    
    # Calculate the fee based on hours parked
    fee = hours * rate_per_hour
    
    # Ensure the fee is within the allowed range
    if fee < minimum_fee:
        fee = minimum_fee
    elif fee > maximum_fee:
        fee = maximum_fee
    
    return fee

def display_menu():
    """
    Displays the menu options to the user.
    """
    print("\nMenu---------------")
    print("1) Calculate parking fee")
    print("2) Exit")
    print("--------------------") 
    

def main():
    """
    Main function to run the menu-driven parking fee program.
    """
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1 or 2): "))
            if choice == 1:
                hours = getParkingHours()
                fee = calcParkingFee(hours)
                print(f"The parking fee for {hours:.2f} hours is ${fee:.2f}.")
            elif choice == 2:
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Run the program
if __name__ == "__main__":
    main()
