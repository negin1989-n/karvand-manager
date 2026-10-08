import json
import os

DATA_DIR = "data"
DATA_FILE = "data/karvands.json"


def load_data():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    if not os.path.exists(DATA_FILE):
        data = {
            "bootcamp": {
                "name": "Karvand Bootcamp"
            },
            "karvands": []
        }

        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        return data

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):
        data = {
            "bootcamp": {
                "name": "Karvand Bootcamp"
            },
            "karvands": []
        }

        with open(DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        return data


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def add_karvand(data):
    print("\n--- Add Karvand ---")

    name = input("Full name: ")
    email = input("Email: ")
    city = input("City: ")
    degree = input("Education degree: ")
    field = input("Education field: ")
    skill_name = input("Skill name: ")
    skill_level = input("Skill level: ")

    while True:
        try:
            score = int(input("Skill score (0-100): "))

            if 0 <= score <= 100:
                break

            print("Score must be between 0 and 100.")

        except ValueError:
            print("Please enter a number.")

    if data["karvands"]:
        new_id = max(k["id"] for k in data["karvands"]) + 1
    else:
        new_id = 1

    karvand = {
        "id": new_id,
        "name": name,
        "email": email,
        "city": city,
        "education": {
            "degree": degree,
            "field": field
        },
        "skills": [
            {
                "name": skill_name,
                "level": skill_level,
                "score": score
            }
        ]
    }

    data["karvands"].append(karvand)

    save_data(data)

    print(f"Karvand added successfully. ID: {new_id}")


def main():
    data = load_data()

    add_karvand(data)


if __name__ == "__main__":
    main()