import pandas as pd
from tqdm import tqdm 
import emoji
import re
import string
from googletrans import Translator
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

# print(df1)

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
print(df1['Text'].iloc[10])
test_text="mai thak gya hu"
# print(test_text)
import Levenshtein
from  minor_hinglish import adjacency_data
# print(adjacency_data)
from pyphonetics import RefinedSoundex
rs = RefinedSoundex()
for i in list(adjacency_data):
    if i.isnumeric():
        del adjacency_data[i]

print(adjacency_data)
for i in adjacency_data:
    # m=Levenshtein.distance('ka',i)
    # print(m,i)
    # if(len(i)<4):
    try:
        print(rs.distance(i,'ka'),i)
    except:
        print("exception occured")
    # pass
# print(adjacency_data)




# print(test_text)
test_text=test_text.split()
# print(test_text)
changed_text=[]
changed_idx=[]
for key in adjacency_data:
     for val in  adjacency_data[key]:
        for i in range(len(test_text)):
            if(test_text[i]==val):
                # print("KEY = ",key,"VAL =",val,"i =",test_text[i],"ADJENCENCY_DATA =",adjacency_data[key])
                changed_text.append(key)
                changed_idx.append(i)
normalized_string=""
# print(changed_text)
for i in changed_idx:
    pop_index=changed_text.pop(0)
    normalized_string = test_text[:i] + [pop_index] + test_text[i + 1:]

# transliterating hinglish to devnagri
from hinglish_to_devnagri import hing_to_dev
dev_transliterated_text=hing_to_dev(normalized_string)
dev_transliterated_text=dev_transliterated_text.split()
# print(dev_transliterated_text)
# empty=""
# for i in dev_transliterated_text:
#     empty=empty+" "+ i 
# empty=[empty]
# print(empty)
# english translation
translator = Translator()

translated=[]
for i in tqdm(dev_transliterated_text):
    translated_text = translator.translate(i ,src='hi',dest='en')
    translated.append(translated_text.text)
    # print(translated)
# df=pd.DataFrame(translated)
# df.to_csv('bhavy_data.csv')
# print(translated)