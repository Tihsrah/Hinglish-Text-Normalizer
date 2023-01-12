import pandas as pd
import pickle
from  minor_methods import *
from tqdm import tqdm
from Levenshtein import distance as lev
import joblib
from googletrans import Translator
from indictrans import Transliterator
from bs4 import BeautifulSoup
import re

translator = Translator()
trn = Transliterator(source='eng', target='hin')

# english_vocab=pd.read_csv(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\all_english_vocabulary.csv",engine="python", sep=',', quotechar='"', error_bad_lines=False)
# hinglish_vocab=pd.read_csv(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\all_hinglish_vocabulary.csv",engine="python", sep=',', quotechar='"', error_bad_lines=False)
# english_vocab=english_vocab.iloc[:,0].tolist()
# hinglish_vocab=hinglish_vocab.iloc[:,0].tolist()

# english_vocab=create_dictionary(english_vocab)
# hinglish_vocab=create_dictionary(hinglish_vocab)

# print(english_vocab)
# print(hinglish_vocab)


# create a binary pickle file 
# f = open("hinglish_vocab.pkl","wb")

# # write the python object (dict) to pickle file
# pickle.dump(hinglish_vocab,f)

# # close file
# f.close()

with open("english_vocab.pkl", "rb") as fp:   # Unpickling
   english = pickle.load(fp)
hinglish_vocab=english
with open("hinglish_vocab.pkl", "rb") as fp:   # Unpickling
   hinglish = pickle.load(fp)
english_vocab=hinglish
# print(len(english_vocab))
# print(len(hinglish_vocab))
# print("good" in english_vocab.values())
# print("good" in hinglish_vocab.values())

# duplicate removal

# for val in tqdm(english_vocab.values()):
#     for valh in hinglish_vocab.values():
#         for i in val:
#             for j in valh:
#                 if i==j:
#                     try:
#                         val.remove(i)
#                     except:
#                         pass
# print("good" in english_vocab.values())
# print("good" in hinglish_vocab.values())

# print(len(english_vocab))
# print(len(hinglish_vocab))
def clean_tweet(tweet):
    text=re.sub(r'@ [A-Za-z0-9\']+','',tweet)
    text=BeautifulSoup(text,'lxml').get_text()
    text=re.sub(r'https (//)[A-Za-z0-9. ]*(/) [A-Za-z0-9]+','',text)
    text=re.sub(r'https[A-Za-z0-9/. ]*','',text)
    text=re.sub("[^a-zA-Z]"," ",text)
    text=re.sub(r'\bRT\b',' ',text)
    text=re.sub(r'\bnan\b',' ',text)
    return text

df1=pd.read_csv(r'timepass.csv')
df1['Text']=df1['Text'].apply(clean_tweet)
total_text=df1['Text'].tolist()
total_translated=[]
test_text=["tum bhai kaise ho all good?"]
for i in tqdm(test_text):
    test_text=i.split()
    # print(test_text)
    changed_text=[]
    changed_idx=[]
    print(changed_text)
    for i in range(len(test_text)):
        for key in english_vocab:
            done=0
            for val in  english_vocab[key]:
                if(test_text[i]==val):
                    # print("KEY = ",key,"VAL =",val,"i =",test_text[i],"ADJENCENCY_DATA =",adjacency_data[key])
                    print(key,val)
                    changed_text.append(key)
                    changed_idx.append(i)
                    done=1
                    # print("breaking")
                    break
            if done==1:
                # print("breaking again")
                break
    print(changed_text)
    print(changed_idx)
    for i in test_text:
        for j in changed_text:
            dist=lev(i,j)
            print(i,j)
            print(dist)
            if i not in changed_text and dist>=2:
                for key in hinglish_vocab:
                    done=0
                    for val in  hinglish_vocab[key]:
                        if(i==val):
                            idx=test_text.index(i)
                            changed_text.insert(idx,key)
                            changed_idx.insert(idx,idx)
                            # print("hinglish distance wala")
                            # print("abhi ye dekh rha hu",i,val)
                            # print(idx)

                            # print(changed_text)
                            # print(changed_idx)
                            done=1
                            break
                    if done==1:
                        break
            break
    print(changed_text)
    print(changed_idx)
    # for i in test_text:
    #     if i not in changed_text:
    #         idx=test_text.index(i)
    #         changed_text.insert(idx,i)
    #         changed_idx.insert(idx,idx)
    # print(changed_text)
    # print(changed_idx)
        

    # for key in english_vocab:
    #      for val in  english_vocab[key]:
    #         for i in range(len(test_text)):
    #             if(test_text[i]==val):
    #                 # print("KEY = ",key,"VAL =",val,"i =",test_text[i],"ADJENCENCY_DATA =",adjacency_data[key])
    #                 print(key,val)
    #                 changed_text.append(key)
    #                 changed_idx.append(i)
    normalized_string=[]
    # print(changed_text)
    # print(changed_idx)
    res = {}
    for key in changed_idx:
        for value in changed_text:
            res[key] = value
            changed_text.remove(value)
            break
    print(res)
    for i in range(len(res)):
        try:
            normalized_string.append(res[i])
        except:
            normalized_string.append(test_text[i])
    print(normalized_string)

    # changed_text2=[]
    # changed_idx2=[]
    # for i in range(len(normalized_string)):
    #     for key in hinglish_vocab:
    #         done=0
    #         for val in  hinglish_vocab[key]:
    #             if(test_text[i]==val):
    #                 # print("KEY = ",key,"VAL =",val,"i =",test_text[i],"ADJENCENCY_DATA =",adjacency_data[key])
    #                 # print(key,val)
    #                 changed_text2.append(key)
    #                 changed_idx2.append(i)
    #                 done=1
    #                 # print("breaking")
    #                 break
    #         if done==1:
    #             # print("breaking again")
    #             break
    # print(changed_text2)
    # print(changed_idx2)

    # sentence tagging
    classifier=joblib.load(r"classifer.joblib")
    classify=[]
    for i in normalized_string:
        test_classify=classifier(i)
        classify.append(test_classify[0].get("label"))
    print(normalized_string)
    print(classify)

    for i in range(len(classify)):
        if classify[i]=='en':
            try:
                normalized_string[i]=translator.translate(normalized_string[i] ,src='en',dest='hi').text
            except:
                normalized_string[i]="delete"
    print(normalized_string)


    conversion_list=[]
    c=0
    for i in tqdm(normalized_string):
        conversion_list.append(trn.transform(i))
    print(conversion_list)

    string=""
    sentence=[]
    for i in conversion_list:
        string=string+' '+i
    sentence.append(string)
    translated=[]
    for i in tqdm(sentence):
        try:
            translated_text = translator.translate(i ,src='hi',dest='en')
            translated.append(translated_text.text)
        except:
            translated.append("delete")
    print(translated)
    total_translated.append(translated[0])
    # inv_trn = Transliterator(source='hin', target='eng')
    # for i in tqdm(conversion_list):
    #     translated.append(inv_trn.transform(i))
    print(translated)
total_translated=pd.DataFrame(total_translated)
total_translated.to_csv("total_translated.csv", index=False)