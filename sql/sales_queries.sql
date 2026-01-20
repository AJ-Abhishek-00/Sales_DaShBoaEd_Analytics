-- SQL Queries for Sales Dashboard Analysis

-- 1. Total Revenue and Profit by Region
SELECT 
    Region,
    COUNT(*) as Total_Orders,
    SUM(Revenue) as Total_Revenue,
    SUM(Profit) as Total_Profit,
    ROUND(AVG(Profit_Margin), 2) as Avg_Profit_Margin
FROM sales
GROUP BY Region
ORDER BY Total_Profit DESC;

-- 2. Top 10 Cities by Profit
SELECT 
    City,
    Region,
    COUNT(*) as Orders,
    SUM(Revenue) as Revenue,
    SUM(Profit) as Profit,
    ROUND(SUM(Profit) * 100.0 / SUM(Revenue), 2) as Profit_Margin_Pct
FROM sales
GROUP BY City, Region
ORDER BY Profit DESC
LIMIT 10;

-- 3. Bottom 5 Cities (Underperforming)
SELECT 
    City,
    Region,
    COUNT(*) as Orders,
    SUM(Revenue) as Revenue,
    SUM(Profit) as Profit,
    ROUND(SUM(Profit) * 100.0 / SUM(Revenue), 2) as Profit_Margin_Pct
FROM sales
GROUP BY City, Region
ORDER BY Profit ASC
LIMIT 5;

-- 4. Category Performance Analysis
SELECT 
    Category,
    COUNT(*) as Total_Orders,
    SUM(Quantity) as Units_Sold,
    SUM(Revenue) as Total_Revenue,
    SUM(Profit) as Total_Profit,
    ROUND(AVG(Profit_Margin), 2) as Avg_Margin_Pct
FROM sales
GROUP BY Category
ORDER BY Total_Profit DESC;

-- 5. Top 20 Products by Revenue
SELECT 
    Product,
    Category,
    COUNT(*) as Orders,
    SUM(Quantity) as Units_Sold,
    SUM(Revenue) as Revenue,
    SUM(Profit) as Profit
FROM sales
GROUP BY Product, Category
ORDER BY Revenue DESC
LIMIT 20;

-- 6. Loss-Making Product-City Combinations (Critical!)
SELECT 
    Product,
    Category,
    City,
    Region,
    COUNT(*) as Orders,
    SUM(Revenue) as Revenue,
    SUM(Profit) as Profit,
    ROUND(SUM(Profit) * 100.0 / SUM(Revenue), 2) as Margin_Pct
FROM sales
GROUP BY Product, Category, City, Region
HAVING SUM(Profit) < 0
ORDER BY Profit ASC;

-- 7. Monthly Trend (2024)
SELECT 
    strftime('%Y-%m', Order_Date) as Month,
    COUNT(*) as Orders,
    SUM(Revenue) as Revenue,
    SUM(Profit) as Profit,
    ROUND(AVG(Profit_Margin), 2) as Avg_Margin
FROM sales
WHERE strftime('%Y', Order_Date) = '2024'
GROUP BY Month
ORDER BY Month;

-- 8. Quarterly Performance Comparison
SELECT 
    Year,
    Quarter,
    COUNT(*) as Orders,
    SUM(Revenue) as Revenue,
    SUM(Profit) as Profit
FROM sales
GROUP BY Year, Quarter
ORDER BY Year, Quarter;

-- 9. Sales Representative Performance
SELECT 
    Sales_Rep,
    COUNT(*) as Total_Orders,
    SUM(Revenue) as Total_Revenue,
    SUM(Profit) as Total_Profit,
    ROUND(AVG(Profit_Margin), 2) as Avg_Margin
FROM sales
GROUP BY Sales_Rep
ORDER BY Total_Profit DESC;

-- 10. Customer Segment Analysis
SELECT 
    Customer_Segment,
    COUNT(*) as Orders,
    SUM(Revenue) as Revenue,
    SUM(Profit) as Profit,
    ROUND(SUM(Profit) * 100.0 / SUM(Revenue), 2) as Margin_Pct,
    ROUND(AVG(Revenue), 2) as Avg_Order_Value
FROM sales
GROUP BY Customer_Segment
ORDER BY Profit DESC;

-- 11. Year-over-Year Growth
SELECT 
    Year,
    SUM(Revenue) as Annual_Revenue,
    SUM(Profit) as Annual_Profit,
    COUNT(*) as Total_Orders
FROM sales
GROUP BY Year
ORDER BY Year;

-- 12. High Discount Impact on Profit
SELECT 
    CASE 
        WHEN Discount < 0.10 THEN 'Low (< 10%)'
        WHEN Discount < 0.20 THEN 'Medium (10-20%)'
        ELSE 'High (> 20%)'
    END as Discount_Range,
    COUNT(*) as Orders,
    AVG(Profit_Margin) as Avg_Margin,
    SUM(Profit) as Total_Profit
FROM sales
GROUP BY Discount_Range
ORDER BY Avg_Margin DESC;

-- 13. Region-Category Cross Analysis
SELECT 
    Region,
    Category,
    COUNT(*) as Orders,
    SUM(Revenue) as Revenue,
    SUM(Profit) as Profit
FROM sales
GROUP BY Region, Category
ORDER BY Region, Profit DESC;

-- 14. Top 5 Customers by Revenue (using Order_ID as proxy)
SELECT 
    SUBSTR(Order_ID, 1, 6) as Customer_Code,
    Customer_Segment,
    City,
    COUNT(*) as Orders,
    SUM(Revenue) as Revenue,
    SUM(Profit) as Profit
FROM sales
GROUP BY Customer_Code, Customer_Segment, City
ORDER BY Revenue DESC
LIMIT 5;

-- 15. Products with Negative Profit Margin
SELECT 
    Product,
    Category,
    AVG(Profit_Margin) as Avg_Margin,
    COUNT(*) as Occurrences
FROM sales
WHERE Profit_Margin < 0
GROUP BY Product, Category
ORDER BY Avg_Margin ASC;