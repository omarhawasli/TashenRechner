import customtkinter

class CalculatorApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("430x600")

        self.expression = ''
        self.result_var = customtkinter.StringVar()
        self.result_var.set("")

        self.label = customtkinter.CTkLabel(self, textvariable=self.result_var, width=80, height=75)
        self.label.pack(side="top")

        buttons = [
            ("7", 25, 100), ("8", 123, 100), ("9", 223, 100), ("*", 323, 100),
            ("4", 25, 200), ("5", 123, 200), ("6", 223, 200), ("-", 323, 200),
            ("1", 25, 300), ("2", 123, 300), ("3", 223, 300), ("+", 323, 300),
            ("0", 25, 400), (",", 123, 400), ("%", 223, 400), ("/", 323, 400),
            ("Clear", 25, 500), ("Backspace", 123, 500), ("Sqrt ", 223, 500), ("=", 323, 500)
        ]

        for text, x, y in buttons:
            btn = customtkinter.CTkButton(self, text=text, width=80, height=75,
                                          command=lambda t=text: self.button_callback(t))
            btn.place(x=x, y=y)

    def button_callback(self, value):
        if value == "=":
            try:
                result = str(eval(self.expression))
                self.result_var.set(result)
                self.expression = result
            except:
                self.result_var.set("Error")
                self.expression = ''
        elif value == "Clear":
            self.expression = ''
            self.result_var.set('')
        elif value == "Backspace":
            self.expression = self.expression[:-1]
            self.result_var.set(self.expression)
        else:
            self.expression += str(value)
            self.result_var.set(self.expression)


if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()
