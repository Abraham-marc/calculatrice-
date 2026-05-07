from tkinter import *
from logic import Calculator
import sys
import colorama

calc = Calculator()
calc_input = ""

def run():
    window = Tk()
    window.title("Calculatrice Scientifique")
    window.configure(padx=10, pady=10) 

    calc_input_text = StringVar()
    result_text = StringVar()

    def input_key(value):
        global calc_input
        calc_input += str(value)
        calc_input_text.set(calc_input)

    def equal():
        global calc_input
        result = calc.interface(calc_input) 
        result_text.set(str(result))
        calc_input = str(result) 

    def clear():
        global calc_input
        calc_input = ""
        calc_input_text.set("")
        result_text.set("")

    
    Label(window, ).grid(row=0, column=0, sticky="w")
    Entry(window, textvariable=calc_input_text, font=("Arial", 14), width=25, justify="right").grid(row=1, column=0, columnspan=5, pady=5)
    
    Label(window, ).grid(row=2, column=0, sticky="w")
    Entry(window, textvariable=result_text, font=("Arial", 16, "bold"), width=20, justify="right", fg="blue").grid(row=3, column=0, columnspan=5, pady=5)
    
    Button(window, text="sin", width=5, command=lambda: input_key("sin(")).grid(row=4, column=0)
    Button(window, text="cos", width=5, command=lambda: input_key("cos(")).grid(row=4, column=1)
    Button(window, text="tan", width=5, command=lambda: input_key("tan(")).grid(row=4, column=2)
    Button(window, text="exp", width=5, command=lambda: input_key("exp(")).grid(row=4, column=3)
    Button(window, text="^", width=5, command=lambda: input_key("^")).grid(row=4, column=4)

    Button(window, text=" 7 ", width=5, command=lambda: input_key("7")).grid(row=5, column=0)
    Button(window, text=" 8 ", width=5, command=lambda: input_key("8")).grid(row=5, column=1)
    Button(window, text=" 9 ", width=5, command=lambda: input_key("9")).grid(row=5, column=2)
    Button(window, text=" / ", width=5, command=lambda: input_key("/")).grid(row=5, column=3)
    Button(window, text=" ( ", width=5, command=lambda: input_key("(")).grid(row=5, column=4)

    Button(window, text=" 4 ", width=5, command=lambda: input_key("4")).grid(row=6, column=0)
    Button(window, text=" 5 ", width=5, command=lambda: input_key("5")).grid(row=6, column=1)
    Button(window, text=" 6 ", width=5, command=lambda: input_key("6")).grid(row=6, column=2)
    Button(window, text=" * ", width=5, command=lambda: input_key("*")).grid(row=6, column=3)
    Button(window, text=" ) ", width=5, command=lambda: input_key(")")).grid(row=6, column=4)

    Button(window, text=" 1 ", width=5, command=lambda: input_key("1")).grid(row=7, column=0)
    Button(window, text=" 2 ", width=5, command=lambda: input_key("2")).grid(row=7, column=1)
    Button(window, text=" 3 ", width=5, command=lambda: input_key("3")).grid(row=7, column=2)
    Button(window, text=" - ", width=5, command=lambda: input_key("-")).grid(row=7, column=3)

    Button(window, text=" 0 ", width=5, command=lambda: input_key("0")).grid(row=8, column=0)
    Button(window, text=" . ", width=5, command=lambda: input_key(".")).grid(row=8, column=1)
    Button(window, text=" = ", width=5, bg="orange", command=equal).grid(row=8, column=2)
    Button(window, text=" + ", width=5, command=lambda: input_key("+")).grid(row=8, column=3)

    Button(window, text="EFFACER", width=12, bg="red", fg="white", command=clear).grid(row=9, column=0, columnspan=2, pady=10)
    Button(window, text="QUITTER", width=12, command=window.quit).grid(row=9, column=3, columnspan=2, pady=10)

    window.mainloop()

if __name__ == "__main__":
    run()
