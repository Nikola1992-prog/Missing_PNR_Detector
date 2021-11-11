from pnr.pnr_detector import MissingPnrDetector
from pnr.utils.helper import user_input


def find_missing_pnrs():
    pnr1, pnr2 = user_input()
    pnr = MissingPnrDetector(pnr1, pnr2)
    pnr.pnr_iterator()


if __name__ == "__main__":
    find_missing_pnrs()
