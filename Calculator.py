import tkinter as tk
from tkinter import simpledialog, messagebox

class SimpleCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title('Simple Calculator')
        self.create_widgets()

    def create_widgets(self):
        # Set a background color for the calculator
        self.root.configure(bg='#e6e6fa')

        # Entry for the first number
        self.first_number_entry = tk.Entry(self.root, width=15, borderwidth=5, bg='#f8f8ff', fg='#333')
        self.first_number_entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Entry for the second number
        self.second_number_entry = tk.Entry(self.root, width=15, borderwidth=5, bg='#f8f8ff', fg='#333')
        self.second_number_entry.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Buttons for operations
        self.add_button = tk.Button(self.root, text='+', width=5, height=2, command=lambda: self.calculate('+'), bg='#98fb98', fg='#333')
        self.add_button.grid(row=2, column=0)

        self.subtract_button = tk.Button(self.root, text='-', width=5, height=2, command=lambda: self.calculate('-'), bg='#98fb98', fg='#333')
        self.subtract_button.grid(row=2, column=1)

        self.multiply_button = tk.Button(self.root, text='*', width=5, height=2, command=lambda: self.calculate('*'), bg='#98fb98', fg='#333')
        self.multiply_button.grid(row=3, column=0)

        self.divide_button = tk.Button(self.root, text='/', width=5, height=2, command=lambda: self.calculate('/'), bg='#98fb98', fg='#333')
        self.divide_button.grid(row=3, column=1)

    def calculate(self, operation):
        first_number = self.first_number_entry.get()
        second_number = self.second_number_entry.get()

        try:
            first_number = float(first_number)
            second_number = float(second_number)

            if operation == '+':
                result = first_number + second_number
            elif operation == '-':
                result = first_number - second_number
            elif operation == '*':
                result = first_number * second_number
            elif operation == '/':
                result = first_number / second_number

            messagebox.showinfo('Result', f'The result is: {result}')
        except ValueError:
            messagebox.showerror('Error', 'Please enter valid numbers.')
        except ZeroDivisionError:
            messagebox.showerror('Error', 'Cannot divide by zero.')

if __name__ == '__main__':
    root = tk.Tk()
    calculator = SimpleCalculator(root)
    root.mainloop()
