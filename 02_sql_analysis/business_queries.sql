

--  Male vs Female customers ka total revenue
SELECT 
    gender,
    SUM([purchase_amount_(usd)]) AS total_revenue
FROM customer
GROUP BY gender;

--  Customer Discount use kiya aur average se zyada spend kiya
SELECT 
    customer_id,
    [purchase_amount_(usd)]
FROM customer
WHERE discount_applied = 'Yes'
AND [purchase_amount_(usd)] > (
    SELECT AVG([purchase_amount_(usd)]) FROM customer
);

--  Top 5 products with highest average review rating
SELECT TOP 5
    item_purchased, 
    AVG(review_rating) AS average_product_rating
FROM customer 
GROUP BY item_purchased
ORDER BY AVG(review_rating) DESC;

-- Standard vs Express Shipping – Average Purchase Comparison
SELECT 
    shipping_type,
    ROUND(AVG([purchase_amount_(usd)]), 2) AS average_purchase
FROM customer
WHERE shipping_type IN ('Express', 'Standard')
GROUP BY shipping_type;

--  Subscribers vs Non-Subscribers – Spend Comparison
SELECT 
    subscription_status,
    COUNT(customer_id) AS total_customer,
    AVG([purchase_amount_(usd)]) AS avg_spend,
    SUM([purchase_amount_(usd)]) AS total_revenue
FROM customer
GROUP BY subscription_status
ORDER BY total_revenue DESC, avg_spend DESC;

--  Top 5 products with highest % of discounted purchases
SELECT TOP 5
    item_purchased,
    ROUND(
        SUM(CASE WHEN discount_applied = 'Yes' THEN 1 ELSE 0 END) 
        * 100.0 / COUNT(*),
        2
    ) AS discount_rate
FROM customer
GROUP BY item_purchased
ORDER BY discount_rate DESC;

--  Customer Segmentation (New / Returning / Loyal)
WITH customer_type AS (
    SELECT
        customer_id,
        previous_purchases,
        CASE
            WHEN previous_purchases = 1 THEN 'New'
            WHEN previous_purchases BETWEEN 2 AND 10 THEN 'Returning'
            ELSE 'Loyal'
        END AS customer_segment
    FROM customer
)
SELECT 
    customer_segment, 
    COUNT(*) AS number_of_customers
FROM customer_type
GROUP BY customer_segment;

--  Each category ke Top 3 most purchased products
WITH item_counts AS (
    SELECT
        category,
        item_purchased,
        COUNT(customer_id) AS total_orders,
        ROW_NUMBER() OVER (
            PARTITION BY category
            ORDER BY COUNT(customer_id) DESC
        ) AS item_rank
    FROM customer
    GROUP BY category, item_purchased
)
SELECT
    category,
    item_purchased,
    total_orders
FROM item_counts
WHERE item_rank <= 3
ORDER BY category, total_orders DESC;

--  Repeat buyers (>5 purchases) subscribe karte hain?
SELECT
    subscription_status,
    COUNT(*) AS repeat_buyers,
    ROUND(
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER (), 
        2
    ) AS percentage
FROM customer
WHERE previous_purchases > 5
GROUP BY subscription_status;

--  Revenue contribution of each age group
SELECT
    age,
    SUM([purchase_amount_(usd)]) AS total_revenue
FROM customer
GROUP BY age
ORDER BY total_revenue DESC;

-- View all customer data
SELECT * FROM customer;
