import pandas as pd

# In function we can also use head
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.iloc[:3 , :]

# Dummy data for test
data = {
        'student_id' : [1,2,3,4,4],
        'age' : [15,11,11,20,1]
    }
df = pd.DataFrame(data)

print(selectFirstRows(df))