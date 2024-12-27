from logic import *

# TODO: make a gui?

while True:

    choice = input('''1. length
2. weight
3. temperature
4. currency
input [1/2/3/4]: ''').lower().strip()

    if choice == "1":
        print(f"Supported units: {supportedlengths}")
        fromunit = input(f"input unit to convert from: ").lower().strip()
        while fromunit not in supportedlengths:
            print("invalid unit, please input a proper unit")
            fromunit = input("input unit to convert from: ").lower().strip()

        val = getvalfromuser()

        tounit = input("input unit to convert to: ").lower().strip()
        while tounit not in supportedlengths:
            print("invalid unit, please input a proper unit")
            tounit = input("input unit to convert from: ").lower().strip()

        final = convert(val, fromunit, tounit, "length")

    elif choice == "2":
        print(f"Supported units: {supportedweights}")
        fromunit = input("input unit to convert from: ").lower().strip()
        while fromunit not in supportedweights:
            print("invalid unit, please input a proper unit")
            fromunit = input("input unit to convert from: ").lower().strip()

        val = getvalfromuser()

        tounit = input("input unit to convert to: ").lower().strip()
        while tounit not in supportedweights:
            print("invalid unit, please input a proper unit")
            tounit = input("input unit to convert from: ").lower().strip()

        final = convert(val, fromunit, tounit, "weight")

    elif choice == "3":
        print(f"Supported units: {supportedtemps}")
        fromunit = input("input unit to convert from: ").lower().strip()
        while fromunit not in supportedtemps:
            print("invalid unit, please input a proper unit")
            fromunit = input("input unit to convert from: ").lower().strip()

        val = getvalfromuser()

        tounit = input("input unit to convert to: ").lower().strip()
        while tounit not in supportedtemps:
            print("invalid unit, please input a proper unit")
            tounit = input("input unit to convert from: ").lower().strip()

        final = converttemp(val, fromunit, tounit)

    elif choice == "4":
        try:
            supportedcurrs = getavailablecurrencies()
        except Exception as e:
            print()
            print(
                f"error: {e}\n\nDid you put your api key in .env? \nGo to https://app.freecurrencyapi.com/ to make a key"
            )
            print()
            input("Press ENTER to continue")
            continue
        print(f"Supported currencies: {supportedcurrs}")
        fromunit = input("Input currency to cunvert from: ").upper().strip()
        while fromunit not in supportedcurrs:
            print("Please input a proper currency.")
            fromunit = input(
                "Input currency to convert from: ").upper().strip()

        val = getvalfromuser()

        tounit = input("Input currency to cunvert to: ").upper().strip()
        while tounit not in supportedcurrs:
            print("Please input a proper currency.")
            tounit = input("Input currency to convert to: ").upper().strip()

        print()
        print("retrieving data... please wait a moment")
        try:
            final = convertcurr(val, fromunit, tounit)
        except Exception as e:
            print(
                f"error: {e}\nDid you put your api key in .env? Go to https://app.freecurrencyapi.com/to make a key"
            )
    else:
        print()
        print("Please input a valid option")
        print()
        input("Press ENTER to continue ")
        print()
        continue

    print()
    print(f"{val} {fromunit} is {final} {tounit}")
    print()
    input("Press ENTER to continue ")
