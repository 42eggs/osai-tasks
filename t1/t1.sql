
-- First I selected the department name and the average salary of each employee.
-- Then I inner joined the department table with the employees table on the department id.
-- Then I joined on a subquery that selects the average salary of each employee (grouped by employee id)
-- After that I got the final table on which I grouped by the department name and ordered by the average salary in descending order.
-- Then I limited the results to the top 3.


SELECT 
    Department.NAME AS DEPT_NAME, 
    ROUND(AVG(Monthly_Salaries.AVG_SALARY), 3) AS "AVG_MONTHLY_SALARY (USD)"
FROM 
    Department 
    JOIN Employees ON Department.ID = Employees."DEPT ID"
    JOIN (
        SELECT 
            EMP_ID,
            AVG("AMT (USD)") AS AVG_SALARY 
        FROM 
            Salaries 
        GROUP BY 
            EMP_ID
    ) Monthly_Salaries ON Employees.ID = Monthly_Salaries.EMP_ID
GROUP BY 
    DEPT_NAME 
ORDER BY 
    "AVG_MONTHLY_SALARY (USD)" DESC 
LIMIT 3;


