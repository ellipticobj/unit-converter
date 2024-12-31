import ttkbootstrap as ttk
from logic import *
from ttkbootstrap.constants import *

root = ttk.Window(themename="minty")
root.title("converter")
root.geometry("400x200")
root.minsize(100, 100)

conversiontype = ttk.StringVar()
conversiontype.set("select conversion type...")
conversiontypes = ["length", "weight", "temperature", "currency"]

typelabel = ttk.Label(root, text="conversion type: ")
typelabel.pack(pady=5)

typemenu = ttk.OptionMenu(root, conversiontype, *conversiontypes)
typemenu.pack(pady=5)


root.mainloop()