import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate a random password
def generate_password(length, complexity):
    char_sets = {
        'low': string.ascii_lowercase,
        'medium': string.ascii_letters,
        'high': string.ascii_letters + string.digits,
        'very_high': string.ascii_letters + string.digits + string.punctuation
    }
    
    if complexity not in char_sets:
        messagebox.showerror("Error", "Complexity level must be: low, medium, high, or very_high.")
        return ""
    
    characters = char_sets[complexity]
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main application window
class PasswordGeneratorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Password Generator')
        self.configure(bg='#282c34')  # Dark background for the window
        
        # Style configuration
        label_font = ('Helvetica', 10)
        entry_font = ('Helvetica', 12, 'bold')
        button_font = ('Helvetica', 12, 'bold')
        output_font = ('Helvetica', 12, 'bold')
        
        # Length
        tk.Label(self, text='Password Length:', bg='#282c34', fg='white', font=label_font).grid(row=0, column=0)
        self.length_entry = tk.Entry(self, font=entry_font)
        self.length_entry.grid(row=0, column=1)
        
        # Complexity
        tk.Label(self, text='Password Complexity:', bg='#282c34', fg='white', font=label_font).grid(row=1, column=0)
        self.complexity_entry = tk.Entry(self, font=entry_font)
        self.complexity_entry.grid(row=1, column=1)
        
        # Generate button
        generate_button = tk.Button(self, text='Generate Password', command=self.on_generate, bg='aqua', fg='black', font=button_font)
        generate_button.grid(row=2, column=0, columnspan=2)
        
        # Password display
        self.password_display = tk.Entry(self, state='readonly', font=output_font)
        self.password_display.grid(row=3, column=0, columnspan=2)
    
    def on_generate(self):
        # Get user input
        length = self.length_entry.get()
        complexity = self.complexity_entry.get().lower()
        try:
            length = int(length)
            # Generate and display the password
            password = generate_password(length, complexity)
            self.password_display.config(state='normal', fg='green')  # Green text for password
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, password)
            self.password_display.config(state='readonly')
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number for length.")

# Run the application
if __name__ == '__main__':
    app = PasswordGeneratorApp()
    app.mainloop()
