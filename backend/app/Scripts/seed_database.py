import json

from database.database import SessionLocal
from models.Interview_Preparation import Interview_Preparation
from models.roles import Role

JSON_FILE = "seed_data/interview_preparation/SQL.json"


def seed_database():

    db = SessionLocal()

    try:

        with open(JSON_FILE, "r") as file:
            data = json.load(file)

        print(data, "data")

        for resource in data:

            print("seeding resource:", resource)

            # Find role
            role = (
                db.query(Role)
                .filter(
                    Role.role_name == resource["role"]
                )
                .first()
            )

            if role is None:
                print(
                    f"Role not found: {resource['role']}. "
                    f"Skipping question."
                )
                continue

            # Check duplicate
            existing_resource = (
                db.query(Interview_Preparation)
                .filter(
                    Interview_Preparation.role_id == role.role_id,
                    Interview_Preparation.skill == resource["skill"],
                    Interview_Preparation.question == resource["question"]
                )
                .first()
            )

            if existing_resource:
                print(
                    "Question already exists, skipping:",
                    resource["question"]
                )
                continue

            # Create new interview question
            new_resource = Interview_Preparation(
                role_id=role.role_id,
                skill=resource["skill"],
                question=resource["question"],
                question_type=resource["question_type"],
                difficulty=resource["difficulty"]
            )

            db.add(new_resource)

        db.commit()

        print("Database seeding completed successfully.")


    except Exception as e:

        db.rollback()

        print(
            "Error while seeding database:",
            e
        )

    finally:

        db.close()


if __name__ == "__main__":
    seed_database()