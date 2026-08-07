# Kaggle Data Cleaning - Missing Values (Notebook Note)

> প্রতিটি অংশ একটি আলাদা Jupyter Code Cell হিসেবে কপি-পেস্ট করতে পারো।

``` python
# ============================================================
# Step 1: Import Libraries
# ============================================================

# Pandas -> Data Analysis
import pandas as pd

# NumPy -> Numerical Computing
import numpy as np

# একই random result পাওয়ার জন্য seed সেট করা হয় (Reproducibility)
np.random.seed(0)
```

``` python
# ============================================================
# Step 2: Load Dataset
# ============================================================

nfl_data = pd.read_csv(
    "../input/nflplaybyplay2009to2016/NFL Play by Play 2009-2017 (v4).csv"
)
```

``` python
# ============================================================
# Step 3: First Look
# ============================================================

# প্রথম ৫টি row দেখি
# NaN / None আছে কিনা observe করি
nfl_data.head()
```

``` python
# ============================================================
# Step 4: Count Missing Values
# ============================================================

missing_values_count = nfl_data.isnull().sum()

missing_values_count[:10]
```

``` python
# ============================================================
# Step 5: Missing Percentage
# ============================================================

total_cells = np.product(nfl_data.shape)

total_missing = missing_values_count.sum()

percent_missing = (total_missing / total_cells) * 100

print(percent_missing)
```

``` python
# ============================================================
# Step 6: Data Intuition
# ============================================================

'''
প্রশ্ন:
Missing value কেন?

১. Wasn't Recorded
- Data থাকার কথা ছিল।
- Record করা হয়নি।
- Example:
  User Age
  Student CGPA

=> সাধারণত Fill / Impute করা যায়।

২. Doesn't Exist
- Data বাস্তবেই নেই।
- Example:
  Spouse Name (Unmarried Student)

=> সাধারণত NaN রেখে দেওয়া ভালো।
'''
```

``` python
# ============================================================
# Step 7: Drop Missing Rows
# ============================================================

# যেসব row-এ অন্তত একটি NaN আছে সেগুলো delete হবে
nfl_data.dropna()
```

``` python
# ============================================================
# Step 8: Drop Missing Columns
# ============================================================

columns_with_na_dropped = nfl_data.dropna(axis=1)

columns_with_na_dropped.head()
```

``` python
# ============================================================
# Step 9: Compare Columns
# ============================================================

print("Original Columns :", nfl_data.shape[1])
print("Remaining Columns:", columns_with_na_dropped.shape[1])
```

``` python
# ============================================================
# Step 10: Create Small Subset
# ============================================================

subset_nfl_data = nfl_data.loc[:, "EPA":"Season"].head()

subset_nfl_data
```

``` python
# ============================================================
# Step 11: Fill Missing Values
# ============================================================

# সব NaN এর জায়গায় 0 বসাবে
subset_nfl_data.fillna(0)
```

``` python
# ============================================================
# Step 12: Back Fill
# ============================================================

'''
bfill = নিচের valid value দিয়ে NaN পূরণ করে।

Example

10
NaN
30

↓

10
30
30
'''

subset_nfl_data.fillna(method="bfill", axis=0)
```

``` python
# ============================================================
# Step 13: Back Fill + fillna
# ============================================================

'''
যদি সবচেয়ে নিচের row-ও NaN হয়,
তাহলে bfill সেটা পূরণ করতে পারবে না।

তাই শেষে fillna(0) ব্যবহার করা হয়।
'''

subset_nfl_data.fillna(method="bfill", axis=0).fillna(0)
```

``` python
# ============================================================
# Step 14: Forward Fill (Extra)
# ============================================================

'''
ffill = উপরের valid value দিয়ে NaN পূরণ করে।
'''

subset_nfl_data.fillna(method="ffill", axis=0)
```

``` python
# ============================================================
# Quick Revision
# ============================================================

'''
head()
    প্রথম ৫টি row

isnull()
    Missing value detect

sum()
    Missing value count

shape
    (rows, columns)

dropna()
    Missing row remove

dropna(axis=1)
    Missing column remove

fillna(0)
    নির্দিষ্ট value দিয়ে fill

fillna(method="bfill")
    নিচের value দিয়ে fill

fillna(method="ffill")
    উপরের value দিয়ে fill

Rule

Wasn't Recorded
    Fill / Impute

Doesn't Exist
    NaN রাখা যায়
'''
```
