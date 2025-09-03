# 1. Load the file into a DataFrame and print the first 5 rows.
# 2. Save the DataFrame to a new CSV file called employees_copy.csv.
# 3. Show only the Name column.
# 4. Show the rows for the first three employees.
# 5. Show all employees who work in the "Finance" department.
# 6. Add a new column that calculates each person’s salary after a 10% raise.
# 7. Find the average salary per department.
# 8. Show all employees sorted by age, oldest first.
# 9. Show the dataset where missing values in the Age column are replaced with 0.
# 10. Using this second dataset:

# Department,Location
# HR,New York
# Finance,London
# IT,San Francisco

# combine it with the employees dataset so that each employee also has a location.

import pandas as pd

df = pd.read_csv("employees.csv")

def print_first_five_rows():
    print(df)
    
def load_csv():
    df.to_csv("employees_copy.csv")
    
def name_column():
    print(df["Name"])
    
def rows_first_three_employees():
    print(df.head(3))
    
def all_employees_finance():
    print(print(df[df["Department"] == "Finance"]))
    
#def new_column():
    
#def average_department_salary():
    
#def employees_sorted_age():
    
#def missing_values():
    
#def combine():
all_employees_finance()
