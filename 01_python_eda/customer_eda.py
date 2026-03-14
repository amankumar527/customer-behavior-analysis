"""
Customer Shopping Behavior Analysis
====================================
End-to-end Python EDA + Data Cleaning + PostgreSQL Integration
Author: Aman Kumar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sqlalchemy import create_engine

# ===========================
# 1. LOAD DATA
# ===========================
df = pd.read_csv("data/raw/shopping_behavior.csv")

print("=" * 50)
print("DATASET OVERVIEW")
print("=" * 50)
print(f"Shape: {df.shape}")
print(f"\nColumn Types:\n{df.dtypes}")
print(f"\nBasic Stats:\n{df.describe()}")

# ===========================
# 2. MISSING VALUE CHECK
# ===========================
print("\n" + "=" * 50)
print("MISSING VALUES")
print("=" * 50)
missing = df.isnull().sum()
print(missing[missing > 0])

# Impute Review Rating with category-wise median
df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(
    lambda x: x.fillna(x.median())
)
print(f"\n✅ Review Rating missing values imputed with category-wise median")
print(f"Remaining nulls: {df['Review Rating'].isnull().sum()}")

# ===========================
# 3. COLUMN STANDARDIZATION
# ===========================
df.columns = [col.strip().lower().replace(" ", "_").replace("(", "").replace(")", "") for col in df.columns]
print(f"\n✅ Columns renamed to snake_case:\n{df.columns.tolist()}")

# ===========================
# 4. FEATURE ENGINEERING
# ===========================

# Age group binning
bins = [0, 25, 35, 50, 100]
labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.cut(df['age'], bins=bins, labels=labels, right=False)
print(f"\n✅ age_group created:\n{df['age_group'].value_counts()}")

# Purchase frequency mapping
freq_map = {
    'Weekly': 7,
    'Bi-Weekly': 14,
    'Fortnightly': 14,
    'Monthly': 30,
    'Every 3 Months': 90,
    'Quarterly': 90,
    'Annually': 365
}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(freq_map)
print(f"\n✅ purchase_frequency_days created")

# ===========================
# 5. DATA CONSISTENCY CHECK
# ===========================
# Check if discount_applied and promo_code_used are redundant
check = df.groupby(['discount_applied', 'promo_code_used']).size()
print(f"\nDiscount vs Promo Code cross-tab:\n{check}")

# Drop redundant column
if 'promo_code_used' in df.columns:
    df.drop(columns=['promo_code_used'], inplace=True)
    print("✅ promo_code_used dropped (redundant with discount_applied)")

# ===========================
# 6. KEY EDA INSIGHTS
# ===========================
print("\n" + "=" * 50)
print("KEY INSIGHTS")
print("=" * 50)

# Revenue by gender
rev_gender = df.groupby('gender')['purchase_amount_usd'].sum()
print(f"\nRevenue by Gender:\n{rev_gender}")

# Revenue by category
rev_cat = df.groupby('category')['purchase_amount_usd'].sum().sort_values(ascending=False)
print(f"\nRevenue by Category:\n{rev_cat}")

# Revenue by age group
rev_age = df.groupby('age_group')['purchase_amount_usd'].sum().sort_values(ascending=False)
print(f"\nRevenue by Age Group:\n{rev_age}")

# Subscription breakdown
sub = df['subscription_status'].value_counts(normalize=True) * 100
print(f"\nSubscription %:\n{sub.round(1)}")

# ===========================
# 7. VISUALIZATIONS
# ===========================
plt.style.use('seaborn-v0_8-whitegrid')
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Customer Shopping Behavior — EDA', fontsize=16, fontweight='bold')

# Revenue by Category
rev_cat.plot(kind='bar', ax=axes[0, 0], color='steelblue', edgecolor='black')
axes[0, 0].set_title('Revenue by Category')
axes[0, 0].set_xlabel('Category')
axes[0, 0].set_ylabel('Total Revenue ($)')
axes[0, 0].tick_params(axis='x', rotation=45)

# Revenue by Age Group
rev_age.plot(kind='bar', ax=axes[0, 1], color='coral', edgecolor='black')
axes[0, 1].set_title('Revenue by Age Group')
axes[0, 1].set_xlabel('Age Group')
axes[0, 1].set_ylabel('Total Revenue ($)')
axes[0, 1].tick_params(axis='x', rotation=45)

# Subscription donut chart
sub.plot(kind='pie', ax=axes[1, 0], autopct='%1.1f%%',
         colors=['#4472C4', '#ED7D31'], startangle=90,
         wedgeprops={'width': 0.5})
axes[1, 0].set_title('Subscription Status Distribution')
axes[1, 0].set_ylabel('')

# Purchase amount distribution
axes[1, 1].hist(df['purchase_amount_usd'], bins=30, color='mediumseagreen', edgecolor='black')
axes[1, 1].set_title('Purchase Amount Distribution')
axes[1, 1].set_xlabel('Purchase Amount (USD)')
axes[1, 1].set_ylabel('Frequency')
axes[1, 1].axvline(df['purchase_amount_usd'].mean(), color='red', linestyle='--',
                    label=f"Mean: ${df['purchase_amount_usd'].mean():.2f}")
axes[1, 1].legend()

plt.tight_layout()
plt.savefig('screenshots/eda_plots/eda_overview.png', dpi=150, bbox_inches='tight')
plt.show()
print("✅ EDA plot saved to screenshots/eda_plots/eda_overview.png")

# ===========================
# 8. EXPORT CLEANED DATA
# ===========================
df.to_csv('data/cleaned/shopping_behavior_cleaned.csv', index=False)
print(f"\n✅ Cleaned data saved: {df.shape}")

# ===========================
# 9. POSTGRESQL INTEGRATION
# ===========================
print("\n" + "=" * 50)
print("DATABASE INTEGRATION")
print("=" * 50)

# Update these credentials before running
DB_USER = "postgres"
DB_PASS = "your_password"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "shopping_db"

try:
    engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
    df.to_sql('customer', engine, if_exists='replace', index=False)
    print(f"✅ Data loaded to PostgreSQL table 'customer' — {len(df)} rows")
except Exception as e:
    print(f"⚠️  DB connection failed (update credentials): {e}")

print("\n🎉 EDA Complete!")
