import string

numbers_and_letters = [str(num) for num in range(1, 10)] + (list(string.ascii_uppercase))


class MissingPnrDetector:
    missed_pnrs = []

    def __init__(self, pnr_start, pnr_end):
        """
            :param pnr_start: list of 6 char symbols 1 to Z
            :param pnr_end: list of 6 char symbols 1 to Z

            NAME:
                MissingPnrDetector

            DESCRIPTION:
                Finding all missing PNR ( Passenger Name Record ) serial numbers
                between two serials (PNRs)

            PACKAGE CONTENTS:
                define_index_symbol_pattern - defining dict key ( 1 - 34 ) -> value ( 1 - Z) pars
                converting_pnr_start_symbols_to_digits
                pnr_iterator
        """
        self.pnr_start = pnr_start
        self.pnr_end = pnr_end

        self.index_PnrSymbol = dict()
        self.define_index_symbol_pattern()

        self.pnr_start_digits = []
        self.converting_pnr_start_symbols_to_digits()

    def define_index_symbol_pattern(self):
        """
            For every symbol in (pnr_start), there is key index
            example 1: { 0 : '1'}
            example 2: { 9 : 'A'}
            example 3: { 34 : 'Z'}
        """

        for index, symbol in enumerate(numbers_and_letters):
            self.index_PnrSymbol[index] = symbol
        else:
            # Last key - value acts as EOF or (None - value)
            self.index_PnrSymbol.update({35: None})

    def converting_pnr_start_symbols_to_digits(self):
        """
            Converting every (pnr_start) symbol (1 to Z) into digits (1 to 34)
            example 1: ['A', 'A', 'A', 'A', 'A', 'Z']  ->  [9, 9, 9, 9, 9, 34]
            example 2: ['A', 'A', 'A', 'A', 'A', '1']  ->  [9, 9, 9, 9, 9, 0]
            example 3: ['A', 'A', 'A', 'A', 'B', 'A']  ->  [9, 9, 9, 9, 10, 9]
        """
        for _ in self.pnr_start:
            for index, symbol in self.index_PnrSymbol.items():
                if _ == symbol:
                    self.pnr_start_digits.append(index)

    def pnr_iterator(self):
        """
            iterating trow all six symbols-digits and incrementing each column after every circle
        """

        # PNR =     ['symbol1', 'symbol2', 'symbol3', 'symbol4', 'symbol5', 'symbol6']
        # example = [   9     ,    9     ,    9     ,    9     ,    9     ,    9     ]

        symbol6 = self.pnr_start_digits[5]
        symbol5 = self.pnr_start_digits[4]
        symbol4 = self.pnr_start_digits[3]
        symbol3 = self.pnr_start_digits[2]
        symbol2 = self.pnr_start_digits[1]
        symbol1 = self.pnr_start_digits[0]

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

            incremented_pnr = [self.index_PnrSymbol[symbol1],
                               self.index_PnrSymbol[symbol2],
                               self.index_PnrSymbol[symbol3],
                               self.index_PnrSymbol[symbol4],
                               self.index_PnrSymbol[symbol5],
                               self.index_PnrSymbol[symbol6]]

            if incremented_pnr == self.pnr_end:
                break
            else:
                # print(serial_to_increment)
                self.missed_pnrs.append(incremented_pnr)
