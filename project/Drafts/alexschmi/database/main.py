from database import Database

# Creating the database
db = Database()     # Instantiate the Database class
db.createTables()   # Create all tables
db.insertSeat()     # Initialize seat indexes

# Inserting into the database - examples
db.insertUser("max", "mustermann", "maxmustermann", "max@mustermann.com", "12345")
db.insertSeatType("economy", "1.00 €")
db.insertReservation("4A", "1", "max", "mustermann", "date")

# Reading/getting information from the database
print(db.readUser())
print(db.readReservation())



