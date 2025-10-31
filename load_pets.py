import sqlite3

# Connect to the database
conn = sqlite3.connect('pet.db')
cursor = conn.cursor()


# Person data to insert
person_data = [
    (1, 'James', 'Smith', 41),
    (2, 'Diana', 'Greene', 23,),
    (3, 'Sara', 'White', 27),
    (4, 'William', 'Gibson', 23)
]

cursor.executemany("INSERT INTO person VALUES (?, ?, ?, ?)", person_data)

# Pet data to insert
pet_data = [
    (1, 'Rusty', 'Dalmation', 4, 1),
    (2, 'Bella', 'Alaskan Malamute', 3, 0),
    (3, 'Max', 'Cocker Spaniel', 1, 0),
    (4, 'Rocky', 'Beagle', 7, 0),
    (5, 'Rufus', 'Cocker Spaniel', 1, 0),
    (6, 'Spot', 'Bloodhound', 2, 1)
]

cursor.executemany("INSERT INTO pet VALUES (?, ?, ?, ?, ?)", pet_data)

# person_pet data to insert
## This table is a junction table, used to associate the people with their pets
person_pet = [
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6),
]

cursor.executemany("INSERT INTO person_pet VALUES (?, ?)", person_pet)

conn.commit()
conn.close()

if __name__ == "__main__":
    print("Running load_pets.py")
