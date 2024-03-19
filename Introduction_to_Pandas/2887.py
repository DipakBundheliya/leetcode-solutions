import pandas as pd

# Here we fill missing values with 0
def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'] = products['quantity'].fillna(0)
    return products 

# Dummy data for testing
data = {
        'quantity' : [1,None,3,4,None],
        'name' : ['dipak' , 'jay' , 'Taarak' , 'harsh' , 'prit']
    }
df = pd.DataFrame(data)

print(fillMissingValues(df))