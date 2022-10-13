import pandas as pd

# Create DataFrame from .json and print to view the data structure
students_df = pd.read_json("students.json")
print(students_df)

# Convert DataFrame to .csv
students_df.to_csv("cameron_students_export.csv")

