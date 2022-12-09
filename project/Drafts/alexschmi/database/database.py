import sqlite3
import numpy as np
from datetime import datetime

class Database:
    def __init__(self):
        self.connection = sqlite3.connect("asr.db")  # Creates database
        self.cursor = self.connection.cursor()    # To communicate/interact with the database
        self.seats = np.genfromtxt("chartIn.txt", skip_header=1, dtype="str")   # Generates array from chartIn.txt

    # Creates all tables
    def createTables(self):
        # Creates user table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tbl_user(
            user_ID INTEGER PRIMARY KEY,
            name TEXT,
            surname TEXT,
            username TEXT UNIQUE,
            email TEXT UNIQUE,
            password TEXT
            )""")

        # Creates seat table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tbl_seat(
            seat_ID TEXT PRIMARY KEY,
            seatType_ID INTEGER,
            FOREIGN KEY (seatType_ID) REFERENCES tbl_seatType(seatType_ID)
            )""")

        # Creates seat_type table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tbl_seatType(
            seatType_ID INTEGER PRIMARY KEY,
            seatType TEXT,
            price TEXT
            )""")

        # Creates reservation table
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS tbl_reservation(
            reservation_ID INTEGER PRIMARY KEY,
            seat_ID TEXT UNIQUE,
            user_ID INTEGER,
            passengerName TEXT,
            passengerSurname TEXT,
            date DATE,
            FOREIGN KEY (seat_ID) REFERENCES tbl_seat(seat_ID)
            FOREIGN KEY (user_ID) REFERENCES tbl_user(user_ID)
            )""")

    # Creates the seat indexes from chartIn.txt and inserts them into tbl_seat
    def insertSeat(self):
        self.seats = np.delete(self.seats, 0, axis=1)   # Deletes first column of chartIn.txt since it is not needed for creating the seat indexes

        for i in range(1, self.seats.shape[0]+1):   # Goes through columns numbers
            for j in self.seats[0, :]:  # Goes through row letters
                index = str(i) + str(j)     # The seat index is combination of column number and row letter

                # Inserts the created index into seat_ID from tbl_seat
                # And inserts 1 into seat_type_ID by default
                self.cursor.execute("""INSERT OR IGNORE INTO tbl_seat (seat_ID, seatType_ID) VALUES(?,?)""", (index, 1))
                self.connection.commit()

    # Inserts user information into tbl_user
    def insertUser(self, name, surname, username, email, password):
        self.cursor.execute("""INSERT OR IGNORE INTO tbl_user (name, surname, username, email, password) VALUES(?,?,?,?,?)""", (name, surname, username, email, password))
        self.connection.commit()

    # Inserts seatType information into tbl_seatType
    def insertSeatType(self, seatType, price):
        self.cursor.execute("""INSERT OR IGNORE INTO tbl_seatType (seatType, price) VALUES(?,?)""", (seatType, price))
        self.connection.commit()

    # Inserts reservation information into tbl_reservation
    def insertReservation(self, seat_ID, user_ID, passengerName, passengerSurname, date):
        self.cursor.execute("""INSERT OR IGNORE INTO tbl_reservation (seat_ID, user_ID, passengerName, passengerSurname, date) VALUES(?,?,?,?,?)""", (seat_ID, user_ID, passengerName, passengerSurname, datetime.today().strftime("%d.%m.%y")))
        self.connection.commit()

    # Query template to get user data from tbl_user
    def readUser(self):
        self.cursor.execute("""SELECT * FROM tbl_user""")
        rows = self.cursor.fetchall()
        return rows

    # Query template to get reservation and user data from the two tables tbl_reservation and tbl_user
    def readReservation(self):
        self.cursor.execute("""SELECT seat_ID, username, passengerName, passengerSurname FROM tbl_reservation INNER JOIN tbl_user ON tbl_reservation.user_ID = tbl_user.user_ID""")
        rows = self.cursor.fetchall()
        return rows
