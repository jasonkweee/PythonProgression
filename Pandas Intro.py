from tkinter import *
from tkinter import ttk
import pandas as pd

root = Tk()

cars= ttk.Frame(root, padding = 10)
cars.grid()

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}


ttk.Label(cars, text = mydataset["cars"] ).grid(column = 0, row = 0)
ttk.Label(cars, text = mydataset["passings"] ).grid(column = 0, row = 1)

myvar = pd.DataFrame(mydataset)
root.mainloop()

