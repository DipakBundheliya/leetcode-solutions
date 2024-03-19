import pandas as pd

def selectData(students) :
    new_df = students[students['student_id']==101]
    new_df.reset_index(inplace=True , drop=True)
    return new_df.drop('student_id' , axis=1)

# Dummy data for test
data = {
        'student_id' : [101,2,3,4,4],
        'age' : [15,11,11,20,1]
    }
df = pd.DataFrame(data)

print(selectData(df))