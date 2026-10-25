# BAN6420 Final Project – Income & Spending Survey

A survey web app that collects participants' age, gender, income and expenses,
stores them in MongoDB, and analyses the results in Python.

**Live app:** http://ivan-survey.eu-north-1.elasticbeanstalk.com

## How it works
Browser form → Flask (AWS Elastic Beanstalk) → MongoDB Atlas → `User` class → CSV → Jupyter charts

## Files
| File | Purpose |
|---|---|
| `app.py` | Flask app: shows the form (GET) and saves responses to MongoDB (POST) |
| `templates/index.html` | The survey form |
| `export_data.py` | `User` class that flattens MongoDB records and saves `survey_data.csv` |
| `survey_data.csv` | Exported survey data |
| `analysis.ipynb` | Data analysis and visualisations |
| `chart1_income_by_age.png` | Ages with the highest income |
| `chart2_spending_by_gender.png` | Gender distribution across spending categories |
| `requirements.txt`, `Procfile` | AWS deployment configuration |
| `screenshots/` | Proof of AWS deployment and database records |

## Run locally
1. `pip install -r requirements.txt`
2. Create a `.env` file containing `MONGO_URI=<your MongoDB connection string>`
3. Run `python app.py` and open http://127.0.0.1:5000
4. Run `python export_data.py` to export the data to CSV
5. Open `analysis.ipynb` and click **Run All**

## Deployment
Deployed on AWS Elastic Beanstalk (Python 3.12, single instance, eu-north-1) using
Gunicorn (`Procfile`). The database connection string is stored as an AWS environment
property, not in the code.

## Key insights
- **Income by age:** income generally rises with age; respondents in their 40s–50s earn the most.
- **Spending by gender:** school fees are the largest expense for females; males and others spend more on entertainment.

## Data quality notes
Two capture errors were found and corrected in MongoDB before analysis
(an income missing a zero, and an income typed into the age field).

## Security
- Credentials are kept in `.env` (excluded via `.gitignore`) locally and in AWS environment properties in the cloud.
- The app uses HTTP; a production version would add HTTPS.