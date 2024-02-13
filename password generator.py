import tkinter as tk
import random
import string

def generate_password():
    password_length = int(entry_length.get())
    
    if password_length < 4:
        label_password.config(text="Password length must be at least 4 characters")
        return
    
    strength = selected_strength.get()
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_chars = string.punctuation
    
    if strength == "Low":
        chars = lowercase + uppercase
    elif strength == "Medium":
        chars = lowercase + uppercase + digits
    else:  # Strong
        chars = lowercase + uppercase + digits + special_chars
        
    generated_password = ''.join(random.sample(chars, password_length))
    label_password.config(text=generated_password)

# Create main window
window = tk.Tk()
window.title("Password Generator")

# Password length entry
label_length = tk.Label(window, text="Password Length:")
label_length.grid(row=0, column=0, padx=5, pady=5)
entry_length = tk.Entry(window)
entry_length.grid(row=0, column=1, padx=5, pady=5)

# Radio buttons for password strength
selected_strength = tk.StringVar(value="Low")
label_strength = tk.Label(window, text="Password Strength:")
label_strength.grid(row=1, column=0, padx=5, pady=5)
radio_low = tk.Radiobutton(window, text="Low", variable=selected_strength, value="Low")
radio_low.grid(row=1, column=1, padx=5, pady=5)
radio_medium = tk.Radiobutton(window, text="Medium", variable=selected_strength, value="Medium")
radio_medium.grid(row=1, column=2, padx=5, pady=5)
radio_strong = tk.Radiobutton(window, text="Strong", variable=selected_strength, value="Strong")
radio_strong.grid(row=1, column=3, padx=5, pady=5)

# Button to generate password
button_generate = tk.Button(window, text="Generate Password", command=generate_password)
button_generate.grid(row=2, column=0, columnspan=4, padx=5, pady=5)

# Label to display generated password
label_password = tk.Label(window, text="")
label_password.grid(row=3, column=0, columnspan=4, padx=5, pady=5)

window.mainloop()
