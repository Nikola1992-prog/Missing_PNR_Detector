import unittest
from pnr.pnr_detector import MissingPnrDetector


class TestPnrSerials(unittest.TestCase):
    #                   start_pnr                       end_pnr
    cases = [[['A', 'A', 'A', 'Z', 'Z', 'Z'], ['A', 'A', 'B', '1', '1', '2']],
             [['A', 'A', 'A', 'A', 'Z', 'Z'], ['A', 'A', 'A', 'B', '1', '2']],
             [['A', 'A', 'A', 'A', 'Z', 'Z'], ['A', 'A', 'A', 'B', '2', '2']],
             [['A', 'A', 'A', 'A', 'A', 'A'], ['A', 'A', 'A', 'A', 'A', 'B']],
             [['1', '1', '1', '1', '1', '1'], ['1', '1', '1', '1', '1', '3']]]

    def test_all_cases(self):
        result1 = [['A', 'A', 'B', '1', '1', '1']]

        result2 = [['A', 'A', 'A', 'B', '1', '1']]

        result3 = [['A', 'A', 'A', 'B', '1', '1'],
                   ['A', 'A', 'A', 'B', '1', '2'],
                   ['A', 'A', 'A', 'B', '1', '3'],
                   ['A', 'A', 'A', 'B', '1', '4'],
                   ['A', 'A', 'A', 'B', '1', '5'],
                   ['A', 'A', 'A', 'B', '1', '6'],
                   ['A', 'A', 'A', 'B', '1', '7'],
                   ['A', 'A', 'A', 'B', '1', '8'],
                   ['A', 'A', 'A', 'B', '1', '9'],
                   ['A', 'A', 'A', 'B', '1', 'A'],
                   ['A', 'A', 'A', 'B', '1', 'B'],
                   ['A', 'A', 'A', 'B', '1', 'C'],
                   ['A', 'A', 'A', 'B', '1', 'D'],
                   ['A', 'A', 'A', 'B', '1', 'E'],
                   ['A', 'A', 'A', 'B', '1', 'F'],
                   ['A', 'A', 'A', 'B', '1', 'G'],
                   ['A', 'A', 'A', 'B', '1', 'H'],
                   ['A', 'A', 'A', 'B', '1', 'I'],
                   ['A', 'A', 'A', 'B', '1', 'J'],
                   ['A', 'A', 'A', 'B', '1', 'K'],
                   ['A', 'A', 'A', 'B', '1', 'L'],
                   ['A', 'A', 'A', 'B', '1', 'M'],
                   ['A', 'A', 'A', 'B', '1', 'N'],
                   ['A', 'A', 'A', 'B', '1', 'O'],
                   ['A', 'A', 'A', 'B', '1', 'P'],
                   ['A', 'A', 'A', 'B', '1', 'Q'],
                   ['A', 'A', 'A', 'B', '1', 'R'],
                   ['A', 'A', 'A', 'B', '1', 'S'],
                   ['A', 'A', 'A', 'B', '1', 'T'],
                   ['A', 'A', 'A', 'B', '1', 'U'],
                   ['A', 'A', 'A', 'B', '1', 'V'],
                   ['A', 'A', 'A', 'B', '1', 'W'],
                   ['A', 'A', 'A', 'B', '1', 'X'],
                   ['A', 'A', 'A', 'B', '1', 'Y'],
                   ['A', 'A', 'A', 'B', '1', 'Z'],
                   ['A', 'A', 'A', 'B', '2', '1']]

        result4 = [[]]

        result5 = [['1', '1', '1', '1', '1', '2']]

        results = [result1, result2, result3, result4, result5]

        for case in self.cases:
            serial_input = MissingPnrDetector(case[0], case[1])
            for index, miss_pnr in enumerate(serial_input.missed_pnrs):
                self.assertListEqual(miss_pnr, results[index])


if __name__ == "__main__":
    unittest.main()
