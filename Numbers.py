class Number():
    def __init__(self, value):
        self.value = value

    def num_digits(self, num, base):
        """
        input: int
        returns number of digits to target number base
        """

        digit = 0
        i = 0

        if base == "bin":
            while True:
                digit = 2 ** i
                if digit > num:
                    return i
                i += 1

        elif base == "hex":
            while True:
                digit = 16 ** i
                if digit > num:
                    return i
                i += 1


class Decimal(Number):
    def __init__(self, value):
        super().__init__(value)
        self.base = "dec"
        self.binary = None
        self.hexadecimal = None

    def to_binary(self):
        number = int(self.value)
        num_len = self.num_digits(number, "bin")
        binary = ""

        for exponent in range(num_len - 1, -1, -1):
            bit = 2 ** exponent
            if number >= bit:
                number -= bit
                binary += '1'
            else:
                binary += '0'

        self.binary = binary
        return binary

    def to_hexadecimal(self):
        number = int(self.value)
        hexadecimals = ['a', 'b', 'c', 'd', 'e', 'f']
        num_len = self.num_digits(number, "hex")
        hexadecimal = ""
        
        for exponent in range(num_len - 1, -1, -1):
            digit = 16 ** exponent
            equation = number // digit
            if equation > 9:
                hexadecimal += hexadecimals[equation % 10]
            else:
                hexadecimal += str(equation)
            number -= equation * digit

        self.hexadecimal = hexadecimal
        return hexadecimal
    
    def __str__(self):
        return f"0d{self.value}"

class Hexadecimal(Number):
    def __init__(self, value):
        super().__init__(value)
        self.base = "hex"
        self.decimal = None
        self.binary = None

    def to_decimal(self):
        hexadecimals = ['a', 'b', 'c', 'd', 'e', 'f']
        decimal = 0

        for i in range(len(self.value)):
            if self.value[i] in hexadecimals:
                decimal += (hexadecimals.index(self.value[i]) + 10) * (16 ** (len(self.value) - i - 1))
            else:
                decimal += int(self.value[i]) * (16 ** (len(self.value) - i - 1))

        self.decimal = decimal
        return decimal

    def to_binary(self):
        decimal = Decimal(self.to_decimal())
        binary = decimal.to_binary()
        self.binary = binary
        return binary

    def __str__(self):
        return f"0x{self.value}"

class Binary(Number):
    def __init__(self, value):
        super().__init__(value)
        self.base = "bin"
        self.decimal = None
        self.hexadecimal = None

    def to_decimal(self):
        number = str(self.value)[::-1]
        num_len = len(number)
        decimal = 0
        for i in range(num_len -1, -1, -1):
            equation = int(number[i]) * (2 ** i)
            decimal += equation

        self.decimal = decimal
        return decimal

    def to_hexadecimal(self):
        decimal = Decimal(self.to_decimal())
        hexadecimal = decimal.to_hexadecimal()
        self.hexadecimal = hexadecimal

        return hexadecimal

    def __str__(self):
        return f"0b{self.value}"
