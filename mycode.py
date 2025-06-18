import pandas as pd
import os

dict = {
    'name':['Unik','Vini','Arda'],
    'city':['Germany','Brazil','Turkey']
}

df = pd.DataFrame(dict)

new_row = {'name':'Trent','city':'Liverpool'}
df.loc[len(df.index)] = new_row

new_rows = {'name':'Dean','city':'Spain'}
df.loc[len(df.index)] = new_rows

data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)
file_path = os.path.join(data_dir,'sample_data.csv')
df.to_csv(file_path,index=False)