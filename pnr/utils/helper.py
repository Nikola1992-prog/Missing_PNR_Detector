from pnr.pnr_detector import numbers_and_letters


def more_than_six_symbols(serial):
    if len(serial) != 6:
        return True
    return False


def one_to_z(serial):
    for _ in serial:
        if _ not in numbers_and_letters:
            return False
    return True


def equal(serial_start, serial_end):
    if serial_start == serial_end:
        return True
    return False


def second_is_bigger(serial_start, serial_end):
    first_num = None
    second_num = None
    for _ in range(0, 6):
        if serial_start[_] != serial_end[_]:  # first != symbols in same (serial_start - serial_end) column
            first_num = serial_start[_]
            second_num = serial_end[_]
            break
    if first_num > second_num:
        return True
    return False


def user_input():
    while True:
        try:
            first_serial = list(input('Please enter first PNR: ').upper())
            if more_than_six_symbols(first_serial):
                print('Please use 6 PNR symbols')
                continue
            if not one_to_z(first_serial):
                print('Please use 1 to Z symbols')
                continue

            second_serial = list(input('Please enter second PNR: ').upper())
            if more_than_six_symbols(second_serial):
                print('Please use 6 PNR symbols')
                continue
            if not one_to_z(first_serial):
                print('Please use 1 to Z symbols')
                continue

            if equal(first_serial, second_serial):
                print('Please dont use the same PNRs ')
                continue
            if second_is_bigger(first_serial, second_serial):
                print('First PNR must be smaller than second one')
                continue

            return first_serial, second_serial
        except (TypeError, ValueError) as e:
            print(e, '\n')


def read_pnr_db():
    while True:
        try:
            answer = int(input(
                "Please enter 1 for printing data from table \"missed_pnrs\", or 2 for closing connection with DB: "))
            if answer not in [1, 2]:
                continue
            return True if answer == 1 else False
        except TypeError as e:
            print(e, '\n')
