from logic import *

while True:
    print("unit convertor")
    
    choice = input('''1. length
2. weight
3. temperature
input [1/2/3]: ''').lower().strip()
    
    val = input("input value to convert [integer]: ").strip()
    while not val.isdigit():
        print("please input a number")
        val = input("input value to convert [integer]: ").strip()
    val = int(val)
    
    if choice == "1":
        print(f"Supported units: {set(conv["length"].keys())}")
        fromunit = input(f"input unit to convert from: ").lower().strip()
        while fromunit not in set(conv["length"].keys()):
            print("invalid unit, please input a proper unit")
            print(f"Supported units: {set(conv["length"].keys())}")
            fromunit = input("input unit to convert from: ").lower().strip()

        tounit = input("input unit to convert to: ").lower().strip()
        while tounit not in set(conv["length"].keys()):
            print("invalid unit, please input a proper unit")
            print(f"Supported units: {set(conv["length"].keys())}")
            tounit = input("input unit to convert from: ").lower().strip()
        
        print(f"{val} {fromunit} is {convert(val, fromunit, tounit,"length")} {tounit}")
        
    elif choice == "2":
        print(f"Supported units: {set(conv["weight"].keys())}")
        fromunit = input("input unit to convert from: ").lower().strip()
        while fromunit not in set(conv["weight"].keys()):
            print("invalid unit, please input a proper unit")
            print(f"Supported units: {set(conv["weight"].keys())}")
            fromunit = input("input unit to convert from: ").lower().strip()

        tounit = input("input unit to convert to: ").lower().strip()
        while tounit not in set(conv["weight"].keys()):
            print("invalid unit, please input a proper unit")
            print(f"Supported units: {set(conv["weight"].keys())}")
            tounit = input("input unit to convert from: ").lower().strip()
        
        print(f"{val} {fromunit} is {convert(val, fromunit, tounit,"weight")} {tounit}")
    
    elif choice == "3":
        print(f"Supported units: {supportedtemps}")
        fromunit = input("input unit to convert from: ").lower().strip()
        while fromunit not in supportedtemps:
            print("invalid unit, please input a proper unit")
            print(f"Supported units: {supportedtemps}")
            fromunit = input("input unit to convert from: ").lower().strip()

        tounit = input("input unit to convert to: ").lower().strip()
        while tounit not in supportedtemps:
            print("invalid unit, please input a proper unit")
            print(f"Supported units: {supportedtemps}")
            tounit = input("input unit to convert from: ").lower().strip()
        
        print(f"{val} {fromunit} is {converttemp(val, fromunit, tounit)} {tounit}")