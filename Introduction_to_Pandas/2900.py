import pandas as pd

# Here I have create my own melt function according to leetcode problem , 
# You can use melt method of pandas also

def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    new_data = [] 
    for j in report.columns[1:]:
        for i in report['product']:
            new_data.append([i , j , report[(report['product']==i)][j].values[0]]) 
    new_df = pd.DataFrame(new_data,columns=['product' ,'quarter' ,'sales'])
    return new_df

# Craete dummy data for testing
data4 = [
    [ "Umbrella"     , 417 , 224 , 379 , 611],       
    ["SleepingBag"  , 800 , 936 , 93  , 875]
]
report = pd.DataFrame(data4 , columns=['product' , 'quarter_1' , 'quarter_2' , 'quarter_3' , 'quarter_4' ])
print(meltTable(report))
