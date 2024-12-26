

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

def ctof(celsius: int):
    return celsius * 9/5 + 32

def ftoc(farenheit: int):
    return (farenheit - 32) * 5/9

def ctok(celsius: int):
    return celsius + 273.15

def ktoc(kelvins: int):
    return kelvins - 273.15

def converttemp(val: int, fromunit: str, tounit: str):
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

def convert(val: int, fromunit: str, tounit: str, lengthorweight: str):
    if fromunit not in set(conv[lengthorweight].keys()):
        raise ValueError(f"Unsupported length unit {fromunit}. Please input a proper unit.")
    if tounit not in set(conv[lengthorweight].keys()):
        raise ValueError(f"Unsupported length unit {tounit}. Please input a proper unit.")
    
    if fromunit == tounit:
        return val
    else:
        return val * (conv[lengthorweight][fromunit]/conv[lengthorweight][tounit])