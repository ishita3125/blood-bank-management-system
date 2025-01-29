import sqlite3
import tkinter as tk
from tkinter import messagebox

# Database Initialization
def init_db():
    conn = sqlite3.connect("blood_bank.db")
    c = conn.cursor()
    
    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS donors (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT,
                 age INTEGER,
                 blood_type TEXT,
                 contact TEXT)''')
                 
    c.execute('''CREATE TABLE IF NOT EXISTS blood_inventory (
                 blood_type TEXT PRIMARY KEY,
                 quantity INTEGER)''')
                 
    c.execute('''CREATE TABLE IF NOT EXISTS blood_requests (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 patient_name TEXT,
                 blood_type TEXT,
                 quantity INTEGER,
                 status TEXT)''')
                 
    conn.commit()
    conn.close()

def add_donor(name, age, blood_type, contact):
    conn = sqlite3.connect("blood_bank.db")
    c = conn.cursor()
    c.execute("INSERT INTO donors (name, age, blood_type, contact) VALUES (?, ?, ?, ?)", (name, age, blood_type, contact))
    
    # Update blood inventory
    c.execute("INSERT INTO blood_inventory (blood_type, quantity) VALUES (?, ?) ON CONFLICT(blood_type) DO UPDATE SET quantity = quantity + 1", (blood_type, 1))
    
    conn.commit()
    conn.close()
    messagebox.showinfo("Success", "Donor added successfully!")

def request_blood(patient_name, blood_type, quantity):
    conn = sqlite3.connect("blood_bank.db")
    c = conn.cursor()
    
    # Check availability
    c.execute("SELECT quantity FROM blood_inventory WHERE blood_type = ?", (blood_type,))
    result = c.fetchone()
    if result and result[0] >= quantity:
        new_quantity = result[0] - quantity
        c.execute("UPDATE blood_inventory SET quantity = ? WHERE blood_type = ?", (new_quantity, blood_type))
        status = "Approved"
    else:
        status = "Pending"
    
    # Record request
    c.execute("INSERT INTO blood_requests (patient_name, blood_type, quantity, status) VALUES (?, ?, ?, ?)", 
              (patient_name, blood_type, quantity, status))
    
    conn.commit()
    conn.close()
    messagebox.showinfo("Request Status", f"Blood request {status}")

def view_inventory():
    conn = sqlite3.connect("blood_bank.db")
    c = conn.cursor()
    c.execute("SELECT * FROM blood_inventory")
    inventory = c.fetchall()
    conn.close()
    return inventory

def show_inventory():
    inventory = view_inventory()
    inventory_text.set("\n".join([f"{btype}: {qty}" for btype, qty in inventory]))

# GUI Implementation
root = tk.Tk()
root.title("Blood Bank Management System")
root.geometry("400x400")

inventory_text = tk.StringVar()
tk.Label(root, text="Blood Bank Inventory:").pack()
tk.Label(root, textvariable=inventory_text).pack()
tk.Button(root, text="Refresh Inventory", command=show_inventory).pack()

# Input Fields for Donor
tk.Label(root, text="Add Donor").pack()
tk.Label(root, text="Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()
tk.Label(root, text="Age:").pack()
age_entry = tk.Entry(root)
age_entry.pack()
tk.Label(root, text="Blood Type:").pack()
blood_type_entry = tk.Entry(root)
blood_type_entry.pack()
tk.Label(root, text="Contact:").pack()
contact_entry = tk.Entry(root)
contact_entry.pack()
tk.Button(root, text="Add Donor", command=lambda: add_donor(name_entry.get(), age_entry.get(), blood_type_entry.get(), contact_entry.get())).pack()

root.mainloop()

if __name__ == "__main__":
    init_db()
    print("Blood Bank Management System Initialized!")

