import ttkbootstrap as ttk
from logic import *
from ttkbootstrap.constants import *

root = ttk.Window(themename="minty")
root.title("converter")
root.geometry("400x400")
root.minsize(400, 400)

default_font = ("Arial", 12)
style = ttk.Style()
style.configure(".", font=default_font)

def showpage(page):
    for frame in frames.values():
        frame.pack_forget()
    frames[page].pack(fill="both", expand=True)

def checktype():
    choice = conversiontype.get()
    
    if choice == "length":
        units = supportedlengths
    
    elif choice == "weight":
        units = supportedweights
    
    elif choice == "temperature":
        units = supportedtemps
    
    elif choice == "currency":
        try: 
            units = getavailablecurrencies()
        except Exception as e:
            typeerrorlabel.config(text=f"error retrieving currencies: {e}")
            units = []
        
    fromunit.set(units[0])
    tounit.set(units[0])
    
    frommenu["menu"].delete(0, "end")
    tomenu["menu"].delete(0, "end")
    
    for unit in units:
        frommenu["menu"].add_command(label=unit, command=lambda u=unit: fromunit.set(u))
        tomenu["menu"].add_command(label=unit, command=lambda u=unit: tounit.set(u))

def convertfunc():
    choice = conversiontype.get()
    
    from_unit = fromunit.get()
    to_unit = tounit.get()
    
    value = valinp.get().strip()
    
    print(value == "")
    
    if value == "":
        valerrorlabel.config(text="please enter a number")
        return
    
    try:
        value = float(value.strip())
    except ValueError:
        valerrorlabel.config(text="please enter a valid number")
        return
    
    try:
        if choice in ["length", "weight"]:
            result = convert(value, from_unit, to_unit, choice)
        elif choice == "temperature":
            result = converttemp(value, from_unit, to_unit)
        elif choice == "currency":
            result = convertcurr(value, from_unit, to_unit)
        
        resultlabel.config(text=f"{value} {from_unit} is {result:.2f} {to_unit}")
        showpage("result")
    except Exception as e:
        resulterrorlabel.config(text=f"conversion error: {e}")


frames = {}


frame1 = ttk.Frame(root)
frames["selecttype"] = frame1

conversiontype = ttk.StringVar()
conversiontype.set("select conversion type...")
conversiontypes = ["length", "weight", "temperature", "currency"]

typelabel = ttk.Label(frame1, text="conversion type: ")
typelabel.pack(pady=5)

typemenu = ttk.OptionMenu(frame1, conversiontype, *conversiontypes)
typemenu.pack(pady=5)

typeerrorlabel = ttk.Label(frame1, text="", bootstyle="danger")
typeerrorlabel.pack(pady=5)

nextbutton = ttk.Button(frame1, text="next", command=lambda: (checktype(), showpage("conversion")), bootstyle="success-outline")
nextbutton.pack(pady=10)


frame2 = ttk.Frame(root)
frames["conversion"] = frame2

fromunit = ttk.StringVar()
fromunit.set("select unit")

fromlabel = ttk.Label(frame2, text="from unit: ")
fromlabel.pack(pady=5)

frommenu = ttk.OptionMenu(frame2, fromunit, "")
frommenu.pack(pady=5)

tounit = ttk.StringVar()
tounit.set("select unit: ")

tolabel = ttk.Label(frame2, text="to unit: ")
tolabel.pack(pady=5)

tomenu = ttk.OptionMenu(frame2, tounit, "")
tomenu.pack(pady=5)

vallabel = ttk.Label(frame2, text="number: ")
vallabel.pack(pady=5)

valinp = ttk.Entry(frame2)
valinp.pack(pady=5)

valerrorlabel = ttk.Label(frame2, text="", bootstyle="danger")
valerrorlabel.pack(pady=5)

convertbutton = ttk.Button(frame2, text="convert", command=lambda: (convertfunc(), showpage("result")), bootstyle="success")
convertbutton.pack(pady=10)


frame3 = ttk.Frame(root)
frames["result"] = frame3

resultlabel = ttk.Label(frame3, text="", font=("Arial", 16))
resultlabel.pack(pady=10)

resulterrorlabel = ttk.Label(frame3, text="")
resulterrorlabel.pack(pady=5)

showpage("selecttype")
root.mainloop()