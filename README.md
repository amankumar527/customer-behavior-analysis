# 🛍️ Customer Shopping Behavior Analysis — End-to-End Data Analytics Project

> A complete end-to-end data analytics project analyzing 3,900 customer transactions to uncover spending patterns, customer segments, product preferences, and subscription behavior.

---

## 📌 Project Overview

This project covers the **full data analytics pipeline**:

```
Raw Data → Python (EDA + Cleaning) → PostgreSQL (SQL Analysis) → Power BI (Dashboard)
```

**Business Goal:** Help a retail business understand who their customers are, what they buy, and how to increase revenue through data-driven decisions.

---

## 🗂️ Project Structure

```
customer-behavior-analysis/
│
├── 📂 01_python_eda/
│   ├── customer_eda.ipynb          ← Jupyter notebook (full EDA)
│   └── customer_eda.py             ← Python script version
│
├── 📂 02_sql_analysis/
│   └── business_queries.sql        ← 10 business SQL queries
│
├── 📂 03_powerbi_dashboard/
│   ├── Customer_Behavior.pbix      ← Power BI dashboard file
│   └── dashboard_guide.md          ← How to use the dashboard
│
├── 📂 04_reports/
│   └── Customer_Shopping_Behavior_Analysis.pdf  ← Full project report
│
├── 📂 05_presentation/
│   └── Customer_Behavior_Presentation.pptx      ← Project slides
│
├── 📂 data/
│   ├── raw/                        ← Original dataset (not tracked in Git)
│   └── cleaned/                    ← Processed dataset (not tracked in Git)
│
├── 📂 screenshots/
│   ├── powerbi_dashboard.png       ← Dashboard screenshot
│   ├── sql_results/                ← SQL query result screenshots
│   └── eda_plots/                  ← Python EDA charts
│
├── 📄 README.md
├── 📄 requirements.txt
└── 📄 .gitignore
```

---

## 📊 Dataset Overview

| Property | Value |
|---|---|
| Source | Retail transaction records |
| Rows | 3,900 |
| Columns | 18 |
| Missing Values | 37 (Review Rating) |

**Key Columns:**
- **Demographics:** Age, Gender, Location, Subscription Status
- **Purchase Info:** Item, Category, Amount (USD), Season, Size, Color
- **Behavior:** Discount Applied, Previous Purchases, Frequency, Review Rating, Shipping Type

---

## 🐍 Step 1 — Python EDA & Data Cleaning

**Tools:** `pandas`, `numpy`, `matplotlib`, `seaborn`, `sqlalchemy`

### What Was Done:

| Task | Details |
|---|---|
| Data Loading | Imported with `pandas`, checked shape & dtypes |
| Missing Values | Imputed Review Rating with **category-wise median** |
| Column Standardization | Renamed all columns to `snake_case` |
| Feature Engineering | Created `age_group` (binned) + `purchase_frequency_days` |
| Data Consistency | Verified `discount_applied` vs `promo_code_used` — dropped redundant column |
| DB Integration | Connected to PostgreSQL via `sqlalchemy` & loaded cleaned data |

### Key EDA Findings:
- Average purchase amount: **$59.76**
- Male customers contributed **~68% of total revenue**
- **Young Adults** (18-30) are the highest spending age group
- **Clothing** is the top category by revenue and sales volume

---

## 🗄️ Step 2 — SQL Analysis (PostgreSQL / SSMS)

**10 Business Questions Answered:**

| # | Question | Key Finding |
|---|---|---|
| 1 | Revenue by Gender | Male: $157,890 vs Female: $75,191 |
| 2 | High-Spending Discount Users | 839 customers spent above avg despite discounts |
| 3 | Top 5 Products by Rating | Gloves (3.86), Sandals (3.84), Boots (3.82) |
| 4 | Standard vs Express Shipping | Express avg: $60.48 vs Standard: $58.46 |
| 5 | Subscribers vs Non-Subscribers | Non-sub revenue: $170,436 (larger base) |
| 6 | Discount-Dependent Products | Hat (50%), Sneakers (49.66%), Coat (49.07%) |
| 7 | Customer Segmentation | Loyal: 3,116 \| Returning: 701 \| New: 83 |
| 8 | Top 3 per Category | Jewelry, Blouse, Sandals, Jacket lead categories |
| 9 | Repeat Buyers & Subscriptions | 27.5% of repeat buyers subscribe |
| 10 | Revenue by Age Group | Young Adult: $62,143 → Middle-aged: $59,197 |

---

## 📈 Step 3 — Power BI Dashboard

**Interactive dashboard with slicers for:**
- Subscription Status (Yes / No)
- Gender (Male / Female)
- Category (Accessories, Clothing, Footwear, Outerwear)
- Shipping Type

**Visuals Included:**
- KPI Cards: Total Customers, Avg Review Rating, Avg Purchase Amount
- Donut Chart: % Customers by Subscription Status
- Bar Charts: Revenue by Category, Sales by Category
- Grouped Bar: Revenue & Sales by Age Group

> 📎 Open `03_powerbi_dashboard/Customer_Behavior.pbix` in Power BI Desktop to interact

---

## 💡 Business Recommendations

| Recommendation | Insight |
|---|---|
| **Boost Subscriptions** | Subscribers have similar avg spend — promote exclusive perks |
| **Loyalty Programs** | 3,116 loyal customers — reward to retain |
| **Review Discount Policy** | 50% discount on Hat — review margin impact |
| **Target Young Adults** | Highest revenue group — personalized campaigns |
| **Highlight Top Products** | Gloves, Sandals top rated — feature in marketing |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|---|---|
| Python (pandas, numpy) | Data cleaning & EDA |
| Matplotlib / Seaborn | Visualizations |
| SQLAlchemy | Python → PostgreSQL connection |
| PostgreSQL / SSMS | SQL business analysis |
| Power BI Desktop | Interactive dashboard |
| Jupyter Notebook | EDA documentation |

---

## 🚀 How To Run

### Python EDA
```bash
git clone https://github.com/YOUR_USERNAME/customer-behavior-analysis.git
cd customer-behavior-analysis
pip install -r requirements.txt
jupyter notebook 01_python_eda/customer_eda.ipynb
```

### SQL Queries
1. Open SSMS or pgAdmin
2. Connect to your database
3. Run `02_sql_analysis/business_queries.sql`

### Power BI Dashboard
1. Install [Power BI Desktop](https://powerbi.microsoft.com/desktop/)
2. Open `03_powerbi_dashboard/Customer_Behavior.pbix`
3. Use slicers to filter and explore

---

## 📄 Deliverables

| File | Description |
|---|---|
| `04_reports/Customer_Shopping_Behavior_Analysis.pdf` | Full written report |
| `05_presentation/Customer_Behavior_Presentation.pptx` | Project presentation |
| `03_powerbi_dashboard/Customer_Behavior.pbix` | Interactive dashboard |
| `02_sql_analysis/business_queries.sql` | All SQL queries |
| `01_python_eda/customer_eda.ipynb` | Jupyter notebook |

---

## 👤 Author

**Aman Kumar**



