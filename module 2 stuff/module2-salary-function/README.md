# Module 2 Assignment – Salary Function

A Jupyter Notebook that imports the San Francisco salary data, looks up an
employee by name, returns their details as dictionaries, and exports them to a
CSV file inside a zipped folder called **Employee Profile**. An R script then
unzips the folder and displays the data.

## Files
| File | Purpose |
|---|---|
| `salary_function.ipynb` | Python notebook: import, function, error handling, export and zip |
| `salary_function.R` | R script: unzips `Employee Profile.zip` and displays the data |
| `Total.csv` | Salary data (source: Kaggle – SF Salaries) |
| `Employee Profile.zip` | Output created by the notebook |

## Requirements
- Python 3 with pandas (`pip install pandas`)
- R 4.x (base R only, no extra packages)

## How to use
### Python
1. Open `salary_function.ipynb` in VS Code or Jupyter (keep `Total.csv` in the same folder).
2. Click **Run All**.
3. To export a different employee, change the name in the export cell,
   e.g. `get_employee("Gary Jimenez")`. Names are not case-sensitive.

### R
1. Run the notebook first so `Employee Profile.zip` exists.
2. Set R's working directory to this folder, e.g.
   `setwd("path/to/module2-salary-function")`
3. Run the script with `source("salary_function.R")` (or Ctrl+Shift+S in VS Code).
   The employee's details are displayed as a vertical table.

## How it works
1. **Import:** `Total.csv` is loaded into a pandas DataFrame.
2. **Clean:** employee names are trimmed and converted to upper case, because the
   data uses capitals in 2011 and title case from 2012 onwards.
3. **Function:** `get_employee(name)` filters the data for that name and returns
   **all** of the employee's records (one per year) as a list of dictionaries.
4. **Export:** the records are saved to `Employee Profile/employee_profile.csv`
   and zipped into `Employee Profile.zip`.
5. **R:** the zip is extracted to an `unzipped` folder, and the CSV is read and printed.

## Error handling
| Situation | What happens |
|---|---|
| `Total.csv` missing | Clear message instead of a crash |
| Name is empty or not text | `ValueError`: "Please enter the employee name as text." |
| Name not found | `ValueError`: "<NAME> was not found." |
| Export with a bad name | Caught; prints "Export failed" |
| Zip missing in R | `tryCatch` reports "Employee Profile.zip not found" |

The notebook's test cell checks valid, unknown, empty and non-text names on purpose.

**Author:** Ivan