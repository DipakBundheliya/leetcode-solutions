import pandas as pd

# Here we use astype function of pandas for change datatype of specific column
def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    return students.astype({
        'grade' : int
    })

# Dummy data for testing
data = {
    'grade' : [1.0 , 2.0 , 3.0]
}
df = pd.DataFrame(data)

# You can see difference of data type after apply function
print(type(df['grade'][0]))
print(type(changeDatatype(df)['grade'][0]))
