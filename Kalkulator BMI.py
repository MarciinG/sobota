from tkinter import *
from tkinter import messagebox

def reset_entry():
    age_tf.delete(0, 'end')
    height_tf.delete(0, 'end')
    weight_tf.delete(0, 'end')
    var.set(0)

def calculate_bmi():
    try:
        age = int(age_tf.get())
        if 2 <= age <= 120:
            kg = float(weight_tf.get())
            m = float(height_tf.get()) / 100
            bmi = kg / (m * m)
            bmi = round(bmi, 1)
            bmi_index(bmi)
        else:
            messagebox.showerror('BMI Calculator', 'Wprowadź poprawny wiek (2 - 120).')
    except ValueError:
        messagebox.showerror('BMI Calculator', 'Wprowadź poprawne wartości liczbowe.')

def bmi_index(bmi):
    if bmi < 18.5:
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi} oznacza Niedowagę.')
    elif 18.5 <= bmi < 24.9:
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi} oznacza Normalną wagę.')
    elif 25 <= bmi < 29.9:
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi} oznacza Nadwagę.')
    elif bmi >= 30:
        messagebox.showinfo('BMI Calculator', f'BMI = {bmi} oznacza Otyłość.')
    else:
        messagebox.showerror('BMI Calculator', 'Coś poszło nie tak!')

ws = Tk()
ws.title('Kalkulator BMI')
ws.geometry('400x300')
ws.config(bg='#686e70')

var = IntVar()

frame = Frame(
    ws,
    padx=10,
    pady=10
)
frame.pack(expand=True)

age_lb = Label(
    frame,
    text="Podaj wiek (2 - 120)"
)
age_lb.grid(row=1, column=1)

age_tf = Entry(
    frame,
)
age_tf.grid(row=1, column=2, pady=5)

gen_lb = Label(
    frame,
    text='Wybierz płeć'
)
gen_lb.grid(row=2, column=1)

frame2 = Frame(
    frame
)
frame2.grid(row=2, column=2, pady=5)

male_rb = Radiobutton(
    frame2,
    text='Mężczyzna',
    variable=var,
    value=1
)
male_rb.pack(side=LEFT)

female_rb = Radiobutton(
    frame2,
    text='Kobieta',
    variable=var,
    value=2
)
female_rb.pack(side=RIGHT)

height_lb = Label(
    frame,
    text="Podaj wzrost (cm)  "
)
height_lb.grid(row=3, column=1)

weight_lb = Label(
    frame,
    text="Podaj wagę (kg)  ",

)
weight_lb.grid(row=4, column=1)

height_tf = Entry(
    frame,
)
height_tf.grid(row=3, column=2, pady=5)

weight_tf = Entry(
    frame,
)
weight_tf.grid(row=4, column=2, pady=5)

frame3 = Frame(
    frame
)
frame3.grid(row=5, columnspan=3, pady=10)

cal_btn = Button(
    frame3,
    text='Oblicz BMI',
    command=calculate_bmi
)
cal_btn.pack(side=LEFT)

reset_btn = Button(
    frame3,
    text='Resetuj',
    command=reset_entry
)
reset_btn.pack(side=LEFT)

exit_btn = Button(
    frame3,
    text='Wyjście',
    command=lambda: ws.destroy()
)
exit_btn.pack(side=RIGHT)

ws.mainloop()
