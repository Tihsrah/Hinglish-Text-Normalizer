import pandas as pd
import pickle
from  minor_methods import *
from tqdm import tqdm
from Levenshtein import distance as lev
import joblib
from googletrans import Translator
from indictrans import Transliterator
from pyphonetics import RefinedSoundex
import enchant
from bs4 import BeautifulSoup
import re


dictn = enchant.Dict("en_US")
rs = RefinedSoundex()
normalized_string_final=[]
translator = Translator()
trn = Transliterator(source='eng', target='hin')

with open("updated_vocab\english_vocab2.pkl", "rb") as fp:   # Unpickling
   english = pickle.load(fp)
english_vocab=english 
with open("updated_vocab\hinglish_vocab2.pkl", "rb") as fp:   # Unpickling
   hinglish = pickle.load(fp)
hinglish_vocab=hinglish 

english_vocab['and'] = ['and']
english_vocab['is'] = ['is']

def clean_tweet(tweet):
    text=re.sub(r'@ [A-Za-z0-9\']+','',tweet)
    text=BeautifulSoup(text,'lxml').get_text()
    text=re.sub(r'https (//)[A-Za-z0-9. ]*(/) [A-Za-z0-9]+','',text)
    text=re.sub(r'https[A-Za-z0-9/. ]*','',text)
    text=re.sub("[^a-zA-Z]"," ",text)
    text=re.sub(r'\bRT\b',' ',text)
    text=re.sub(r'\bnan\b',' ',text)
    return text

# df1=pd.read_csv(r"C:\Users\harsh\Downloads\dataset\test.csv")
# df1=pd.read_csv(r'timepass.csv')
# df1['Text']=df1['Text'].apply(clean_tweet)
# df1['Text']=df1['Text'].apply(clean_tweet)
# total_text=df1['Text'].tolist()
# total_text=total_text[100:200]

# total_text=df1.iloc[:,0].tolist()

