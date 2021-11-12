import sqlite3


class PnrDB:
    db_path = './pnr.db'

    def __init__(self):
        self.connection = sqlite3.connect(self.db_path)
        self.cursor = self.connection.cursor()

    def missing_pnr_to_table(self, data):
        """
            Inserts missed prn to DB (pnr.db) into table missed_pnrs
            :param data: lists of 6 char symbols
        """
        drop_table = '''DROP TABLE IF EXISTS missed_pnrs'''
        self.cursor.execute(drop_table)

        create_table = '''CREATE TABLE  missed_pnrs(
                                                    pnr_id INTEGER PRIMARY KEY,
                                                    pnr varchar(6)
                                                );'''
        self.cursor.execute(create_table)

        table_insert = '''INSERT INTO missed_pnrs (pnr) VALUES(?)'''

        for _ in data:
            self.cursor.execute(table_insert, [''.join(_)])
        self.connection.commit()
        print('\nMissed PNRs are added to DB table "missed_pnrs"\n')

    def read_data(self):
        read = '''SELECT * FROM missed_pnrs'''
        data = self.cursor.execute(read)
        print('\tID\t\tPNR')
        for pnr_id, pnr in data.fetchall():
            print(f'\t{pnr_id}\t\t{pnr}')

    def close_connection(self):
        self.connection.close()
