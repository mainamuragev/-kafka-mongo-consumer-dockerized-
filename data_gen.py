from faker import Faker
import random

fake = Faker()

def gen(n=1):
    return [
        {
            "name": fake.name(),
            "email": fake.email(),
            "job": fake.job(),
            "salary": round(random.uniform(30000, 150000), 2)
        }
        for _ in range(n)
    ]