total_translated=[]
# print(english_vocab["of"])
test_text=["tum bhai kaise ho all good?"]
for i in tqdm(test_text):
    test_text=i.split()

    # english word change from vocab
    not_changed_idx=[]
    for i in range(len(test_text)):
        not_changed_idx.append(0)
    
    changed_text=[]
    changed_idx=[]
    print("1st",changed_text)
    for i in range(len(test_text)):

        for key in english_vocab:
            done=0
            for val in  english_vocab[key]:
                if(test_text[i]==val):
                    # print("KEY = ",key,"VAL =",val,"i =",test_text[i],"ADJENCENCY_DATA =",adjacency_data[key])
                    print("yahan par",key,val,test_text[i])
                    changed_text.append(key)
                    changed_idx.append(i)
                    not_changed_idx[i]=1
                    done=1
                    # print("breaking")
                    break
            if done==1:
                # print("breaking again")
                break
    # print(not_changed_idx)
    # for i in test_text:
    #     for j in changed_text:
    #         # dist=lev(i,j)
    #         # print(dist)
    #         if i not in changed_text:
    #             for key in english_vocab:
    #                 done=0
    #                 for val in  english_vocab[key]:
    #                     if(i==val):
    #                         idx=test_text.index(i)
    #                         changed_text.insert(idx,key)
    #                         changed_idx.insert(idx,idx)
    #                         done=1
    #                         break
    #                 if done==1:
    #                     break
    #         break
    # print("2nd",changed_text)
    # print("2nd",changed_idx)
    # for i in test_text:
    #     if i not in changed_text:
    #         idx=test_text.index(i)
    #         changed_text.insert(idx,i)
    #         changed_idx.insert(idx,idx)
    print(changed_text)
    print(changed_idx)
        

    # for key in english_vocab:
    #      for val in  english_vocab[key]:
    #         for i in range(len(test_text)):
    #             if(test_text[i]==val):
    #                 # print("KEY = ",key,"VAL =",val,"i =",test_text[i],"ADJENCENCY_DATA =",adjacency_data[key])
    #                 print(key,val)
    #                 changed_text.append(key)
    #                 changed_idx.append(i)
    normalized_string=[]
    # print("3rd",changed_text)
    # print("3rd",changed_idx)
    

    # making changed text and idx to a dictionary with two lists
    res = dict(zip(changed_idx, changed_text))
    print(res)
    for i in range(len(test_text)):
        try:
            normalized_string.append(res[i])
        except:
            normalized_string.append(test_text[i])
    # print(normalized_string)


    # hinglish word change
    test_list = [i for i in range(len(test_text))]
    changed_hing_idx = [i for i in test_list if i not in changed_idx]
    # print(changed_hing_idx)
    hinglish_text_part=[]
    for i in changed_hing_idx:
        try:
            hinglish_text_part.append(test_text[i])
        except:
            pass
    print(hinglish_text_part)

    changed_text2=[]
    changed_idx2=[]
    print("1st hing",changed_text2)
    for i in range(len(hinglish_text_part)):

        for key in hinglish_vocab:
            done=0
            for val in  hinglish_vocab[key]:
                if(hinglish_text_part[i]==val):
                    # print("KEY = ",key,"VAL =",val,"i =",test_text[i],"ADJENCENCY_DATA =",adjacency_data[key])
                    print(key,val,hinglish_text_part[i])
                    changed_text2.append(key)
                    changed_idx2.append(i)
                    not_changed_idx[i]=1
                    done=1
                    # print("breaking")
                    break
            if done==1:
                # print("breaking again")
                break
    # print(not_changed_idx)
    # for i in hinglish_text_part:
    #     for j in changed_text2:
    #         # dist=lev(i,j)
    #         # print(i,j,dist)
    #         if i not in changed_text2:
    #             for key in hinglish_vocab:
    #                 done=0
    #                 for val in  hinglish_vocab[key]:
    #                     if(i==val):
    #                         idx=hinglish_text_part.index(i)
    #                         changed_text2.insert(idx,key)
    #                         changed_idx2.insert(idx,idx)
    #                         done=1
    #                         break
    #                 if done==1:
    #                     break
    #         break
    # print("2nd hing",changed_text2)
    # print("2nd hing",changed_idx2)













    # making changed text and idx to a dictionary with two lists
    normalized_string2=[]
    print("changed_text 2 ",changed_text2)
    res2 = dict(zip(changed_idx2, changed_text2))
    print(res2)
    for i in range(len(hinglish_text_part)):
        try:
            normalized_string2.append(res2[i])
        except:
            normalized_string2.append(hinglish_text_part[i])
    print("normalised string 2 :",normalized_string2)
    changed_idx=list(set(changed_idx))
    changed_idx.sort()
    print("changed idx",changed_idx)
    for i in changed_idx:
        normalized_string2.append(res[i])

    print(normalized_string2)
    print(not_changed_idx)


    # finding phoneme and leventise distance for unchanged word
    
    for i in range(len(not_changed_idx)):
        try:
            if not_changed_idx[i]==0:
                eng_phoneme_correction=[]
                for j in english_vocab:
                    # print(normalized_string2[i],j)
                    try:
                        phoneme=rs.distance(normalized_string2[i],j)
                    except:
                        pass
                    if phoneme<=1:
                        eng_phoneme_correction.append(j)
                eng_lev_correction=[]
                for k in eng_phoneme_correction:
                    dist=lev(normalized_string2[i],k)
                    if dist <=2:
                        eng_lev_correction.append(k)
                print(eng_phoneme_correction)
                print(eng_lev_correction)


                hing_phoneme_correction=[]
                for j in hinglish_vocab:
                    try:
                        phoneme=rs.distance(normalized_string2[i],j)
                    except:
                        pass
                    if phoneme<=1:
                        hing_phoneme_correction.append(j)
                hing_lev_correction=[]
                for k in hing_phoneme_correction:
                    dist=lev(normalized_string2[i],k)
                    if dist <=2:
                        hing_lev_correction.append(k)
                print(hing_phoneme_correction)
                print(hing_lev_correction)

                eng_lev_correction.extend(hing_lev_correction)
                new_correction=eng_lev_correction
                eng_lev_correction=[]
                # hing_lev_correction=[]
                print(eng_lev_correction)
                
                for l in new_correction:
                    dist=lev(normalized_string2[i],l)
                    eng_lev_correction.append(dist)
                min_val=min(eng_lev_correction)
                min_idx=eng_lev_correction.index(min_val)

                
                suggestion=dictn.suggest(new_correction[min_idx])
                suggestion_lit=[]
                for t in suggestion:
                    dist=lev(new_correction[min_idx],t)
                    suggestion_lit.append(dist)
                min_suggestion_val=min(suggestion_lit)
                min_suggestion_idx=suggestion_lit.index(min_suggestion_val)
                print("Suggestions : ",min_suggestion_val)
                print(suggestion[min_suggestion_idx])



                normalized_string2[i]=suggestion[min_suggestion_idx]
        except:
            pass
    normalized_string=normalized_string2
    normalized_string_final=normalized_string2
# normalized_string_final=pd.DataFrame(normalized_string_final)
# normalized_string_final.to_csv("normalized_string_final.csv", index=False)    
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

    for i in tqdm(normalized_string):
        conversion_list.append(trn.transform(i))
    print(conversion_list)

    string=""
    sentence=[]
    for i in conversion_list:
        string=i+' '+string
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
total_translated.to_csv("total_translated2.csv", index=False)