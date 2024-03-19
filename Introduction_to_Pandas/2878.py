import pandas as pd

def getDataframeSize(players):
    return [players.shape[0] , players.shape[1]]

# Create dummy data for test
data = {
        'student_id' : [1,2,3,4,4],
        'age' : [15,11,11,20,1]
    }
df = pd.DataFrame(data)

# Check output
print(getDataframeSize(df))