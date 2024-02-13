import tkinter as tk

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")
        
        self.display_var = tk.StringVar()
        self.display_var.set("0")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Create display entry
        self.display_entry = tk.Entry(self.master, textvariable=self.display_var, font=("Arial", 20), bd=10, insertwidth=4, width=15, justify="right")
        self.display_entry.grid(row=0, column=0, columnspan=4)
        
        # Create buttons
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]
        
        for (text, row, col) in buttons:
            button = tk.Button(self.master, text=text, font=("Arial", 18), padx=20, pady=20, command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col)
            
        # Create Clear button
        clear_button = tk.Button(self.master, text="Clear", font=("Arial", 18), padx=20, pady=20, command=self.clear_display)
        clear_button.grid(row=5, column=0, columnspan=4)
        
    def on_button_click(self, value):
        if value == "=":
            try:
                result = eval(self.display_var.get())
                self.display_var.set(str(result))
            except Exception as e:
                self.display_var.set("Error")
        elif value == "C":
            self.clear_display()
        else:
            current_display = self.display_var.get()
            if current_display == "0":
                self.display_var.set(value)
            else:
                self.display_var.set(current_display + value)
                
    def clear_display(self):
        self.display_var.set("0")

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
