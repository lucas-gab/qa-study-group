import pandas as pd
import json

with open ('patty_pandas_exercise/students.json') as source_file:
    content = source_file.read()


new_content = json.loads(content)
students_table = pd.DataFrame(new_content)

students_table.to_csv("patty_pandas_exercise/students.csv", index= False)