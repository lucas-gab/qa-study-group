import pandas as pd


def convert_to_csv(json_file):
    df = pd.DataFrame(json_file)
    df.to_csv('students.csv')


convert_to_csv(pd.read_json('students.json'))
