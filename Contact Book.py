import tkinter as tk
from tkinter import messagebox

# Contact class to hold contact details
class Contact:

    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

# Main application class
class ContactBookApp:

    def __init__(self, root):
        self.root = root
        self.contacts = {}
        self.initialize_ui()
    
    def initialize_ui(self):
        self.root.title("Contact Book")
        self.root.configure(bg='light grey')  # Set the background color of the window

        # Add contact form with colorful labels and entry fields
        tk.Label(self.root, text="Name:", bg='light grey', fg='blue').grid(row=0, column=0)
        self.name_entry = tk.Entry(self.root, bg='white', fg='black')
        self.name_entry.grid(row=0, column=1)

        tk.Label(self.root, text="Phone:", bg='light grey', fg='blue').grid(row=1, column=0)
        self.phone_entry = tk.Entry(self.root, bg='white', fg='black')
        self.phone_entry.grid(row=1, column=1)

        tk.Label(self.root, text="Email:", bg='light grey', fg='blue').grid(row=2, column=0)
        self.email_entry = tk.Entry(self.root, bg='white', fg='black')
        self.email_entry.grid(row=2, column=1)

        tk.Label(self.root, text="Address:", bg='light grey', fg='blue').grid(row=3, column=0)
        self.address_entry = tk.Entry(self.root, bg='white', fg='black')
        self.address_entry.grid(row=3, column=1)

        # Add contact button with a colorful design
        tk.Button(self.root, text="Add Contact", bg='green', fg='white', command=self.add_contact).grid(row=4, columnspan=2)

        # Contact list with a colorful scrollbar
        self.contact_listbox = tk.Listbox(self.root, bg='white', fg='black')
        self.contact_listbox.grid(row=5, columnspan=2)
        scrollbar = tk.Scrollbar(self.root, orient='vertical', command=self.contact_listbox.yview)
        scrollbar.grid(row=5, column=2, sticky='ns')
        self.contact_listbox.configure(yscrollcommand=scrollbar.set)

        # Update and delete buttons with a colorful design
        tk.Button(self.root, text="Update Contact", bg='orange', fg='white', command=self.update_contact).grid(row=6, column=0)
        tk.Button(self.root, text="Delete Contact", bg='red', fg='white', command=self.delete_contact).grid(row=6, column=1)

    
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:  # Basic validation
            contact = Contact(name, phone, email, address)
            self.contacts[name] = contact
            self.contact_listbox.insert(tk.END, name)
            messagebox.showinfo("Success", "Contact added successfully!")
        else:
            messagebox.showerror("Error", "Name and phone number are required.")

    def update_contact(self):
        try:
            selected = self.contact_listbox.curselection()[0]
            name = self.contact_listbox.get(selected)
            contact = self.contacts[name]

            # Update contact details
            contact.name = self.name_entry.get()
            contact.phone = self.phone_entry.get()
            contact.email = self.email_entry.get()
            contact.address = self.address_entry.get()

            messagebox.showinfo("Success", "Contact updated successfully!")
        except IndexError:
            messagebox.showerror("Error", "Please select a contact to update.")

    def delete_contact(self):
        try:
            selected = self.contact_listbox.curselection()[0]
            name = self.contact_listbox.get(selected)
            del self.contacts[name]
            self.contact_listbox.delete(selected)
            messagebox.showinfo("Success", "Contact deleted successfully!")
        except IndexError:
            messagebox.showerror("Error", "Please select a contact to delete.")

# Create the main window and pass it to the ContactBookApp
root = tk.Tk()
app = ContactBookApp(root)
root.mainloop()
