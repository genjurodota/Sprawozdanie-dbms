import sqlite3
import csv

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('clients.db')
cursor = conn.cursor()

# Create table
def create_table():
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        city TEXT NOT NULL,
        building_number TEXT NOT NULL,
        street TEXT NOT NULL,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        comments TEXT
    )
    ''')
    conn.commit()

# Insert a new client record
def insert_client(city, building_number, street, name, surname, comments):
    cursor.execute('''
    INSERT INTO clients (city, building_number, street, name, surname, comments)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (city, building_number, street, name, surname, comments))
    conn.commit()

# Retrieve all client records
def get_all_clients():
    cursor.execute('SELECT * FROM clients')
    return cursor.fetchall()

# Retrieve a client by ID
def get_client_by_id(client_id):
    cursor.execute('SELECT * FROM clients WHERE id = ?', (client_id,))
    return cursor.fetchone()

# Update a client's information
def update_client(client_id, city, building_number, street, name, surname, comments):
    cursor.execute('''
    UPDATE clients
    SET city = ?, building_number = ?, street = ?, name = ?, surname = ?, comments = ?
    WHERE id = ?
    ''', (city, building_number, street, name, surname, comments, client_id))
    conn.commit()

# Delete a client record
def delete_client(client_id):
    cursor.execute('DELETE FROM clients WHERE id = ?', (client_id,))
    conn.commit()

# Delete data base
def delete_data_base():
    cursor.execute('DROP TABLE clients')

# Generate CSV file from client data
def generate_csv(file_name):
    clients = get_all_clients()
    with open(file_name, 'w', newline='') as csvfile:
        fieldnames = ['id', 'city', 'building_number', 'street', 'name', 'surname', 'comments']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for client in clients:
            writer.writerow({
                'id': client[0],
                'city': client[1],
                'building_number': client[2],
                'street': client[3],
                'name': client[4],
                'surname': client[5],
                'comments': client[6]
            })

# Close the database connection
def close_connection():
    conn.close()

# Function to input data from console
def input_client_data():
    city = input("Enter city: ")
    building_number = input("Enter building number: ")
    street = input("Enter street: ")
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    comments = input("Enter comments: ")
    insert_client(city, building_number, street, name, surname, comments)


# Example usage
if __name__ == "__main__":
    create_table()

    while True:
        print("\nOptions:")
        print("1. Insert a new client")
        print("2. View all clients")
        print("3. View a client by ID")
        print("4. Update a client")
        print("5. Delete a client")
        print("6. Generate CSV")
        print("7. Erase data base")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            input_client_data()
        elif choice == '2':
            clients = get_all_clients()
            for client in clients:
                print(client)
        elif choice == '3':
            client_id = int(input("Enter client ID: "))
            client = get_client_by_id(client_id)
            if client:
                print(client)
            else:
                print("Client not found.")
        elif choice == '4':
            client_id = int(input("Enter client ID to update: "))
            city = input("Enter new city: ")
            building_number = input("Enter new building number: ")
            street = input("Enter new street: ")
            name = input("Enter new name: ")
            surname = input("Enter new surname: ")
            comments = input("Enter new comments: ")
            update_client(client_id, city, building_number, street, name, surname, comments)
        elif choice == '5':
            client_id = int(input("Enter client ID to delete: "))
            delete_client(client_id)
        elif choice == '6':
            file_name = input("Enter CSV file name (e.g., clients.csv): ")
            generate_csv(file_name)
            print(f"CSV file '{file_name}' generated.")
        elif choice == '7':
            delete_data_base()
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

    close_connection()