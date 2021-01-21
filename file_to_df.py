import pandas as pd
import os
arr = os.listdir('cia_texts')
with open('cia.csv', 'a') as the_file:
    for filename  in arr:
        f = open('cia_texts/'+filename,"r")
        the_file.write(filename+'|'+f.read()+'\n')

"""

df=pd.read_csv("cia.csv",header=None,sep="|")
print(df.head())
"""
