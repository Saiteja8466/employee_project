from django.core.management.base import BaseCommand
from faker import Faker
from employees.models import Employee, Department
from attendance.models import Attendance
from performance.models import Performance
import random
from datetime import date, timedelta

fake = Faker()


class Command(BaseCommand):
    help = "Seed database with fake employees, attendance, and performance"

    def handle(self, *args, **kwargs):
        # Departments
        departments = ["HR", "IT", "Sales", "Marketing"]
        for dept in departments:
            Department.objects.get_or_create(name=dept)

        # Employees
        for _ in range(30):
            dept = Department.objects.order_by("?").first()
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                date_of_joining=fake.date_between(start_date="-2y", end_date="today"),
                department=dept,
            )

            # Attendance for last 30 days
            for i in range(30):
                Attendance.objects.create(
                    employee=emp,
                    date=date.today() - timedelta(days=i),
                    status=random.choice(["Present", "Absent", "Late"]),
                )

            # Performance reviews
            for i in range(3):
                Performance.objects.create(
                    employee=emp,
                    rating=random.randint(1, 5),
                    review_date=fake.date_between(start_date="-1y", end_date="today"),
                )
        self.stdout.write(self.style.SUCCESS("Database seeded successfully!"))
