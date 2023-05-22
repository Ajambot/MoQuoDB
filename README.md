# Movie and TV Series Quotes Database CLI (MoQuoDB)

Welcome to the Movie and TV Series Quotes Database Command Line Interface (CLI) repository! This project provides a simple command line interface to perform CRUD (Create, Read, Update, Delete) operations on a local database of movie and TV series quotes. With this CLI, you can easily manage and interact with your collection of memorable quotes from your favorite movies and TV shows.

## Features
- **Create**: Add new movies/tv shows by providing their IMDB IDs. The program will then web scrape the relevant information from the IMDB website to make inserting to the database simpler. Also, add quotes to the database by providing the information required
- **Read**: View all the quotes in the database, search for quotes by movie or TV show title, or filter by other fields like character name, etc.
- **Update**: Modify existing quotes and works in the database by providing their IDs, allowing you to correct any errors or update the quote itself.
- **Delete**: Remove quotes and movies from the database that are no longer needed or have been entered incorrectly.

## Schema

The schema for the database allows for simple, yet relevant storage of data related to the cinematographic works and quotes in the database.

### Table 1: Works
Fields:
- "work_id" Primary key: represents the IMDB ID of the work
- "title": title of the work
- "director": director of the work
- "year": year of release of the work
- "genre_1", "genre_2", "genre_3": genres of the work

### Table 2: Quotes
Fields:
- "quote_id" Primary key: autoincrementing id of the quotes
- "quote"
- "character": character that said the quote
- "season"
- "episode"
- "timestamp": timestamp where the quote is said
- "work_id" Foreign key: referemces a work_id in the **Works** table

## Prerequisites

To run this project, you need to have the following prerequisites installed:

- Python 3.x: Make sure you have Python 3.x installed on your system.

## Getting Started

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/Ajambot/MoQuoDB.git
   ```

2. Navigate to the project directory:

   ```
   cd MoQuoDB
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Set up the database:

   - Create a new database with your preferred SQL DBMS (I personally use SQL Server 2022) named `MoQuoDB.db`.
   - Use the provided SQL schema file `schema.sql` to create the necessary tables and schema for the database.

5. Create a configuration file named config.py in the following format:
   ```
   db = {
    "server" : "Path/To/Server",
    "dbName" : "MoQuoDB",
    "username" : "yourUserName",
    "password" : "yourPassword"
   }
   ```

5. Run the CLI:

   ```
   python Main.py
   ```

## Usage

Once you have the CLI up and running, you can follow the instructions in the menu to perform the required operations.

## Contributions

Contributions to this project are welcome! If you have any ideas, bug fixes, or improvements, feel free to submit a pull request.

## Contact

If you have any questions, suggestions, or feedback, please feel free to reach me at [mmorale5@lakeheadu.ca](mailto:mmorale5@lakeheadu.ca).

Happy quoting!
