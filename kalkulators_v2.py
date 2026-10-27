import tkinter as tk

root = tk.Tk()
root.title("Kalkulators")
root.geometry("410x650")
root.resizable(False, False)
root.configure(bg="#808080")

display_var = tk.StringVar(value="0")
expression = ""

def calculate(event=None):
    global expression
    try:
        result = eval(expression.replace("x", "*"), {"__builtins__": {}}, {})
        if isinstance(result, float) and result.is_integer():
            result = int(result)
        expression = str(result)
        display_var.set(expression)
    except Exception:
        expression = ""
        display_var.set("Error")

def press(value):
    global expression

    if value == "=":
        calculate()
        return
    if value == "C":
        expression = ""
        display_var.set("0")
        return
    if value == "⌫":
        expression = expression[:-1]
        display_var.set(expression if expression else "0")
        return

    if value in "+-x/":
        if not expression:
            if value != "-":
                return
            expression = "-"
        elif expression[-1] in "+-x/":
            expression = expression[:-1] + value
        else:
            expression += value
    else:
        expression += value
    display_var.set(expression)

root.bind("<Return>", calculate)
root.bind("<KP_Enter>", calculate)

display = tk.Entry(root, textvariable=display_var, font=("Arial", 28),
                   justify="left", bg="#c0c0c0", fg="black",
                   relief="sunken", bd=3)
display.place(x=35, y=20, width=340, height=95)

buttons = [
    ("1", 35, 135), ("2", 125, 135), ("3", 215, 135),
    ("4", 35, 220), ("5", 125, 220), ("6", 215, 220),
    ("7", 35, 305), ("8", 125, 305), ("9", 215, 305),
    ("0", 35, 390),
    ("+", 315, 135), ("-", 315, 220), ("x", 315, 305), ("/", 315, 390),
    (".", 35, 485), ("(", 125, 485), (")", 215, 485), ("=", 315, 485),
    ("C", 35, 570), ("⌫", 125, 570),
]

sizes = {"0": (270, 70), "C": (75, 55), "⌫": (75, 55)}

for text, x, y in buttons:
    width, height = sizes.get(text, (75, 70))
    tk.Button(root, text=text, font=("Arial", 22, "bold"),
              command=lambda v=text: press(v), bg="#eeeeee", fg="black",
              activebackground="#dddddd", relief="raised", bd=3).place(
                  x=x, y=y, width=width, height=height)

root.mainloop()
