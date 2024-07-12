import tkinter as tk
from tkinter import ttk
from call_nasm import call_nasm_program

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculatrice Simple")
        self.geometry("400x600")
        self.configure(bg="#1e1e1e")

        self.expression = ""
        self.create_widgets()

    def create_widgets(self):
        self.result_var = tk.StringVar()

        style = ttk.Style()
        style.configure("TButton", font=("Arial", 18), padding=10, relief="flat", background="#3a3f44", foreground="#ffffff")
        style.map("TButton", background=[("active", "#61dafb")], foreground=[("active", "#000000")])

        # Display
        self.result_display = tk.Entry(self, textvariable=self.result_var, font=('Arial', 24), bd=10, insertwidth=2, width=14, borderwidth=4, justify='right', bg="#282c34", fg="#61dafb", highlightbackground="#61dafb", highlightcolor="#61dafb")
        self.result_display.grid(row=0, column=0, columnspan=5, pady=20, padx=10, sticky='nsew')

        # Buttons
        buttons = [
            '7', '8', '9', '/', 'sqrt',
            '4', '5', '6', '*', '^2',
            '1', '2', '3', '-', '(',
            '0', '.', '=', '+', ')',
            'C'
        ]

        button_bg = "#3a3f44"
        button_fg = "#ffffff"
        button_active_bg = "#61dafb"
        button_active_fg = "#000000"

        row = 1
        col = 0
        for button in buttons:
            button_command = lambda x=button: self.on_button_click(x)
            tk.Button(self, text=button, padx=20, pady=20, bd=4, font=('Arial', 18), bg=button_bg, fg=button_fg,
                      activebackground=button_active_bg, activeforeground=button_active_fg,
                      command=button_command).grid(row=row, column=col, sticky='nsew', padx=5, pady=5)
            col += 1
            if col > 4:
                col = 0
                row += 1

        for i in range(5):
            self.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "=":
            try:
                self.calculate()
            except Exception as e:
                self.result_var.set("Erreur")
                print(f"Erreur: {e}")
        elif char == "C":
            self.expression = ""
            self.result_var.set("")
        elif char == "sqrt":
            self.expression += " sqrt"
            self.result_var.set(self.expression)
        elif char == "^2":
            self.expression += " ^2"
            self.result_var.set(self.expression)
        else:
            self.expression += str(char)
            self.result_var.set(self.expression)

    def calculate(self):
        try:
            result = call_nasm_program(self.expression)
            self.result_var.set(result)
            self.expression = str(result)
        except Exception as e:
            self.result_var.set("Erreur")
            print(f"Erreur: {e}")

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
