from sqlalchemy import text
from sqlalchemy_engine import engine

# Function to fetch data
def fetch_data():
    query = "SELECT * books"  # Replace with your table name

    with engine.connect() as connection:
        result = connection.execute(text(query))

        # Print the results
        for row in result:
            print(row)

# Fetch and display data
fetch_data()
