import pandas as pd

# Here , we can concate data vertically (row wise , for that axis=0)
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    return pd.concat((df1 , df2) , axis=0)


# Create dummy data for test
data = {
        'student_id' : [1,2,3,4,4],
        'age' : [15,11,11,20,1]
    }
data2 = {
        'student_id' : [5,6],
        'age' : [15,11]
    }

df1 = pd.DataFrame(data)
df2 = pd.DataFrame(data2)
print(concatenateTables(df1 , df2))