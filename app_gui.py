import tkinter as tk

window = tk.Tk()
window.title("Temperature Converter")

def celsiusConverter():
     try:
         fahrenheitTemp = float(temperatureEntry.get())
         celsiusTemp = (fahrenheitTemp - 32) * (5/9)
         answerLabel["text"] = f"{celsiusTemp}\N{DEGREE CELSIUS}"
     except:
         answerLabel["text"] = f"digits only"

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0,1,2,3,4,5], minsize=30, weight=1)

temperatureEntry = tk.Entry(master = window, bg="green", fg="white")
temperatureEntry.grid(row=0, column=1, padx=2)

temperatureLabel = tk.Label(master = window, text = "\N{DEGREE FAHRENHEIT}")
temperatureLabel.grid(row=0, column=2)

convertButton = tk.Button(master = window, text = "\N{RIGHTWARDS BLACK ARROW}", command = celsiusConverter)
convertButton.grid(row=0, column=3)

answerLabel = tk.Label(master = window, text = "\N{DEGREE CELSIUS}")
answerLabel.grid(row=0, column=4)

window.mainloop()
