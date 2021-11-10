import string


class MissingPnrDetector:
    missed_pnrs = []

    def __init__(self, serial_start=None, serial_end=None):
        """
        :param serial_start: list of 6 char symbols 1 to Z
        :param serial_end: list of 6 char symbols 1 to Z
        """

        if serial_start is None:
            serial_start = ['A', 'A', 'A', 'A', 'A', 'A']
        self.serial_start = serial_start

        if serial_end is None:
            serial_end = ['A', 'A', 'A', 'A', 'A', 'D']
        self.serial_end = serial_end

        self.index_symbol = dict()
        self.pattern()

        self.serial_start_digits = []
        self.converting_serial_begin_symbols_to_digits()

    def pattern(self):
        """
            For every symbol value in (serial_begin), there is key index
            example 1: { 0 : '1'}
            example 2: { 9 : 'A'}
            example 3: { 34 : 'Z'}

            Last key - value acts as EOF or (None - value)
            example : { 35 : None }
        """
        numbers_letters_combined = [str(num) for num in range(1, 10)] + (list(string.ascii_uppercase))
        for index, symbol in enumerate(numbers_letters_combined):
            self.index_symbol[index] = symbol
        else:
            self.index_symbol.update({35: None})

    def converting_serial_begin_symbols_to_digits(self):
        """
            Converting every (serial_begin) entry param symbols (1 to Z) into digits (1 to 34)
            example 1: ['A', 'A', 'A', 'A', 'A', 'Z']  ->  [9, 9, 9, 9, 9, 34]
            example 2: ['A', 'A', 'A', 'A', 'A', '1']  ->  [9, 9, 9, 9, 9, 0]
            example 3: ['A', 'A', 'A', 'A', 'B', 'A']  ->  [9, 9, 9, 9, 10, 9]
        """
        for _ in self.serial_start:
            for index, value in self.index_symbol.items():
                if _ == value:
                    self.serial_start_digits.append(index)

    def serial_iterator(self):
        """
            symbols = ['symbol1', 'symbol2', 'symbol3', 'symbol4', 'symbol5', 'symbol6']

            iterating trow all six symbols and incrementing each column after every circle

        """

        symbol6 = self.serial_start_digits[5]
        symbol5 = self.serial_start_digits[4]
        symbol4 = self.serial_start_digits[3]
        symbol3 = self.serial_start_digits[2]
        symbol2 = self.serial_start_digits[1]
        symbol1 = self.serial_start_digits[0]

        while True:
            if symbol6 <= 34:
                symbol6 += 1

            if symbol6 == 35:
                symbol6 = 0
                symbol5 += 1

            if symbol5 == 35:
                symbol5 = 0
                symbol4 += 1

            if symbol4 == 35:
                symbol4 = 0
                symbol3 += 1

            if symbol3 == 35:
                symbol3 = 0
                symbol2 += 1

            if symbol2 == 35:
                symbol2 = 0
                symbol1 += 1

            if symbol1 == 35:
                symbol1 = 0

            serial_numeric_begin = [self.index_symbol[symbol1],
                                    self.index_symbol[symbol2],
                                    self.index_symbol[symbol3],
                                    self.index_symbol[symbol4],
                                    self.index_symbol[symbol5],
                                    self.index_symbol[symbol6]]

            if serial_numeric_begin == self.serial_end:
                break
            else:
                # print(serial_numeric_begin)
                self.missed_pnrs.append(serial_numeric_begin)
