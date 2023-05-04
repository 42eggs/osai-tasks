import pandas as pd

# Read the csv files
employees_df = pd.read_csv(".csv/Employees.csv")
departments_df = pd.read_csv(".csv/Departments.csv")
salaries_df = pd.read_csv(".csv/Salaries.csv")

# Note: _x represents the left table (Departments) and _y represents the right table (Employees)

# Merge Departments and Employees on their Department.ID and Employees."DEPT_ID" using join operations
merged_df = pd.merge(departments_df, employees_df, left_on="ID", right_on="DEPT ID")

# Applying Group By to the salaries table to get average salary per employee
monthly_salaries_df = salaries_df.groupby("EMP_ID")["AMT (USD)"].mean().reset_index()

# Merge Monthly Salaries and the former merged table on Employee.ID and Monthly Salaries."EMP_ID"
merged_df = pd.merge(merged_df, monthly_salaries_df, left_on="ID_y", right_on="EMP_ID")

# Removing the unnecessary columns
merged_df.drop(columns=["ID_x", "DEPT ID"], axis=1, inplace=True)
merged_df.drop(columns=["EMP_ID", "NAME_y", "ID_y"], axis=1, inplace=True)


# Apply group by on Department.NAME and get the average salary per department
result_df = merged_df.groupby("NAME_x")["AMT (USD)"].mean().reset_index()


# Rename the columns
result_df.columns = ["DEPT_NAME", "AVG_MONTHLY_SALARY (USD)"]

# Round the values to 3 decimal places
result_df["AVG_MONTHLY_SALARY (USD)"] = result_df["AVG_MONTHLY_SALARY (USD)"].round(3)

# Sort the values in descending order and get the top 3
# I don't know what I did regarding the index but it worked out fine
result_df = (
    result_df.sort_values(by="AVG_MONTHLY_SALARY (USD)", ascending=False)
    .head(3)
    .reset_index()
    .drop(columns=["index"], axis=1)
)

# Print the result
print(result_df)

# Extra: Save the result to a csv file
result_df.to_csv("result.csv", index=False)

