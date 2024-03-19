import pandas as pd

# You can also use rename function of pandas for change specific column name with specific name 
def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.columns = ['student_id' , 'first_name' , 'last_name' , 'age_in_years']
    return students

# It is straightforward to understand how can we rename columns names, so here we do not need to test
# But , you can also check it by your own