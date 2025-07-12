import tkinter

button_values = [
    ["AC", "+/-", "%", "÷"], 
    ["7", "8", "9", "×"], 
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "√", "="]
]

simbol_kanan = ["÷", "×", "-", "+", "="]
simbol_atas = ["AC", "+/-", "%"]

row_count = len(button_values)
column_count = len(button_values[0])

color_pink1 = "#FF99BB"
color_pink2 = "#EC4E83"
color_beige = "#FBF5DE"
color_white = "white"
color_black = "#3A0519"

#window setup
window = tkinter.Tk()
window.title("CALCULATOR")
window.resizable(False, False)

frame = tkinter.Frame(window)
label = tkinter.Label(frame, text="0", font=("Poppins", 45), 
                      background=color_white, foreground=color_black, anchor="e",
                      width=column_count)

label.grid(row=0, column=0, columnspan=column_count, sticky="we")

for row in range(row_count):
    for column in range(column_count):
        value = button_values[row][column]
        button = tkinter.Button(frame, text=value, font=("poppins", 30),
                            width=column_count-1, height=1,
                            command=lambda value=value: button_clicked(value))
        
        if value in simbol_atas:
            button.config(foreground=color_black, background=color_pink1)
        elif value in simbol_kanan:
            button.config(foreground=color_white, background=color_pink2)
        else:
            button.config(foreground=color_black, background=color_beige)  

        button.grid(row=row+1, column=column)
   
frame.pack()

#pertambahan, penguragan, perkalian, pembagian
A = "0"
operator = None
B = None

def clear_all():
    global A, B, operator
    A = "0"
    operator = None
    B = None

def remove_zero_decimal(num):
    if num % 1 == 0:
        num = int (num)
    return str(num)

#fungsi button 
def button_clicked(value):
    global simbol_kanan, simbol_atas, label, A, B, operator

    if value in simbol_kanan:
        if value == "=":
            if A is not None and operator is not None:
                B = label["text"]
                numA = float(A)
                numB = float(B)

                try:
                    if operator == "+":
                        result = numA + numB
                    elif operator == "-":
                        result = numA - numB
                    elif operator == "×":
                        result = numA * numB
                    elif operator == "÷":
                        result = numA / numB

                    label["text"] = remove_zero_decimal(result)
                    A = str(result)
                    operator = None
                    B = None
                except ZeroDivisionError:
                    label["text"] = "Error"
                    clear_all()

        elif value in "+-×÷":
            if operator is None:
                A = label["text"]
                label["text"] = "0"
                B = None

            operator = value

    elif value in simbol_atas:
        if value == "AC":
            clear_all()
            label["text"] = "0"

        elif value == "+/-":
            result = float(label["text"]) * -1
            label["text"] = remove_zero_decimal(result)

        elif value == "%":
            result = float(label["text"]) / 100
            label["text"] = remove_zero_decimal(result)

    elif value == "√":
        result = float(label["text"]) ** 0.5
        label["text"] = remove_zero_decimal(result)

    else:
        if value == ".":
            if "." not in label["text"]:
                label["text"] += value
        elif value in "0123456789":
            if label["text"] == "0":
                label["text"] = value
            else:
                label["text"] = str(label["text"]) + str(value)


#agar muncul di tengah layar 
window.update()
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = int ((screen_width/2) - (window_width/2))
window_y = int ((screen_height/2) - (window_height/2))

#format "(w)x(y)+(x)+(Y)"
window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")
window.mainloop()