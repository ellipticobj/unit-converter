from logic import *

# TODO: make a gui?
# TODO: make CURRENCY CONVERSION!!!!

while True:
    
    choice = input('''1. length
2. weight
3. temperature
input [1/2/3]: ''').lower().strip()

    if choice == "1":
        print(f"Supported units: {supportedlengths}")
        fromunit = input(f"input unit to convert from: ").lower().strip()
        while fromunit not in supportedlengths:
            print("invalid unit, please input a proper unit")
            fromunit = input("input unit to convert from: ").lower().strip()
            
        val = input("input value to convert [integer]: ").strip()
        while not val.isdigit():
            print("please input a number")
            val = input("input value to convert [integer]: ").strip()
        val = int(val)

        tounit = input("input unit to convert to: ").lower().strip()
        while tounit not in supportedlengths:
            print("invalid unit, please input a proper unit")
            tounit = input("input unit to convert from: ").lower().strip()
        
        final = convert(val, fromunit, tounit,"length")
        
    elif choice == "2":
        print(f"Supported units: {supportedweights}")
        fromunit = input("input unit to convert from: ").lower().strip()
        while fromunit not in supportedweights:
            print("invalid unit, please input a proper unit")
            fromunit = input("input unit to convert from: ").lower().strip()
            
        val = input("input value to convert [integer]: ").strip()
        while not val.isdigit():
            print("please input a number")
            val = input("input value to convert [integer]: ").strip()
        val = int(val)

        tounit = input("input unit to convert to: ").lower().strip()
        while tounit not in supportedweights:
            print("invalid unit, please input a proper unit")
            tounit = input("input unit to convert from: ").lower().strip()
        
        final = convert(val, fromunit, tounit,"weight")
    
    elif choice == "3":
        print(f"Supported units: {supportedtemps}")
        fromunit = input("input unit to convert from: ").lower().strip()
        while fromunit not in supportedtemps:
            print("invalid unit, please input a proper unit")
            fromunit = input("input unit to convert from: ").lower().strip()

        val = input("input value to convert [integer]: ").strip()
        while not val.isdigit():
            print("please input a number")
            val = input("input value to convert [integer]: ").strip()
        val = int(val)

        tounit = input("input unit to convert to: ").lower().strip()
        while tounit not in supportedtemps:
            print("invalid unit, please input a proper unit")
            tounit = input("input unit to convert from: ").lower().strip()
        
        final = converttemp(val, fromunit, tounit)
        
    print(f"{val} {fromunit} is {final:.2f} {tounit}")
    print()
    print()