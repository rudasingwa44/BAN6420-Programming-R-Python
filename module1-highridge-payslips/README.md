# Highridge Construction Company – Weekly Payment Slips

Creates 400 workers dynamically and prints a weekly payment slip for each,
written in Python and converted to R.

## Files
- `payslips.py` – Python version
- `payslips.R` – R version

## How to run
- **Python:** open `payslips.py` in VS Code and click Run (▷), or run `python payslips.py`
- **R:** open `payslips.R` in VS Code and press Ctrl+Shift+S, or run `Rscript payslips.R`

No extra packages are needed.

## Employee level rules
| Level | Rule |
|---|---|
| A5-F | Salary > $7,500 and < $30,000 and female |
| A1 | Salary > $10,000 and < $20,000 |
| Standard | Everyone else |

The female (A5-F) rule is checked first because the two salary ranges overlap.
Otherwise, female workers earning $10,000–$20,000 would never receive A5-F.

## Exception handling
Each payment slip is created inside `try/except` (Python) or `tryCatch` (R).
If a salary is not a number, an error is raised, reported, and the program
continues with the next worker. Worker 401 (`Worker_Test`, salary "N/A") is
included on purpose to show this working.

## Note
A random seed (42) is used so results are the same on every run. Python and R
generate different random numbers, so the two outputs will differ, but the
logic is identical.

**Author:** Ivan