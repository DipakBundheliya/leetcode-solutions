import pandas as pd
 
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:  
    # Here , we first get index of those which animal has descening weight and greater than 100
    sort_index = animals[animals['weight']>100]['weight'].sort_values(ascending=False).index
    new_animals = pd.DataFrame(animals.iloc[sort_index]['name'])
    return new_animals


# Create dummy data for test
data = [[ 'Tatiana'  , 'Snake'   , 98 , 464 ],   
[ 'Khaled'   , 'Giraffe' , 50 , 41  ],   
[ 'Alex'     , 'Leopard' , 6  , 328 ],   
[ 'Jonathan' , 'Monkey'  , 45 , 463 ],   
[ 'Stefan'   , 'Bear'    , 100, 50  ],   
[ 'Tommy'    , 'Panda'   , 26 , 349 ]]
df = pd.DataFrame(data , columns=['name', 'species' , 'age' , 'weight'])

# Check result 
print(findHeavyAnimals(df))

