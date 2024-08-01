from tkinter import *
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    fahrenheit = 32 + celsius*1.8
    return round(fahrenheit, 3)

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32)/1.8
    return round(celsius, 3)

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return round(celsius, 3)

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return round(kelvin, 3)

def convert():
    try:
        celsius = celsius_input.get(1.0, END)
        fahrenheit = fahrenheit_input.get(1.0, END)
        kelvin = kelvin_input.get(1.0, END)

        if len(celsius) > 1:
            celsius = float(celsius)
            fahrenheit = celsius_to_fahrenheit(celsius)
            kelvin = celsius_to_kelvin(celsius)
        elif len(kelvin) > 1:
            kelvin = float(kelvin)
            celsius = kelvin_to_celsius(kelvin)
            fahrenheit = celsius_to_fahrenheit(celsius)
        elif len(fahrenheit) > 1:
            fahrenheit = float(fahrenheit)
            celsius = fahrenheit_to_celsius(fahrenheit)
            kelvin = celsius_to_kelvin(celsius)

        celsius_input.delete(1.0, END)
        celsius_input.insert(END, celsius)
        fahrenheit_input.delete(1.0, END)
        fahrenheit_input.insert(END, fahrenheit)
        kelvin_input.delete(1.0, END)
        kelvin_input.insert(END, kelvin)

    except:
        print("error")

def clear():
    celsius_input.delete(1.0, END)
    fahrenheit_input.delete(1.0, END)
    kelvin_input.delete(1.0, END)

root = Tk()
root.geometry('550x400')
root.resizable(15, 15)
root.config(bg='#f2f2f2')
root.title("Temperature Converter App - JK")


Label(root, text="Celsius:", font='helvetica 20 bold', fg='black', bg='#f2f2f2').place(x=20, y=50)
Label(root, text="Fahrenheit:", font='helvetica 20 bold', fg='black', bg='#f2f2f2').place(x=20, y=125)
Label(root, text="Kelvin:", font='helvetica 20 bold', fg='black', bg='#f2f2f2').place(x=20, y=200)

celsius_input = Text(root, font='helvetica 20',width=20, height=1, wrap=WORD, padx=5, pady=5, bg='#e5e5e5')
celsius_input.place(x=200, y=50)
fahrenheit_input = Text(root, font='helvetica 20',width=20, height=1, wrap=WORD, padx=5, pady=5, bg='#e5e5e5')
fahrenheit_input.place(x=200, y=125)
kelvin_input = Text(root, font='helvetica 20',width=20, height=1, wrap=WORD, padx=5, pady=5, bg='#e5e5e5')
kelvin_input.place(x=200, y=200)

clearBtn = Button(root, text='Clear', font='helvetica 20 bold', padx=4, pady=4, command=clear, bg='#cccccc', fg='#ff0000', borderwidth=2, relief='ridge')
clearBtn.place(x=300, y=275)
convertBtn = Button(root, text='Convert', font='helvetica 20 bold', padx=4, pady=4, command=convert, bg='#cccccc', fg='#023020', borderwidth=2, relief='ridge')
convertBtn.place(x=150, y=275)

root.mainloop()