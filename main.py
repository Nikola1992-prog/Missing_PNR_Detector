from pnr.pnr_detector import MissingPnrDetector
from pnr.utils.helper import user_input, read_pnr_db
from pnr.pnr_db import PnrDB


def find_missing_pnrs():
    pnr_start, pnr_end = user_input()

    pnr = MissingPnrDetector(pnr_start, pnr_end)
    pnr.pnr_iterator()

    db = PnrDB()
    db.missing_pnr_to_table(pnr.missed_pnrs)
    if read_pnr_db():
        db.read_data()
    db.close_connection()


if __name__ == "__main__":
    find_missing_pnrs()
