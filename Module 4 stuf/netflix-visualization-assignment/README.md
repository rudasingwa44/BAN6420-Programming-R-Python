# Module 4 Assignment – Netflix Data Visualization

Analysis of the Netflix titles dataset (movies and TV shows) using Python for
data preparation, cleaning, exploration and visualization, and R (ggplot2) for
one of the charts.

## Files
| File | Description |
|---|---|
| `assignment.ipynb` | Python notebook: unzip & rename, cleaning, exploration, charts |
| `assignment.R` | R script: ratings distribution chart with ggplot2 |
| `netflix_data.zip` | Original dataset (zipped) |
| `Netflix_shows_movies.csv` | Raw data after unzipping and renaming (as required) |
| `Netflix_shows_movies_cleaned.csv` | Cleaned data created by the notebook and used by R |
| `top_genres.png` | Chart: most common genres (Python, Seaborn) |
| `ratings_distribution.png` | Chart: ratings distribution (Python, Seaborn) |
| `ratings_r.png` | Chart: ratings distribution (R, ggplot2) |

## Requirements
- Python 3 with pandas, matplotlib and seaborn:
  `pip install pandas matplotlib seaborn`
- R 4.x with ggplot2:
  `install.packages("ggplot2")`

## How to run
### Python
1. Keep all files in this folder.
2. Open `assignment.ipynb` and click **Run All**.
   The notebook unzips `netflix_data.zip`, renames the file to
   `Netflix_shows_movies.csv`, cleans it, prints the exploration results,
   saves both charts as PNG files and writes `Netflix_shows_movies_cleaned.csv`.

### R
1. Run the Python notebook first (it creates the cleaned CSV).
2. Set R's working directory to this folder, for example:
   `setwd("path/to/netflix-visualization-assignment")`
3. Run the script with `source("assignment.R")` (or Ctrl+Shift+S in VS Code).
   The chart is displayed and saved as `ratings_r.png`.

## Data preparation
The dataset was provided on Canvas as a CSV file, so it was zipped as
`netflix_data.zip` to demonstrate the required unzip step. The notebook unzips it
with `zipfile` and renames it to `Netflix_shows_movies.csv` with `os.replace`,
which also allows the notebook to be re-run safely.

## Data cleaning
| Column | Missing values | Action |
|---|---|---|
| director | 1,969 | Filled with "Unknown" |
| cast | 570 | Filled with "Unknown" |
| country | 476 | Filled with "Unknown" |
| rating | 10 | Filled with "Unknown" |
| date_added | 11 | Rows dropped (very few) |

Text columns were filled rather than dropped so that no titles were lost.
The cleaned dataset has **6,223 titles** (from 6,234).

## Assumptions
- The dataset has **no viewing figures**, so "most watched genres" is measured as
  the **genres with the most titles** on Netflix.
- Each title can belong to several genres (e.g. "Dramas, International Movies"),
  so the `listed_in` column was split and each genre counted separately.
- "Ratings" are content (age) ratings such as TV-MA and PG-13, so their
  distribution is shown as the number of titles per rating.

## Key findings
- **69% movies, 31% TV shows** (4,264 vs 1,959 titles).
- **Top genres:** International Movies (1,927), Dramas (1,623), Comedies (1,113).
- **Most common ratings:** TV-MA (2,025) and TV-14 (1,695), so most content
  targets adult and teenage audiences.
- **Release years** range from 1925 to 2020. The median is 2016, so the catalogue
  is mostly recent titles; the mean (2013) is pulled down by a few very old titles.

**Author:** Ivan