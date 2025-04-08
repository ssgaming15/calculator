import tkinter as tk
from tkinter import ttk, messagebox
from math import sqrt, log, exp, sin, cos, tan

class CalculatorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Aesthetic Dark and Yellow Calculator")
        self.root.geometry("450x700")
        self.root.configure(bg="#1e1e2e")  # Dark modern background
        self.history = []  # For storing calculation history
        self.result_var = tk.StringVar()

        # Setup UI Elements
        self.create_display()
        self.create_buttons()
        self.create_history_section()

    def create_display(self):
        # Display Area
        display_frame = tk.Frame(self.root, bg="#1e1e2e")
        display_frame.pack(pady=20, padx=10)
        tk.Entry(
            display_frame, textvariable=self.result_var, font=("Arial", 28),
            bg="#1e1e2e", fg="#f3f547", justify="right", relief="flat", bd=5,
            insertbackground="#f3f547"  # Yellow cursor for entry
        ).pack(fill=tk.BOTH)

    def create_buttons(self):
        # Buttons Area
        button_frame = tk.Frame(self.root, bg="#1e1e2e")
        button_frame.pack(pady=20)

        buttons = [
            "7", "8", "9", "/", "C",
            "4", "5", "6", "*", "√",
            "1", "2", "3", "-", "^",
            "0", ".", "=", "+", "log",
            "sin", "cos", "tan", "exp", "Convert"
        ]

        row, col = 0, 0
        for btn in buttons:
            tk.Button(
                button_frame, text=btn, font=("Arial", 16, "bold"),
                bg="#2e2e3e", fg="#f3f547", width=6, height=2,
                activebackground="#43434f", activeforeground="#f3f547",
                relief="flat", bd=0,
                highlightthickness=0,
                command=lambda b=btn: self.on_button_click(b)
            ).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col == 5:  # Move to the next row after 5 buttons
                col = 0
                row += 1

    def create_history_section(self):
        # History Section
        history_frame = tk.Frame(self.root, bg="#1e1e2e")
        history_frame.pack(pady=10)
        tk.Label(
            history_frame, text="Calculation History", font=("Arial", 16),
            bg="#1e1e2e", fg="#f3f547"
        ).pack(pady=5)

        self.history_text = tk.Text(
            history_frame, height=8, font=("Arial", 14), bg="#2e2e3e", fg="#f3f547",
            wrap="word", relief="flat", bd=5
        )
        self.history_text.pack(fill=tk.BOTH, padx=10)

    def on_button_click(self, button):
        if button == "=":
            self.calculate_result()
        elif button == "C":
            self.result_var.set("")
        elif button == "√":
            self.handle_unary_operation(sqrt)
        elif button == "log":
            self.handle_unary_operation(lambda x: log(x, 10))
        elif button == "sin":
            self.handle_unary_operation(sin)
        elif button == "cos":
            self.handle_unary_operation(cos)
        elif button == "tan":
            self.handle_unary_operation(tan)
        elif button == "exp":
            self.handle_unary_operation(exp)
        elif button == "Convert":
            self.open_unit_converter()
        else:
            self.result_var.set(self.result_var.get() + button)

    def handle_unary_operation(self, operation):
        try:
            value = float(self.result_var.get())
            result = operation(value)
            self.result_var.set(result)
            self.history.append(f"{operation.__name__.capitalize()}({value}) = {result}")
            self.update_history()
        except Exception:
            messagebox.showerror("Error", "Invalid Input for Operation")

    def calculate_result(self):
        try:
            expression = self.result_var.get()
            result = eval(expression)  # Evaluate expression safely
            self.result_var.set(result)
            self.history.append(f"{expression} = {result}")
            self.update_history()
        except Exception:
            messagebox.showerror("Error", "Invalid Calculation")

    def update_history(self):
        self.history_text.delete(1.0, tk.END)
        self.history_text.insert(tk.END, "\n".join(self.history[-10:]))

    def open_unit_converter(self):
        unit_window = tk.Toplevel(self.root)
        unit_window.title("Unit Converter")
        unit_window.geometry("400x300")
        unit_window.configure(bg="#1e1e2e")

        tk.Label(unit_window, text="Unit Converter", font=("Arial", 16), bg="#1e1e2e", fg="#f3f547").pack(pady=10)

        # Dropdown Menu for Unit Selection
        conversions = {
            "Length (Meters to Feet)": lambda x: x * 3.28084,
            "Length (Feet to Meters)": lambda x: x / 3.28084,
            "Weight (Kg to Pounds)": lambda x: x * 2.20462,
            "Weight (Pounds to Kg)": lambda x: x / 2.20462,
            "Temperature (C to F)": lambda x: (x * 9/5) + 32,
            "Temperature (F to C)": lambda x: (x - 32) * 5/9,
        }

        selected_conversion = tk.StringVar(value=list(conversions.keys())[0])
        ttk.Combobox(unit_window, textvariable=selected_conversion, values=list(conversions.keys()), font=("Arial", 12)).pack(pady=10)

        input_var = tk.StringVar()
        tk.Entry(unit_window, textvariable=input_var, font=("Arial", 14), bg="#2e2e3e", fg="#f3f547").pack(pady=10)

        result_var = tk.StringVar()
        tk.Entry(unit_window, textvariable=result_var, font=("Arial", 14), bg="#2e2e3e", fg="#f3f547", state="readonly").pack(pady=10)

        def perform_conversion():
            try:
                value = float(input_var.get())
                conversion = conversions[selected_conversion.get()]
                result_var.set(conversion(value))
            except Exception:
                messagebox.showerror("Error", "Invalid Input for Conversion")

        tk.Button(unit_window, text="Convert", command=perform_conversion, font=("Arial", 14), bg="#43434f", fg="#f3f547").pack(pady=10)

# Main Execution
if __name__ == "__main__":
    root = tk.Tk()

    CalculatorGUI(root)
    root.mainloop()