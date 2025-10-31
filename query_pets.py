import sqlite3

import sqlite3


def query_person_and_pet(person_id):
    conn = sqlite3.connect('pet.db')
    cursor = conn.cursor()

    # Query for person
    cursor.execute("SELECT first_name, last_name, age FROM person WHERE id = ?", (person_id,))
    person = cursor.fetchone()

    if person is None:
        print("Error: Person not found")
        conn.close()
        return

    first_name, last_name, age = person
    print(f"{first_name} {last_name}, {age} years old")

    # Query for pet
    cursor.execute("""
        SELECT pet.name, pet.breed, pet.age, pet.dead
        FROM pet
        JOIN person_pet ON pet.id = person_pet.pet_id
        WHERE person_pet.person_id = ?
    """, (person_id,))

    pet = cursor.fetchall()

    for pet_name, breed, pet_age, dead in pet:
        status = "was" if dead else "is"
        print(f"{first_name} {last_name} owned {pet_name}, a {breed}, that {status} {pet_age} years old")

    conn.close()

# Main program loop
while True:
    try:
        person_id = int(input("Enter a person's ID number (-1 to exit): "))

        if person_id == -1:
            print("Exiting program...")
            break

        query_person_and_pet(person_id)
        print()  # Blank line for readability

    except ValueError:
        print("Error: Please enter a valid number")

if __name__ == "__main__":
    print("Running query_pet.py")
