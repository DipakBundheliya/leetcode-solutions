import pandas as pd

# Function for create dataframe
def createDataframe(student_data):
    df= pd.DataFrame(student_data)
    df.columns = ['student_id' , 'age']
    return df

# Create data
data = {
        'student_id' : [1,2,3,4,4],
        'age' : [15,11,11,20,1]
}

print(createDataframe(data))