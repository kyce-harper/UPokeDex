# UPokeDex: Learning SQLite and API Integration

## About This Project
This project is my first time working with an SQLite database while interacting with an external API. Using the [PokéAPI](https://pokeapi.co/), I built a simple Pokémon database that allows users to search for Pokémon, store them locally, and retrieve or sort the stored data.

## What I Learned
- **API Requests & JSON Handling**: I learned how to fetch data from an external API using the `requests` library and process JSON responses.
- **SQLite Database Basics**: I created and managed an SQLite database to store Pokémon details, learning about table creation, inserting data, and handling constraints (e.g., preventing duplicate entries).
- **Handling User Input & Errors**: I implemented user input handling, error checking, and exception handling for database constraints and API failures.
- **Basic Querying & Sorting**: I wrote SQL queries to retrieve and sort Pokémon data by different attributes.

## New Development Approach
Previously, I would code everything and then commit all changes at once. However, moving forward, I will **live update my coding process**. This means:
- Committing incremental changes with meaningful messages.
- Adding notes and documentation throughout development.
- Keeping track of issues and fixes as I go.

I hope this approach will improve transparency, clarity, and maintainability in my projects.

## Features
- Fetch Pokémon data using the PokéAPI.
- Store Pokémon details in an SQLite database.
- Retrieve all stored Pokémon.
- Search for a Pokémon by name.
- Sort Pokémon by height or weight.
- Prevent duplicate entries in the database.

## How to Use
1. Install dependencies: `pip install requests sqlite3`
2. Run the script: `python upokedex.py`
3. Follow the on-screen options to interact with the database.

## Future Improvements
- Add more Pokémon details (types, abilities, base stats).
- Implement a GUI for better user experience.
- Enable exporting the Pokémon list as a CSV file.

---
This project was a great learning experience, and I look forward to refining it as I go!


