#{"username":"tahirismailwala","key":"44c1ab015c92e1b5d776903097232998"}

import tmbd

import os
import pandas as pd
import zipfile


import os
import pandas as pd
import zipfile

# Download the dataset
dataset_name = 'ahmedshahriarsakib/top-1000-twitter-celebrity-accounts'
os.system(f'kaggle datasets download -d {dataset_name}')

# Extract the downloaded .zip file
zip_path = f'{dataset_name.split("/")[-1]}.zip'
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall('.')

# Load the dataset into a Pandas DataFrame
csv_filename = r'C:\Users\tahir\OneDrive\Desktop\Python\finalfantasy\Top-1000-Celebrity-Twitter-Accounts.csv'
df = pd.read_csv(csv_filename)

#displays basic stuff
#print(df.head())

tmbdPeople = tmbd.peopleList()
#print(tmbdPeople)
#print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`````")

df['name'] = df['name'].str.lower()

for i in tmbdPeople:
    for names in df['name']:
        if i == names:
            print(i)

#    print(names)
