import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.iloc[customers['email'].drop_duplicates().index]

# Dummy data for testing
data = {
        'student_id' : [2,3,4,4],
        'email' : ['deep@gmail.com' , 'jay@gmail.com' , 'deep@gmail.com', 'taark@gmail.com']
    }
df = pd.DataFrame(data)

print(dropDuplicateEmails(df))