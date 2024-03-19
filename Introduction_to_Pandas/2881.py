import pandas as pd

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary']*2
    return employees 

# Dummy data for testing
data = {
        'student_id' : [101,2,3,4,4],
        'salary' : [1500,1100,1100,2000,100]
    }
df = pd.DataFrame(data)

print(createBonusColumn(df))