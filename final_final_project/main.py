from website.__init__ import create_app
from website.database import Database

# Creating the database
db = Database()     # Instantiate the Database class
db.create_tables()  # Create all tables
db.insert_seat()     # Initialize seat indexes

# -----

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
