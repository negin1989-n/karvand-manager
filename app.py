
import json
import os

DATA_DIR = "data"
DATA_FILE = "data/karvands.json"
REPORT_FILE = "data/report.json"


def load_data():
    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(DATA_FILE):
        data = {
            "bootcamp": {"name": "Karvand Bootcamp"},
            "karvands": []
        }
        save_data(data)
        return data

    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict) or not isinstance(data.get("karvands"), list):
            raise ValueError("Invalid data format.")

        return data

    except (json.JSONDecodeError, FileNotFoundError, ValueError):
        data = {
            "bootcamp": {"name": "Karvand Bootcamp"},
            "karvands": []
        }
        save_data(data)
        return data


def save_data(data):
    os.makedirs(DATA_DIR, exist_ok=True)

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def add_karvand(data):
    print("\n--- Add Karvand ---")

    name = input("Full name: ").strip()
    email = input("Email: ").strip()
    city = input("City: ").strip()
    degree = input("Education degree: ").strip()
    field = input("Education field: ").strip()
    skill_name = input("Skill name: ").strip()
    skill_level = input("Skill level: ").strip()

    while True:
        try:
            score = int(input("Skill score (0-100): "))
            if 0 <= score <= 100:
                break
            print("Score must be between 0 and 100.")
        except ValueError:
            print("Please enter a valid number.")

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


def show_karvands(data):
    print("\n--- All Karvands ---")

    if not data["karvands"]:
        print("No karvands found.")
        return

    for karvand in data["karvands"]:
        print(f"\nID: {karvand['id']}")
        print(f"Name: {karvand['name']}")
        print(f"Email: {karvand['email']}")
        print(f"City: {karvand['city']}")
        print(f"Education: {karvand['education']['degree']}")
        print(f"Field: {karvand['education']['field']}")
        print("Skills:")

        for skill in karvand["skills"]:
            print(
                f"  - {skill['name']} | "
                f"Level: {skill['level']} | "
                f"Score: {skill['score']}"
            )


def search_karvand(data):
    print("\n--- Search Karvand ---")
    keyword = input("Enter name or email: ").strip().lower()

    if not keyword:
        print("Search keyword cannot be empty.")
        return

    found = False

    for karvand in data["karvands"]:
        if (
            keyword in karvand["name"].lower()
            or keyword in karvand["email"].lower()
        ):
            print(f"\nID: {karvand['id']}")
            print(f"Name: {karvand['name']}")
            print(f"Email: {karvand['email']}")
            print(f"City: {karvand['city']}")
            print(f"Education: {karvand['education']['degree']}")
            print(f"Field: {karvand['education']['field']}")

            for skill in karvand["skills"]:
                print(
                    f"Skill: {skill['name']} | "
                    f"Level: {skill['level']} | "
                    f"Score: {skill['score']}"
                )

            found = True

    if not found:
        print("No karvand found.")


def delete_karvand(data):
    print("\n--- Delete Karvand ---")

    try:
        karvand_id = int(input("Enter Karvand ID: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    for karvand in data["karvands"]:
        if karvand["id"] == karvand_id:
            data["karvands"].remove(karvand)
            save_data(data)
            print("Karvand deleted successfully.")
            return

    print("Karvand not found.")


def edit_karvand(data):
    print("\n--- Edit Karvand ---")

    try:
        karvand_id = int(input("Enter Karvand ID: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    karvand = None

    for item in data["karvands"]:
        if item["id"] == karvand_id:
            karvand = item
            break

    if karvand is None:
        print("Karvand not found.")
        return

    print("\nSelect the information you want to edit:")
    print("1. Name")
    print("2. Email")
    print("3. City")
    print("4. Education degree")
    print("5. Education field")
    print("6. Skill name")
    print("7. Skill level")
    print("8. Skill score")

    choice = input("Choose an option: ")

    if choice == "1":
        karvand["name"] = input("Enter new name: ").strip()

    elif choice == "2":
        karvand["email"] = input("Enter new email: ").strip()

    elif choice == "3":
        karvand["city"] = input("Enter new city: ").strip()

    elif choice == "4":
        karvand["education"]["degree"] = input(
            "Enter new education degree: "
        ).strip()

    elif choice == "5":
        karvand["education"]["field"] = input(
            "Enter new education field: "
        ).strip()

    elif choice in ("6", "7", "8"):
        if not karvand["skills"]:
            print("No skills found for this karvand.")
            return

        for index, skill in enumerate(karvand["skills"], start=1):
            print(f"{index}. {skill['name']}")

        try:
            skill_number = int(input("Select skill number: "))
        except ValueError:
            print("Please enter a valid number.")
            return

        if not 1 <= skill_number <= len(karvand["skills"]):
            print("Invalid skill number.")
            return

        skill = karvand["skills"][skill_number - 1]

        if choice == "6":
            skill["name"] = input("Enter new skill name: ").strip()

        elif choice == "7":
            skill["level"] = input("Enter new skill level: ").strip()

        elif choice == "8":
            while True:
                try:
                    score = int(input("Enter new skill score (0-100): "))

                    if 0 <= score <= 100:
                        skill["score"] = score
                        break

                    print("Score must be between 0 and 100.")

                except ValueError:
                    print("Please enter a valid number.")

    else:
        print("Invalid choice.")
        return

    save_data(data)
    print("Karvand updated successfully.")


def generate_report(data):
    print("\n--- Summary Report ---")

    karvands = data["karvands"]
    total_karvands = len(karvands)

    all_skills = [
        skill
        for karvand in karvands
        for skill in karvand.get("skills", [])
    ]

    total_skills = len(all_skills)

    scores = [
        skill["score"]
        for skill in all_skills
        if isinstance(skill.get("score"), (int, float))
        and not isinstance(skill.get("score"), bool)
    ]

    average_score = round(sum(scores) / len(scores), 2) if scores else 0

    cities = sorted({
        karvand.get("city", "")
        for karvand in karvands
        if karvand.get("city", "")
    })

    skill_names = sorted({
        skill.get("name", "")
        for skill in all_skills
        if skill.get("name", "")
    })

    report = {
        "bootcamp": data.get("bootcamp", {}).get(
            "name", "Karvand Bootcamp"
        ),
        "total_karvands": total_karvands,
        "total_skills": total_skills,
        "average_skill_score": average_score,
        "cities": cities,
        "skill_names": skill_names
    }

    with open(REPORT_FILE, "w", encoding="utf-8") as file:
        json.dump(report, file, ensure_ascii=False, indent=4)

    print(f"Total karvands: {total_karvands}")
    print(f"Total skills: {total_skills}")
    print(f"Average skill score: {average_score}")
    print(f"Cities: {', '.join(cities) if cities else 'None'}")
    print(
        f"Skills: {', '.join(skill_names) if skill_names else 'None'}"
    )
    print(f"Report saved to {REPORT_FILE}")


def show_menu():
    print("\n--- Karvand Manager ---")
    print("1. Add Karvand")
    print("2. Show Karvands")
    print("3. Search Karvand")
    print("4. Delete Karvand")
    print("5. Edit Karvand")
    print("6. Generate Summary Report")
    print("7. Exit")


def main():
    data = load_data()

    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_karvand(data)
        elif choice == "2":
            show_karvands(data)
        elif choice == "3":
            search_karvand(data)
        elif choice == "4":
            delete_karvand(data)
        elif choice == "5":
            edit_karvand(data)
        elif choice == "6":
            generate_report(data)
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
