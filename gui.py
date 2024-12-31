import ttkbootstrap as ttk
from logic import *
from ttkbootstrap.constants import *

root = ttk.Window(themename="minty")
root.title("converter")

conversiontype = ttk.StringVar()
conversiontype.set("select conversion type...")
conversiontypes = ["length", "weight", "temperature", "currency"]

typelabel = ttk.Label(root, text="conversion type: ")
typelabel.pack(bootstyle="default", pady=5)

typemenu = ttk.OptionMenu(root, conversiontype, *conversiontypes)
typemenu.pack(pady=5)
