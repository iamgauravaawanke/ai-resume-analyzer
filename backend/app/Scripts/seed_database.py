import json

from database.database import SessionLocal
from models.learning_resource import Learning_Resource, ResourceType

JSON_FILE = "seed_data/learning_resources/Docker.json"


def seed_database():
    db = SessionLocal()

    try:
        with open(JSON_FILE, "r") as file:
            data = json.load(file)

        print(data, "data")

        for resource in data:
            print("Seeding resource:", resource)

            # Check for duplicate resource
            existing_resource = (
                db.query(Learning_Resource)
                .filter(
                    Learning_Resource.skill == resource["skill"],
                    Learning_Resource.resource_type
                    == ResourceType(resource["resource_type"]),
                    Learning_Resource.url == resource["url"],
                )
                .first()
            )

            if existing_resource:
                # Resource already exists, so skip it
                continue

            # Create new resource
            new_resource = Learning_Resource(
                skill=resource["skill"],
                resource_type=ResourceType(resource["resource_type"]),
                title=resource["title"],
                url=resource["url"],
            )

            db.add(new_resource)

        # Commit all resources at once
        db.commit()

        print("Database seeding completed successfully.")

    except Exception as e:
        db.rollback()
        print("Error while seeding database:", e)

    finally:
        db.close()


if __name__ == "__main__":
    seed_database()