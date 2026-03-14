# 📊 Power BI Dashboard Guide

## File: `Customer_Behavior.pbix`

---

## How to Open

1. Download and install [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (free)
2. Open `Customer_Behavior.pbix`
3. If data source error appears → go to `Transform Data` → update file path

---

## Dashboard Features

### KPI Cards (Top Row)
| Card | Value |
|---|---|
| Number of Customers | 3,900 / filtered count |
| Average Review Rating | 3.75 (out of 5) |
| Average Purchase Amount | $59.76 |

### Slicers (Left Panel)
- **Subscription Status:** No / Yes
- **Gender:** Female / Male
- **Category:** Accessories / Clothing / Footwear / Outerwear
- **Shipping Type:** 2-Day / Express / Free / Next Day Air / Standard / Store Pickup

### Charts
| Visual | Insight |
|---|---|
| Donut — Subscription % | 73% No, 27% Yes |
| Bar — Revenue by Category | Clothing leads |
| Bar — Sales by Category | Clothing most units |
| Bar — Revenue by Age Group | Young Adults highest |
| Bar — Sales by Age Group | Young Adults most purchases |

---

## Data Model
- Single table: `customer` (3,900 rows, 17 columns after cleaning)
- All visuals connected to same table with cross-filter enabled

---

## DAX Measures Used
```
Total Revenue = SUM(customer[purchase_amount_usd])
Avg Purchase  = AVERAGE(customer[purchase_amount_usd])
Avg Rating    = AVERAGE(customer[review_rating])
Customer Count = COUNTROWS(customer)
```
