import json
import os.path

from django.core.management import BaseCommand

from main_app.models import Student
from project_data import settings


class Command(BaseCommand):
    help = "Populates Our DB with Students data from json file"

    def handle(self, *args, **options):
        path = os.path.join(settings.BASE_DIR, "students.json")
        print(path)

        self.stdout.write(
            self.style.SUCCESS("Starting to ingest the data")
        )

        with open(path) as file:
            students = json.load(file)
            for s in students:
                Student.objects.create(
                    first_name=s["first_name"],
                    last_name=s["last_name"],
                    email=s["email"],
                    dob=s["dob"],
                    is_sporty=s["is_sporty"],
                    kcpe_score=s["kcpe_score"],
                    weight=s["weight"],
                    profile_pic="students/default.png",
                )

        self.stdout.write(
            self.style.SUCCESS("Completed  ingesting the data")
        )

        # python manage.py populate
