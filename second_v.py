import tkinter as tk

FONT = ("verdana", 14, "bold")

window = tk.Tk()
window.title("Convert Miles to Km")
window.config(padx=30, pady=15)

# list of labels

miles_label = tk.Label(text="Miles", font=FONT)
miles_label.grid(column=3, row=0)
miles_label.config(padx=10, pady=10)

equal_label = tk.Label(text="is equal to", font=FONT)
equal_label.grid(column=0, row=1)
equal_label.config(padx=10, pady=10)

km_label = tk.Label(text="Km", font=FONT)
km_label.grid(column=3, row=1)
km_label.config(padx=10, pady=10)

convert_label = tk.Label()
convert_label.grid(column=1, row=1)


# list of entries

miles_input = tk.Entry(width=10)
miles_input.grid(column=1, row=0)

# list of buttons


def convert():
    miles_convert = miles_input.get()
    km_convert = int(int(miles_convert)*1.6093)
    convert_label.config(text=f"{km_convert}")
    # versao antiga criando a label no botao
    # km_final = tk.Label(text=f"{km_convert}", font=("verdana", 16))
    # km_final.grid(column=1, row=1)


button = tk.Button(text="Convert", command=convert)
button.grid(column=1, row=2)


window.mainloop()
