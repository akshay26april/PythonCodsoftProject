import tkinter as tk

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = add(num1, num2)
        elif operation == '-':
            result = subtract(num1, num2)
        elif operation == '*':
            result = multiply(num1, num2)
        elif operation == '/':
            result = divide(num1, num2)
        else:
            result_label.config(text="Invalid operation. Please choose +, -, *, or /.")
            return

        result_label.config(text="Result: " + str(result))

    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numerical values.")

# GUI setup
window = tk.Tk()
window.title("Simple Calculator")

# Entry fields
entry_num1 = tk.Entry(window)
entry_num1.pack()

entry_num2 = tk.Entry(window)
entry_num2.pack()

# Operation dropdown
operation_var = tk.StringVar()
operation_var.set('+')  # default operation
operation_menu = tk.OptionMenu(window, operation_var, '+', '-', '*', '/')
operation_menu.pack()

# Button to trigger calculation
calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.pack()

# Result label
result_label = tk.Label(window, text="")
result_label.pack()

# Run the GUI
window.mainloop()
