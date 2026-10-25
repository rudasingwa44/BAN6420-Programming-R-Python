import os
import pandas as pd
from dotenv import load_dotenv
from pymongo import MongoClient

EXPENSE_TYPES = ["utilities", "entertainment", "school_fees", "shopping", "healthcare"]

class User:
    def __init__(self, age, gender, total_income, expenses):
        self.age = age
        self.gender = gender
        self.total_income = total_income
        self.expenses = expenses

    def to_row(self):
        row = {"age": self.age, "gender": self.gender, "total_income": self.total_income}
        for item in EXPENSE_TYPES:
            row[item] = self.expenses.get(item, 0)
        return row

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
collection = client["survey_db"]["responses"]

users = []
for doc in collection.find():
    user = User(doc["age"], doc["gender"], doc["total_income"], doc.get("expenses", {}))
    users.append(user)

rows = []
for user in users:
    rows.append(user.to_row())

df = pd.DataFrame(rows)

folder = os.path.dirname(__file__)
df.to_csv(os.path.join(folder, "survey_data.csv"), index=False)

print(df.head())
print(len(df), "rows saved to survey_data.csv")
