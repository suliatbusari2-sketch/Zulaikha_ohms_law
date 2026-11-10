"""
CTE123 Python Mini Project: Ohm's Law and Power Calculator
Author: Oladimeji Ismail olamilekan
Extra feature: Calculation History
"""

def get_positive_number(prompt):
    """Get a positive number and handle invalid input."""
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            print("Please enter a number greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def calculate_voltage():
    """Calculate voltage using V = I x R."""
    current = get_positive_number("Enter current in amperes (A): ")
    resistance = get_positive_number("Enter resistance in ohms: ")
    return f"Voltage = {current * resistance:.2f} V"


def calculate_current():
    """Calculate current using I = V / R."""
    voltage = get_positive_number("Enter voltage in volts (V): ")
    resistance = get_positive_number("Enter resistance in ohms: ")
    return f"Current = {voltage / resistance:.2f} A"


def calculate_resistance():
    """Calculate resistance using R = V / I."""
    voltage = get_positive_number("Enter voltage in volts (V): ")
    current = get_positive_number("Enter current in amperes (A): ")
    return f"Resistance = {voltage / current:.2f} ohms"


def calculate_power():
    """Calculate power using P = V x I."""
    voltage = get_positive_number("Enter voltage in volts (V): ")
    current = get_positive_number("Enter current in amperes (A): ")
    return f"Power = {voltage * current:.2f} W"


def show_menu():
    """Display the calculator menu."""
    print("\n===== OHM'S LAW AND POWER CALCULATOR =====")
    print("1. Calculate Voltage (V = I x R)")
    print("2. Calculate Current (I = V / R)")
    print("3. Calculate Resistance (R = V / I)")
    print("4. Calculate Power (P = V x I)")
    print("5. View Calculation History")
    print("6. Exit")


def main():
    # This list stores successful results for the extra history feature.
    calculation_history = []

    # Keep displaying the menu until the user chooses to exit.
    while True:
        show_menu()
        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            result = calculate_voltage()
            print("\n" + result)
            calculation_history.append(result)
        elif choice == "2":
            result = calculate_current()
            print("\n" + result)
            calculation_history.append(result)
        elif choice == "3":
            result = calculate_resistance()
            print("\n" + result)
            calculation_history.append(result)
        elif choice == "4":
            result = calculate_power()
            print("\n" + result)
            calculation_history.append(result)
        elif choice == "5":
            # Display calculations saved during this program session.
            if len(calculation_history) == 0:
                print("\nNo calculation has been made yet.")
            else:
                print("\n===== CALCULATION HISTORY =====")
                for number, item in enumerate(calculation_history, start=1):
                    print(f"{number}. {item}")
        elif choice == "6":
            print("\nThank you for using the calculator. Goodbye!")
            break
        else:
            print("\nInvalid menu choice. Please select a number from 1 to 6.")


# Run the main function when this file is executed.
if __name__ == "__main__":
    main()
