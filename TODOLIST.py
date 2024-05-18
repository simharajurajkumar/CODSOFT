import tkinter as tk
from tkinter import messagebox, simpledialog

class ToDoApp:

    def __init__(self, root):
        self.root = root
        self.root.title('To-Do List App')
        self.tasks = []
        self.widgets()

    def widgets(self):
        # Set a background color for the listbox
        self.listbox = tk.Listbox(self.root, width=50, height=15, bg='#f0f0f0', fg='blue')
        self.listbox.pack(pady=20)

        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=10)

        # Set a background color for the entry widget
        self.task_entry = tk.Entry(entry_frame, width=45, bg='#fff', fg='blue')
        self.task_entry.pack(side=tk.LEFT, padx=(0, 10))

        # Set a color for the 'Add Task' button
        add_button = tk.Button(entry_frame, text='Add Task', command=self.add_task, bg='#add8e6', fg='black')
        add_button.pack(side=tk.LEFT)

        # Set a color for the 'Update Selected' button
        self.update_button = tk.Button(self.root, text='Update Selected', state=tk.DISABLED, command=self.update_task, bg='#add8e6', fg='black')
        self.update_button.pack(side=tk.LEFT, padx=(20, 10))

        # Set a color for the 'Delete Selected' button
        delete_button = tk.Button(self.root, text='Delete Selected', command=self.delete_task, bg='#ff6961', fg='#fff')
        delete_button.pack(side=tk.LEFT)

        self.listbox.bind('<<ListboxSelect>>', self.enable_update_button)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning('Warning', 'Please enter a task.')

    def update_task(self):
        selected = self.listbox.curselection()
        if selected:
            task = self.listbox.get(selected)
            new_task = simpledialog.askstring('Update Task', 'Update the selected task:', initialvalue=task)
            if new_task:
                self.listbox.delete(selected)
                self.listbox.insert(selected, new_task)

    def delete_task(self):
        selected = self.listbox.curselection()
        if selected:
            self.listbox.delete(selected)

    def enable_update_button(self, event):
        if self.listbox.curselection():
            self.update_button['state'] = tk.NORMAL
        else:
            self.update_button['state'] = tk.DISABLED

if __name__ == '__main__':
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
