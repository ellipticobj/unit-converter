import os
import requests
from dotenv import load_dotenv

load_dotenv()

conv = {
    "length": {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
        "mi": 1000.34,
        "ft": 0.3048,
        "in": 0.0254
    },
    "weight": {
        "kg": 1,
        "g": 0.001,
        "lbs": 0.4536,
        "oz": 0.0283495
    }
}

supportedlengths = ["mm", "cm", "m", "km", "mi", "ft", "in"]
supportedweights = ["kg", "g", "lbs", "oz"]
supportedtemps = ["c", "f", "k"]

def ctof(celsius: int) -> int:
    return celsius * 9/5 + 32

def ftoc(farenheit: int) -> int:
    return (farenheit - 32) * 5/9

def ctok(celsius: int) -> int:
    return celsius + 273.15

def ktoc(kelvins: int) -> int:
    return kelvins - 273.15

def converttemp(val: int, fromunit: str, tounit: str) -> int:
    if fromunit not in supportedtemps:
        raise ValueError(f"Unsupported temperature unit {fromunit}. Please input one of {supportedtemps}")
    
    if tounit not in supportedtemps:
        raise ValueError(f"Unsupported temperature unit {tounit}. Please input one of {supportedtemps}")
    
    if fromunit == tounit:
        return val
    elif fromunit == "celsius":
        return ctof(val) if tounit == "farenheit" else ctok(val)
    elif fromunit == "farenheit":
        return ftoc(val) if tounit == "celsius" else ctok(ftoc(val))
    elif fromunit == "kelvin":
        return ktoc(val) if tounit == "celsius" else ctof(ktoc(val))

def convert(val: int, fromunit: str, tounit: str, lengthorweight: str) -> int:
    if fromunit not in set(conv[lengthorweight].keys()):
        raise ValueError(f"Unsupported length unit {fromunit}. Please input a proper unit.")
    if tounit not in set(conv[lengthorweight].keys()):
        raise ValueError(f"Unsupported length unit {tounit}. Please input a proper unit.")
    
    if fromunit == tounit:
        return val
    else:
        return val * (conv[lengthorweight][fromunit]/conv[lengthorweight][tounit])
    
def getavailablecurrencies() -> list:
    response = requests.get(f"https://api.freecurrencyapi.com/v1/currencies?apikey={os.getenv("APIKEY")}&currencies=")
    response.raise_for_status()
    
    data = response.json()
    return list(data["data"].keys())

def convertcurr(val: int, basecurr: str, tocurr: str) -> int:
    if basecurr == tocurr:
        return val
    availablecurrs = set(getavailablecurrencies())
    if basecurr not in availablecurrs:
        raise ValueError(f"Unsupported currency {basecurr}.")
    if tocurr not in availablecurrs:
        raise ValueError(f"Unsupported currency {tocurr}.")

    response = requests.get(f"https://api.freecurrencyapi.com/v1/latest?apikey={os.getenv("APIKEY")}&currencies={tocurr}&base_currency={basecurr}")
    response.raise_for_status()
    data = response.json()
    return data["data"][tocurr]

def getvalfromuser(prompt:str="Input value to convert [number]: ", errormsg:str="Please input a number"):
    while True:
        val = input(prompt).strip()
        try:
            val = float(val)
            break
        except ValueError:
            print(errormsg)
    val = float(val)
    return val
