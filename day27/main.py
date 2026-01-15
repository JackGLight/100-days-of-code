import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
window.minsize(500,300)

#Entry
input = tk.Entry()
input.grid(column=1, row=0)

#miles label
my_label = tk.Label(text="Miles", font=('Arial', 26))
my_label.grid(column=2, row=0)
my_label.config(padx=10, pady=10)

#Km label
my_label = tk.Label(text="Km", font=('Arial', 26))
my_label.grid(column=2, row=1)
my_label.config(padx=10, pady=10)

#is equal to label
my_label = tk.Label(text="is equal to", font=('Arial', 26))
my_label.grid(column=0, row=1)
my_label.config(padx=10, pady=10)

#Km value label
km_label = tk.Label(text="0", font=('Arial', 26))
km_label.grid(column=1, row=1)
km_label.config(padx=10, pady=10)

def calculate():
    num = float(input.get())
    num *= 1.60934
    km_label["text"] = num




#new button 
new_button = tk.Button()
new_button.config(text="Calculate", command=calculate)
new_button.grid(column=1, row=2)







window.mainloop()