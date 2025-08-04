import tkinter as tk
from time import strftime

def time():
    current_time = strftime('%H:%M:%S %p ')  # Format: Hour:Minute:Second AM/PM
    label.config(text=current_time)
    label.after(1000, time)  # Update every 1000 milliseconds (1 second)

# Create window
root = tk.Tk()
root.title("Digital Clock")

# Configure the label
label = tk.Label(root, font=('calibri', 50, 'bold'), background='black', foreground='cyan')
label.pack(anchor='center')

time()  # Call the time function

root.mainloop()
