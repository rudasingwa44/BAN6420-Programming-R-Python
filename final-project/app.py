import os
from dotenv import load_dotenv
from flask import Flask, render_template, request
from pymongo import MongoClient

load_dotenv()
client = MongoClient(os.getenv("MONGO_URI"))
collection = client["survey_db"]["responses"]

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        ticked = request.form.getlist("expense")

        expenses = {}
        for item in ticked:
            amount = request.form.get(item + "_amount") or 0
            expenses[item] = float(amount)

        record = {
            "age": int(request.form["age"]),
            "gender": request.form["gender"],
            "total_income": float(request.form["total_income"]),
            "expenses": expenses
        }

        collection.insert_one(record)
        return 'Thank you! Your response was saved. <a href="/">Submit another</a>'

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)