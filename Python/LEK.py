### LEK

import tkinter as tk
import random


class converter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Temperature Converter")
        self.var1 = tk.StringVar()
        self.var1.set("Input Scale")
        self.var2 = tk.StringVar()
        self.var2.set("Output Scale")
        self.confloat = tk.DoubleVar()

        self.menu1 = tk.OptionMenu(
            self.root,
            self.var1,
            "Celsius",
            "Kelvin",
            "Fahrenheit",
            command=self.display_selected,
        )
        self.menu1.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.menu2 = tk.OptionMenu(
            self.root,
            self.var2,
            "Celsius",
            "Kelvin",
            "Fahrenheit",
            command=self.display_selected,
        )
        self.menu2.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        # Top option entry
        self.username_entry = tk.Entry(self.root)
        self.username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)
        # Output box
        self.label = tk.Label(self.root, text="output")
        self.label.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        self.convert_button = tk.Button(
            self.root,
            text="Convert",
            bg="#" + ("%06x" % random.randint(0, 16777215)),
            fg="#" + ("%06x" % random.randint(0, 16777215)),
            command=self.convert,
        )
        self.convert_button.grid(
            column=1, row=3, sticky=tk.E, padx=5, pady=5,
        )

        self.root.mainloop()

    def display_selected(self, choice):
        choice1 = self.var1.get()
        choice2 = self.var2.get()

    def convert(self):
        numcon = self.username_entry.get()
        if self.var1.get() == "Kelvin" and self.var2.get() == "Celsius":
            self.label.config(text=float(numcon) - 273.15)
        elif self.var1.get() == "Kelvin" and self.var2.get() == "Fahrenheit":
            self.label.config(text=1.8 * (float(numcon) - 273.15) + 32.00)
        elif self.var1.get() == "Celsius" and self.var2.get() == "Kelvin":
            self.label.config(text=float(numcon) + 273.15)
        elif self.var1.get() == "Celsius" and self.var2.get() == "Fahrenheit":
            self.label.config(text=float(numcon) * 1.8000) + 32.00
        elif self.var1.get() == "Fahrenheit" and self.var2.get() == "Celsius":
            self.label.config(text=(float(numcon) - 32.00) / 1.8000)
        elif self.var1.get() == "Fahrenheit" and self.var2.get() == "Kelvin":
            self.label.config(text= 5 / 9(float(numcon) - 32.00) + 273.15)


converter()
