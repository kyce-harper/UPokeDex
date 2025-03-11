import requests
import sqlite3

# Define API base URL
base_url = "https://pokeapi.co/api/v2/"

#This method retrives pokeman data and turns it into a python library
def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data {response.status_code}")
        return None

# Connect to SQLite database
connection = sqlite3.connect('pokemon_data.db')
cursor = connection.cursor()

# Create table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS pokemon (
                  id INTEGER PRIMARY KEY,
                  name TEXT UNIQUE,
                  height INTEGER,
                  weight INTEGER)''')
connection.commit()

while True:
    print("𝑼𝑷𝒐𝒌𝒆𝑫𝒆𝒙")
    pokemon_name = input("Enter a Pokémon name (or 'exit' to quit): ").strip() #strip() removes char from string space by default
    if pokemon_name.lower() == 'exit':
        break
    
    #pokemon_info is a dictionary (key, info) of all info recieved from API call
    pokemon_info = get_pokemon_info(pokemon_name)
    if pokemon_info:
        name = pokemon_info["name"].capitalize()
        poke_id = pokemon_info["id"]
        height = pokemon_info["height"]
        weight = pokemon_info["weight"]
        
        print(f"\nName: {name}\nID: {poke_id}\nHeight: {height}\nWeight: {weight}\n")
        print("Added to your Pokedex!")
        
        # Insert data into the database
        try:
            cursor.execute("INSERT INTO pokemon (id, name, height, weight) VALUES (?, ?, ?, ?)",
                           (poke_id, name, height, weight))
            connection.commit()
        except sqlite3.IntegrityError:
            print("Pokémon already exists in the database.")

# Close the database connection
connection.close()
