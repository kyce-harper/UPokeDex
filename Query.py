import sqlite3

# Connect to SQLite database
connection = sqlite3.connect('pokemon_data.db')
cursor = connection.cursor()

def get_all_pokemon():
    """Retrieve all Pokémon stored in the database."""
    cursor.execute("SELECT * FROM pokemon")
    results = cursor.fetchall()
    if results:
        for pokemon in results:
            print(f"ID: {pokemon[0]}, Name: {pokemon[1]}, Height: {pokemon[2]}, Weight: {pokemon[3]}")
    else:
        print("No Pokémon found in the database.")

def search_pokemon(name):
    """Retrieve a Pokémon by its name."""
    cursor.execute("SELECT * FROM pokemon WHERE name = ?", (name.capitalize(),))
    result = cursor.fetchone()
    if result:
        print(f"ID: {result[0]}, Name: {result[1]}, Height: {result[2]}, Weight: {result[3]}")
    else:
        print(f"No Pokémon named {name} found.")

def sort_pokemon_by(column):
    """Sort Pokémon by height or weight."""
    if column not in ["height", "weight"]:
        print("Invalid sorting option. Choose 'height' or 'weight'.")
        return
    cursor.execute(f"SELECT * FROM pokemon ORDER BY {column} ASC")
    results = cursor.fetchall()
    for pokemon in results:
        print(f"ID: {pokemon[0]}, Name: {pokemon[1]}, {column.capitalize()}: {pokemon[2 if column == 'height' else 3]}")

while True:
    print("𝑼𝑷𝒐𝒌𝒆𝑫𝒆𝒙")
    print("\nOptions:")
    print("1. View all Pokémon")
    print("2. Search for a Pokémon")
    print("3. Sort Pokémon by height")
    print("4. Sort Pokémon by weight")
    print("5. Exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        get_all_pokemon()
    elif choice == "2":
        name = input("Enter Pokémon name: ").strip()
        search_pokemon(name)
    elif choice == "3":
        sort_pokemon_by("height")
    elif choice == "4":
        sort_pokemon_by("weight")
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")

# Close the database connection
connection.close()