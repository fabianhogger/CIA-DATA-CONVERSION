import pandas as pd
import os

"""arr = os.listdir('cia_texts')
with open('cia.csv', 'a') as the_file:
    for filename  in arr:
        f = open('cia_texts/'+filename,"r")
        filename=filename.replace(".txt",'')
        filetext=f.read()
        filetext=filetext.replace('|','')
        print(filename.replace(".txt",''))
        print(filetext)
        the_file.write(filename+'|'+filetext+'|')

"""

df=pd.read_csv("cia.csv",header=None,sep="|")
df.columns=["filename","filetext"]
print(df.head())
