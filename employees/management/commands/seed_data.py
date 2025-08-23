from django.core.management.base import BaseCommand
from faker import Faker
import random
from employees.models import Employee
from departments.models import Department
from attendance.models import Attendance
from performance.models import Performance
from datetime import datetime, timedelta

class Command(BaseCommand):
    help = "Seed database with fake employees, departments, attendance, and performance"

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create Departments
        departments = ["HR", "IT", "Finance", "Marketing", "Operations"]
        dept_objs = []
        for dept in departments:
            obj, created = Department.objects.get_or_create(name=dept)
            dept_objs.append(obj)

        # Create Employees
        employees = []
        for _ in range(50):
            emp = Employee.objects.create(
                name=fake.name(),
                email=fake.unique.email(),
                phone=fake.unique.phone_number(),
                address=fake.address(),
                date_of_joining=fake.date_between(start_date="-2y", end_date="today"),
                department=random.choice(dept_objs),
            )
            employees.append(emp)

        # Create Attendance
        for emp in employees:
            for i in range(10):  # 10 random days per employee
                Attendance.objects.create(
                    employee=emp,
                    date=fake.date_between(start_date="-30d", end_date="today"),
                    status=random.choice(["Present", "Absent", "Late"]),
                )

        # Create Performance
        for emp in employees:
            for i in range(3):  # 3 reviews per employee
                Performance.objects.create(
                    employee=emp,
                    rating=random.randint(1, 5),
                    review_date=fake.date_between(start_date="-1y", end_date="today"),
                )

        self.stdout.write(self.style.SUCCESS("✅ Database seeded successfully!"))
