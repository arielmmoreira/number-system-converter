from Numbers import *

def main():
    while True:      
        base_from = int(input("Base: (1-Decimal 2-Binary 3-Hexadecimal): "))
        num = str(input("Number: "))

        if base_from == 1:
            number = Decimal(num)
            print(f"Binary: 0b{number.to_binary()}")
            print(f"Hexadecimal: 0x{number.to_hexadecimal()}")

        elif base_from == 2:
            number = Binary(num)
            print(f"Decimal: 0d{number.to_decimal()}")
            print(f"Hexadecimal: 0x{number.to_hexadecimal()}")

        elif base_from == 3:
            number = Hexadecimal(num)
            print(f"Decimal: 0d{number.to_decimal()}")
            print(f"Binary: 0b{number.to_binary()}")
                
        print()

main()