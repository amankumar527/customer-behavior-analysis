# Data Folder

## Structure

```
data/
├── raw/           ← Original dataset (not tracked in Git)
└── cleaned/       ← Cleaned dataset after Python EDA (not tracked in Git)
```

## Dataset Info

| Property | Value |
|---|---|
| Rows | 3,900 |
| Columns | 18 (raw) → 17 (after dropping promo_code_used) |
| Format | CSV |

## Note

Raw and cleaned CSV files are excluded from Git (via `.gitignore`) to keep the repo lightweight.
To get the dataset, download from the original source or run `01_python_eda/customer_eda.py`.
