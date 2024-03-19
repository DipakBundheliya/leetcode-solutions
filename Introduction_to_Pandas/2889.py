import pandas as pd

# Here I have create my own pivot function according to leetcode problem , 
# You can use pivot method of pandas also
  
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:

    new_df = pd.DataFrame()
    new_df['month'] = weather['month'].drop_duplicates().sort_values()
    new_df.reset_index(inplace=True , drop=True)
    city_name = weather['city'].drop_duplicates().sort_values()

    for col in city_name:
        new_df[col] = new_df.apply(lambda row : weather[(weather['month']==row['month']) & (weather['city'] == col)]['temperature'].values[0]  , axis=1)
    new_df.set_index('month' , inplace=True)
    return new_df

# Create dummy data for testing

data3 = {
    'city' : ['Jacksonville' , 'Jacksonville' ,'Jacksonville' , 'Jacksonville' , 'Jacksonville',
              'ElPaso' , 'ElPaso' , 'ElPaso' , 'ElPaso' , 'ElPaso'],
    'month' : ['January',   
                'February' ,
                'March'    ,
                'April'    ,
                'May'      ,
                'January'  ,
                'February' ,
                'March'    ,
                'April',
                'May'  ]     ,
    'temperature' : [13,23,38,5,34,20,6,26,2,43]                            
}

df = pd.DataFrame(data3)
print(pivotTable(df))

