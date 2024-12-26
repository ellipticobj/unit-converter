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
        
        fromunit = input("input unit to convert from \n[meters/kilometers/miles/feet/inches]: ").lower().strip()
        while fromunit not in set(conv["length"].keys()):
            print("invalid unit, please input a proper unit")
            fromunit = input("input unit to convert from \n[meters/kilometers/miles/feet/inches]: ").lower().strip()

        tounit = input("input unit to convert to: \n[meters/kilometers/miles/feet/inches]: ").lover().strip()
        while tounit not in set(conv["length"].keys()):
            print("invalid unit, please input a proper unit")
            tounit = input("input unit to convert from \n[meters/kilometers/miles/feet/inches]: ").lower().strip()
        
        print(f"{val} {fromunit} is {convert(val, fromunit, tounit,"length")} {tounit}")
        
    elif choice == "2":
        fromunit = input("input unit to convert from \n[kilograms/grams/pounds/ounces]: ").lower().strip()
        while fromunit not in set(conv["weight"].keys()):
            print("invalid unit, please input a proper unit")
            fromunit = input("input unit to convert from \n[kilograms/grams/pounds/ounces]: ").lower().strip()

        tounit = input("input unit to convert to: \n[kilograms/grams/pounds/ounces]: ").lover().strip()
        while tounit not in set(conv["weight"].keys()):
            print("invalid unit, please input a proper unit")
            tounit = input("input unit to convert from \n[kilograms/grams/pounds/ounces]: ").lower().strip()
        
        print(f"{val} {fromunit} is {convert(val, fromunit, tounit,"weight")} {tounit}")