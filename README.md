# Ohm's Law and Power Calculator

## What it does
This Python program calculates voltage, current, resistance and electrical power using Ohm's Law. The user chooses what to calculate, enters the known values, and receives an answer with the correct unit. The program repeats its menu until the user chooses to exit.

## How to run it
1. Install Python 3.
2. Save the Python code as `ohms_law.py`.
3. Open a terminal or command prompt in the folder containing the file.
4. Run:

```bash
python ohms_law.py
```

You can also run the file using a Python IDE or an Android app such as Pydroid 3.

## Sample output

```text
===== OHM'S LAW AND POWER CALCULATOR =====
1. Calculate Voltage (V = I x R)
2. Calculate Current (I = V / R)
3. Calculate Resistance (R = V / I)
4. Calculate Power (P = V x I)
5. View Calculation History
6. Exit
Choose an option (1-6): 1
Enter current in amperes (A): 2
Enter resistance in ohms: 5

Voltage = 10.00 V

Choose an option (1-6): 4
Enter voltage in volts (V): 12
Enter current in amperes (A): 3

Power = 36.00 W

Choose an option (1-6): 5

===== CALCULATION HISTORY =====
1. Voltage = 10.00 V
2. Power = 36.00 W

Choose an option (1-6): 6
Thank you for using the calculator. Goodbye!
```

## My own twist
I added a **Calculation History** feature. It stores every successful calculation in a Python list and allows the user to view previous results during the current session. This makes it easier to review earlier answers without entering the values again.

## What I learned
I practised creating Python functions, using a `while` loop, making decisions with `if/elif/else`, converting user input with `float()`, handling invalid input with `try/except`, and storing results in a list. I also applied the formulas of Ohm's Law and electrical power.

## Author
**Oladimeji Ismail olamilekan**  
ND1 Mechatronics Engineering, YabaTech
