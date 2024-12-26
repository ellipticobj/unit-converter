

conv = {
    "length": {
        "meters": 1,
        "kilometers": 1000,
        "miles": 1000.34,
        "feet": 0.3048,
        "inches": 0.0254
    },
    "weight": {
        "kilograms": 1,
        "grams": 0.001,
        "pounds": 0.4536,
        "ounces": 0.0283495
    }
}

supportedtemps = ["celsius", "farenheit", "kelvin"]

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