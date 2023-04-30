import tkinter as tk

def update_text(var_dict, dose_dict, menubutton, bill_label):
    selected_items = [item for item, var in var_dict.items() if var.get()]
    total_bill = 0
    if selected_items:
        for item in selected_items:
            dose = dose_dict[item].get()
            if int(dose) > 0:
                total_bill += int(dose) * prices[item]
        menubutton.config(text=", ".join("{} x {}".format(item, dose_dict[item].get()) for item in selected_items))
    else:
        menubutton.config(text="Select Medicines")
    bill_label.config(text="Total Bill: ${:.2f}".format(total_bill))

root = tk.Tk()
medicines = ["Paracetamol", "Ibuprofen", "Aspirin", "Codeine"]
prices = {"Paracetamol": 2.50, "Ibuprofen": 3.50, "Aspirin": 1.75, "Codeine": 5.00}
var_dict = {}
dose_dict = {}

# Create the menubutton
menubutton = tk.Menubutton(root, text="Select Medicines", indicatoron=True, borderwidth=1, relief="solid")
menubutton.pack()

# Create a custom menu
menu = tk.Menu(menubutton, tearoff=False)

# Add the checkboxes and doses to the menu
for item in medicines:
    var = tk.BooleanVar(value=False)
    var_dict[item] = var
    dose_var = tk.StringVar(value="0")
    dose_dict[item] = dose_var
    menu.add_checkbutton(label=item, variable=var, onvalue=True, offvalue=False)
    menu.add_command(label=f"Enter dose for {item}", command=lambda x=item: root.after(1, get_dose(x, dose_dict)))

# Define a function to get the dose from the user
def get_dose(item, dose_dict):
    top = tk.Toplevel(root)
    top.title(f"Enter dose for {item}")
    entry = tk.Entry(top, width=10, textvariable=dose_dict[item])
    entry.pack(padx=10, pady=10)
    button = tk.Button(top, text="OK", command=top.destroy)
    button.pack(pady=10)

# Add a separator and a "Clear" option to the menu
menu.add_separator()
menu.add_command(label="Clear", command=lambda: clear_menu(var_dict, dose_dict, menubutton, bill_label))

# Set the menubutton's menu to the custom menu
menubutton.config(menu=menu)

# Create a label to display the total bill
bill_label = tk.Label(root, text="Total Bill: $0.00")
bill_label.pack()

# Update the menubutton's text and the total bill when the user selects a checkbox
menu.config(postcommand=lambda: update_text(var_dict, dose_dict, menubutton, bill_label))

# Define a function to clear the menu and reset the bill
def clear_menu(var_dict, dose_dict, menubutton, bill_label):
    for var in var_dict.values():
        var.set(False)
    for dose_var in dose_dict.values():
        dose_var.set("0")
    menubutton.config(text="Select Medicines")
    bill_label.config(text="Total Bill: $0.00")

root.mainloop()
