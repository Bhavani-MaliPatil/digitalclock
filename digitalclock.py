import tkinter as tk
from time import strftime

def time():
    current_time = strftime('%H:%M:%S %p')      # Example: 10:15:45 PM
    current_date = strftime('%A, %d %B %Y')      # Example: Monday, 04 August 2025
    label.config(text=f"{current_time}\n{current_date}")
    label.after(1000, time)  # Update every 1 second

# Create window
root = tk.Tk()
root.title("Digital Clock with Date")

# Configure the label
label = tk.Label(root, font=('calibri', 50, 'bold'), background='black', foreground='cyan', justify='center')
label.pack(anchor='center')

time()  # Start the clock
root.mainloop()
