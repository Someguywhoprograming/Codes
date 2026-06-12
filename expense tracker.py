import tkinter as tk
from tkinter import messagebox

def save_data():
    with open("expenses.text", "w") as f:
        for item in listbox.get(0, tk.END):
            f.write(item + "\n")

def load_data():
    try:
        with open("expenses.text", "r") as f:
            for line in f:
                if line.strip():
                    listbox.insert(tk.END, line.strip())


            if listbox.size() > 0:
                current_total = sum(float(i.split(
                    '$')[1]) for i in listbox.get(
                        0, tk.END))
                label_total.config(
                    text=f"Total: $ {current_total:.2f}")
    except FileNotFoundError:
        pass

def add_expense(event=None):
    desc = entery_desc.get()
    amt = entery_amt.get()

    if desc and amt:
        try:
            value = float(amt)
            listbox.insert(
                tk.END, f"{desc}: ${value:.2f}")
            entery_desc.delete(0, tk.END)
            entery_amt.delete(0, tk.END)

            current_total = sum(float(i.split('$')[1]
                    ) for i in listbox.get(0, tk.END))
            label_total.config(
                text=f"Total: ${current_total:.2f}")
            
            save_data()
            entery_desc.focus_set()
        except ValueError:
            messagebox.showerror("Error",
                    "Amount must be a number")
        else:
            messagebox.showwarning("Warning", 
                                   "Fill all fields")
            
root = tk.Tk()
root.title("Pocket Tracker")
root.geometry("300x450")

tk.Label(root, text="Description").pack(pady=5)
entery_desc = tk.Entry(root)
entery_desc.pack(pady=5)

tk.Label(root, text="Amount ($)").pack(pady=5)
entery_amt = tk.Entry(root)
entery_amt.pack(pady=5)

tk.Button(root,
          text="Add Expense",
          command=add_expense).pack(pady=10)

listbox = tk.Listbox(root)
listbox.pack(pady=10, fill=tk.BOTH, expand=True,
             padx=20)

label_total = tk.Label(root,
                       text="Total: $0.00",
                       font=("Arial", 12, "bold"))
label_total.pack(pady=10)

root.bind('<Return>', add_expense)

load_data()

root.mainloop()