# Missing_PNR_Detector

This project is used to find all missing PNRs ( Passenger Name Record ) between the two given ones.

## About project

Its bulit in virtual environment (venv) using Python 3.9.7

DB used to store missing PNRs is sqlite3 

## Requirements

There are no requirements for this project, is built with python standard library

## Running code

All code is running in main.py

User needs to input two PNRs ( start - end ).
After entering two PNRs results are saved in pnr.db inside main project directory in table missed_pnrs.

User can choose to read date from table by entering 1, or 2 to close connection to DB.
