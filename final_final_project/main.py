from website import create_app
from website.database import Database

# Creating the database
db = Database()     # Instantiate the Database class
db.create_tables()  # Create all tables
db.insert_seat()     # Initialize seat indexes

# Inserting into the database - examples
db.insert_user("max", "mustermann", "maxmustermann", "max@mustermann.com", "12345")
db.insert_seat_type("economy", "1.00 €")
db.insert_reservation("4A", "1", "max", "mustermann", "date")

# Reading/getting information from the database
#print(db.read_user())
#print(db.read_reservation())
print(db.read_login("max@mustermann.com"))

# ----------

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
