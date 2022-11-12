import pandas as pd
from tqdm import tqdm 
import emoji
import re
import string
from googletrans import Translator
from bs4 import BeautifulSoup
data=pd.read_csv(r"C:\Users\harsh\OneDrive - UPES\Desktop\Hinglish\Hinglish_test_unalbelled_conll_updated.txt",sep='\t',engine='python',names=['word','type','class'])
# print(data.to_string())


# converting texts in line 

df1=pd.DataFrame()
text=""
cla=data['class'][0]
j=data['type'][0]
for i in range(1,len(data)):
    if(data['word'][i]=="meta"):
        df1=df1.append({"ID":j,"Text":text,"class":cla},ignore_index=True)
        cla=data['class'][i]
        j=data['type'][i]
        text=""
    else:
        text+=" "+str(data["word"][i])
df1=df1.append({"ID":j,"Text":text,"class":cla},ignore_index=True)
df1.to_csv("timepass.csv")