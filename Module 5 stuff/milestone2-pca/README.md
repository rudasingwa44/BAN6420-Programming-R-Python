# Milestone 2 – Principal Component Analysis (Anderson Cancer Center)

A PySpark data pipeline that prepares breast cancer referral data and applies
Principal Component Analysis (PCA) to identify the essential variables for securing
donor funding. Bonus: a logistic regression model predicts diagnosis from the
2 principal components.

## Files
| File | Description |
|---|---|
| `pca_pipeline.ipynb` | The full pipeline: schema, cleaning, scaling, PCA, essential variables, logistic regression |
| `BAN6420 M5 breast_cancer_referrals.csv` | Raw referral data (572 rows, 32 columns) |

## Requirements
- **Java 17** (e.g. Eclipse Temurin 17) – required by Spark
- **Python 3** with `pyspark` and `pandas`:
  `pip install pyspark pandas`

## How to run
1. Keep the notebook and the CSV file in the same folder.
2. Open `pca_pipeline.ipynb` in VS Code or Jupyter.
3. Click **Run All**. The first cell starts Spark (this takes 10–30 seconds).
   Warnings about `winutils`/Hadoop on Windows are normal and can be ignored.

## Pipeline steps
1. **Schema:** the CSV is loaded into a Spark DataFrame with an explicit schema –
   `patient_id` and `diagnosis` as text, the 30 measurements as decimals.
2. **Data quality check:** 3 duplicate rows and 18 missing values
   (6 each in `mean_radius`, `mean_texture`, `worst_area`).
3. **Cleaning:** duplicates removed first, then rows with missing values dropped
   (about 3% of the data), leaving **551 patients**.
4. **Assemble & standardize:** the 30 measurements are combined into one feature
   vector with `VectorAssembler`, then standardized (mean 0, standard deviation 1)
   with `StandardScaler`. `patient_id` and `diagnosis` are excluded from the features.
5. **PCA:** reduced to 2 principal components with Spark MLlib `PCA`.
6. **Essential variables:** the PCA loadings show which measurements drive each component.
7. **Bonus:** `diagnosis` is encoded (B = 0, M = 1), the data split 80/20 into
   training and test sets, and a logistic regression trained on the 2 components.

## Results
| Component | Variance explained | Main drivers |
|---|---|---|
| PC1 | 44.22% | concave points, concavity, compactness, perimeter (tumour shape & size) |
| PC2 | 19.04% | fractal dimension (tumour boundary complexity) |
| **Total** | **63.27%** | |

**Bonus – logistic regression accuracy:** 97.62% on unseen test patients.

## Conclusion
Two principal components retain about two-thirds of the information in the 30
original measurements. Tumour shape and size variables (PC1) and boundary
complexity (PC2) are the essential variables to prioritise. The 2 components alone
are enough to predict diagnosis with about 98% accuracy.

**Author:** Ivan