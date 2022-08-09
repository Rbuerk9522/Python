-- Exploring the Data
Select * From product;
Select * From sales;
Select * From customer;

--Creting the table for my product data
Select a.product_id as Product_ID, a.category as Category, a.sub_category as Sub_Category, b.year as Year, Sum(b.sales) as Sales
From product as a left join (Select product_id, EXTRACT(YEAR FROM order_date) as year, sales FROM sales) as b
on a.product_id = b.product_id
group by a.product_id, a.Category, a.Sub_Category, b.Year
Order by b.Year;

-- Testing my Left Join Statement
Select product_id, EXTRACT(YEAR FROM order_date) AS Year, sales as Sales FROM sales;

-- Checking the data matches
Select * From product
where product_id = 'FUR-BO-10000330';

-- Creating my table for my customer table
Select a.customer_id as Customer_ID, a.customer_name as Customer_Name, a.segment as Customer_Type, a.state as State, a.city as City, a.region as Region, 
b.year as Year, Sum(b.sales) as Sales
From customer as a left join (Select customer_id, EXTRACT(YEAR FROM order_date) as year, sales FROM sales) as b
on a.customer_id = b.customer_id
group by a.customer_id, a.customer_name, a.segment, a.state, a.city, b.Year
Order by b.Year;
