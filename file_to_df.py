import pandas as pd
import os
import re
"""
arr=os.listdir("cia_texts")
with open('cia_ufo.csv', 'a') as the_file:
    the_file.write("filename | filetext |\n")
    for filename  in arr:
        f = open('cia_texts/'+filename,"r")
        filename=filename.replace(".txt",'')
        filetext=f.read()
        print(filetext)
        filetext=re.sub(r"\r\n", " ",filetext)
        #print(filename+'|'+filetext+' |\n')
        #print(filetext)

        the_file.write(filename+'|'+filetext+' |\n')

"""
df=pd.read_csv("cia_ufo.csv",sep="|")

print(df['filename'][:100])
