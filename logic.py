

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

def ctof(celsius):
    return celsius * 9/5 + 32

def ftoc(farenheit):
    return (farenheit - 32) * 5/9

def ctok(celsius):
    return celsius + 273.15

def ktoc(kelvins):
    return kelvins - 273.15

def converttemp(val, fromunit, tounit):
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

def convertlength(val, fromunit, tounit):
    # TODO
    return 0

def convertmass(val, fromunit, tounit):
    # TODO
    return 0