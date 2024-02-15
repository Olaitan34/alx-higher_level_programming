-- Import in hbtn_0c_0 database this table dump
SELECT city, AVG(value) as avg_temp FROM temperatures where month=7 or month=8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
