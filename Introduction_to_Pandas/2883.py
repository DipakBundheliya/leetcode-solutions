import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students[students['name'].isnull() == False]

# Dummy data for testing
data = {
        'student_id' : [1,2,3,4,4],
        'name' : ['dipak' , 'jay' , None , 'harsh' , 'prit']
    }
df = pd.DataFrame(data)

print(dropMissingData(df))