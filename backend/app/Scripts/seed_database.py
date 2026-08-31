
import json

from database.database import SessionLocal
from models.learning_resource import Learning_Resource

JSON_FILE = "seed_data/learning_resources/Kubernetes.json"


def seed_database():

    db = SessionLocal()

    try:

        with open(JSON_FILE, "r") as file:
            data = json.load(file)

        print(data, "data")

        for resource in data:

            print("seeding resource:", resource)

            # Check duplicate
            existing_resource = (
                db.query(Learning_Resource)
                .filter(
                    Learning_Resource.skill == resource["skill"],
                    Learning_Resource.title == resource["title"]
                )
                .first()
            )

            if existing_resource:
                print(
                    "Resource already exists, skipping:",
                    resource["title"]
                )
                continue

            # Create learning resource
            new_resource = Learning_Resource(
                skill=resource["skill"],
                resource_type=resource["resource_type"],
                title=resource["title"],
                url=resource["url"]
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
