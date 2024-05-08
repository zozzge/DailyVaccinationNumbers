-- Question 7: Code Implementation Task: If this list would be a database table, please provide SQL query to fill in the missing daily vaccination numbers with discrete median of country as similar to question a.  
--Please  provide the link to your code as answer to this question. 
--Note: This time SQL equivalent is requested, and imputation value is median of each country, not minimum. Please remember filling countries with zero if they do not have any valid daily_vaccination records like Kuwait.

WITH ImputedData AS (
  SELECT 
    country, 
    date, 
    COALESCE(daily_vaccinations, 0) AS daily_vaccinations,
    MEDIAN(daily_vaccinations) OVER (PARTITION BY country) AS median_daily_vaccinations
  FROM 
    vaccination_data
)
SELECT 
  country, 
  date, 
  COALESCE(daily_vaccinations, median_daily_vaccinations) AS daily_vaccinations
FROM 
  ImputedData;

