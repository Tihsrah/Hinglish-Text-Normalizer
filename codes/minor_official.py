import pandas as pd
from tqdm import tqdm 
import emoji
import re
import string
from bs4 import BeautifulSoup
data=pd.read_csv(r'C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\official dataset\semEval.txt',sep='\t',engine='python',names=['word','type','class'])
# print(data.to_string())


# converting texts in line 

# df1=pd.DataFrame()
# text=""
# cla=data['class'][0]
# j=data['type'][0]
# for i in range(1,len(data)):
#     if(data['word'][i]=="meta"):
#         df1=df1.append({"ID":j,"Text":text,"class":cla},ignore_index=True)
#         cla=data['class'][i]
#         j=data['type'][i]
#         text=""
#     else:
#         text+=" "+str(data["word"][i])
# df1=df1.append({"ID":j,"Text":text,"class":cla},ignore_index=True)
# df1.to_csv("texts.csv")

df1=pd.read_csv(r'texts.csv')

print(df1)

# for i in tqdm(range(5)):

#     # converting emoji to its meaning
#     non_emoji=emoji.demojize(df1.iloc[i:2])


#     # removal of url
#     non_url=re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", non_emoji)
#     non_url = non_url.strip()

#     # hastag removal
#     non_hashtag=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",non_url).split())

#     # punctuation removal
#     non_punctuation = non_hashtag.translate(str.maketrans('', '', string.punctuation))

#     # new line and /r removal
#     no_newline = non_punctuation.replace('\n', ' ').replace('\r', '')
#     print(no_newline)

# def clean_tweet(tweet):
#     text=re.sub(r'@[A-Za-z0-9]+','',tweet)
#     text=BeautifulSoup(text,'lxml').get_text()
#     text=re.sub("[^a-zA-Z]"," ",text)

#     return text

def clean_tweet(tweet):
    text=re.sub(r'@ [A-Za-z0-9\']+','',tweet)
    text=BeautifulSoup(text,'lxml').get_text()
    text=re.sub(r'https (//)[A-Za-z0-9. ]*(/) [A-Za-z0-9]+','',text)
    text=re.sub(r'https[A-Za-z0-9/. ]*','',text)
    text=re.sub("[^a-zA-Z]"," ",text)
    text=re.sub(r'\bRT\b',' ',text)
    text=re.sub(r'\bnan\b',' ',text)


    return text

df1['Text']=df1['Text'].apply(clean_tweet)

print(df1['Text'])