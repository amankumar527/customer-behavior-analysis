# 🗄️ SQL Business Analysis — Customer Shopping Behavior

## Database: PostgreSQL / SSMS
## Table: `customer`

---

## How to Run

1. Open **SSMS** or **pgAdmin**
2. Connect to your database
3. Open `business_queries.sql`
4. Run all queries (or one by one)

---

## Query Summary

| Query | Business Question | Key Result |
|---|---|---|
| Q1 | Revenue by Gender | Male: $157,890 / Female: $75,191 |
| Q2 | High-Spending Discount Users | 839 customers |
| Q3 | Top 5 Products by Rating | Gloves → Sandals → Boots |
| Q4 | Standard vs Express Shipping | Express slightly higher avg ($60.48) |
| Q5 | Subscribers vs Non-Subscribers | Non-subs have more customers |
| Q6 | Discount-Dependent Products | Hat (50%) top discounted item |
| Q7 | Customer Segmentation | Loyal: 3116, Returning: 701, New: 83 |
| Q8 | Top 3 per Category | Jewelry, Blouse, Sandals, Jacket |
| Q9 | Repeat Buyers & Subscriptions | 72.4% repeat buyers don't subscribe |
| Q10 | Revenue by Age Group | Young Adult leads at $62,143 |

---

## Techniques Used

- `GROUP BY` + `SUM`, `AVG`, `COUNT`
- Subqueries (correlated)
- `CASE WHEN` for segmentation
- `WITH` CTE (Common Table Expressions)
- `ROW_NUMBER()` window function
- `OVER (PARTITION BY ...)` for ranking
- `ROUND()` for formatting
