import re
import string
import pandas as pd
import emoji
from nltk.stem import WordNetLemmatizer
from tqdm import tqdm 



inappropriate=pd.read_csv(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\Inappropriate words classification.csv")
pos_neg=pd.read_excel(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\Positive and Negative Word List.xlsx")
stop_word=pd.read_csv(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\stopwords-en-master\stopwords-en.txt").iloc[:,0].tolist()
neg=pos_neg['Negative Sense Word List'].dropna().tolist()
pos=pos_neg['Positive Sense Word List'].dropna().tolist()



neg_slang=inappropriate[inappropriate["Sentiment Value"]=="Negative"]
neg_slang=neg_slang['Preprocessed Violent toxic words'].dropna().tolist()


pos_slang=inappropriate[inappropriate["Sentiment Value"]=="Positive"]
pos_slang=pos_slang['Preprocessed Violent toxic words'].dropna().tolist()



for i in stop_word:
    if i in pos:
        stop_word.remove(i)
for i in stop_word:
    if i in neg:
        stop_word.remove(i)    

# lemmatizing the datasets.
lemmatizer=WordNetLemmatizer()
pos_new=[]
for i in tqdm(pos):
    pos_new.append(lemmatizer.lemmatize(i))
pos=pos+pos_new
pos=set(pos)
pos=list(pos)
neg_new=[]
for i in neg:
    neg_new.append(lemmatizer.lemmatize(i))
neg=neg+neg_new
neg=set(neg)
neg=list(neg)


# cleaning slangs
print(len(pos_slang))
print(len(neg_slang))

for i in pos:
    if i in pos_slang:
        pos_slang.remove(i)
    # if i in neg_slang:
    #     neg_slang.remove(i)

for i in neg:
    if i in pos_slang:
        pos_slang.remove(i)
    # if i in neg_slang:
    #     neg_slang.remove(i)
new_pos_slang=[]
for i in pos_slang:
    new_pos_slang.append(lemmatizer.lemmatize(i))
pos_slang=pos_slang+new_pos_slang

new_neg_slang=[]
for i in neg_slang:
    new_neg_slang.append(lemmatizer.lemmatize(i))
neg_slang=neg_slang+new_neg_slang
print(len(pos_slang))
print(len(neg_slang))







check_data=pd.read_csv(r"C:\Users\harsh\Downloads\archive\sentiment_no_emoticons.csv",encoding='latin-1')
print(check_data.iloc[:,0].unique())
check_data=check_data[check_data.iloc[:,0] != 2]
print(len(check_data))
# print(check_data[check_data['0'] != 2])
print(check_data.iloc[:,0].unique())
check_data_val=check_data.iloc[:,0].tolist()
# print(check_data_val)

test_data=check_data.iloc[:,5].tolist()
# print(len(test_data))

our_result=[]
for i in tqdm(range(len(test_data))):

    # converting emoji to its meaning
    non_emoji=emoji.demojize(test_data[i])


    # removal of url
    non_url=re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", non_emoji)
    non_url = non_url.strip()

    # hastag removal
    non_hashtag=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",non_url).split())

    # punctuation removal
    non_punctuation = non_hashtag.translate(str.maketrans('', '', string.punctuation))

    # new line and /r removal
    no_newline = non_punctuation.replace('\n', ' ').replace('\r', '')
    # print(no_newline)

    # removal of stop words
    text=no_newline.split()
    print(text)
    temp_text=[]
    for i in text:
        if i in stop_word:
            pass
        else:
            temp_text.append(lemmatizer.lemmatize(i))
     # checking for positive words
    pos_count=0
    pos_slang_count=0
    for i in temp_text:
        if i in pos:
            pos_count=pos_count+1
        if i in pos_slang:
            pos_slang_count=pos_slang_count+1

    # checking for negative words
    neg_count=0
    neg_slang_count=0
    for i in temp_text:
        if i in neg:
            neg_count=neg_count+1
        if i in neg_slang:
            neg_slang_count=neg_slang_count+1

    # calculating emotion of text

    result = pos_count-neg_count+pos_slang_count-neg_slang_count

    if(result>0):
        our_result.append(4)
    else:
        our_result.append(0)
# print(check_data_val)
# print(our_result)

positive_prediction=0
negative_prediction=0
neutral_prediction=0
for i in range(len(our_result)):
    if our_result[i]==check_data_val[i]:
        positive_prediction=positive_prediction+1
    else:
        negative_prediction=negative_prediction+1

print(positive_prediction)
print(negative_prediction)

