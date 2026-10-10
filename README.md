# Adult Dataset Income Analysis

This Python project performs a demographic data analysis on the well-known *Adult Dataset* using the **Pandas** library. It extracts insights regarding income, education, age, and working hours.

## 📊 Key Analyses
The script calculates the following metrics:
* The percentage of people earning more than \$50k.
* The average age of high earners (>50k).
* The average age grouped by education level.
* The percentage of men and women earning over \$50k (proportionate to their respective gender totals).
* The median hours worked per week for high earners.
  
## 🛠️ Data Cleaning & Ethical Note
Before processing, the dataset is cleaned and prepared:
* **Missing Values:** `?` placeholders are replaced with `NaN` and text columns are filled with `--No Data--`.
* **Data Ethics:** The `race` column was intentionally dropped.
