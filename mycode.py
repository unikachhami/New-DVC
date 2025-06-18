import pandas as pd
import os

dict = {
    'name':['Unik','Vini','Arda'],
    'city':['Germany','Brazil','Turkey']
}

df = pd.DataFrame(dict)

new_row = {'name':'Trent','city':'Liberpool'}
df.loc[len(df.index)] = new_row
data_dir = 'data'
os.makedirs(data_dir,exist_ok=True)
file_path = os.path.join(data_dir,'sample_data.csv')
df.to_csv(file_path,index=False)