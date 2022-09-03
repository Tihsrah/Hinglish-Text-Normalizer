import re
import string
from tqdm import tqdm 
import pandas as pd



inappropriate=pd.read_csv(r'C:\Users\HP OMEN\Downloads\archive\Inappropriate words classification.csv')
pos_neg=pd.read_excel(r'C:\Users\HP OMEN\Downloads\pos_neg\Positive and Negative Word List.xlsx')
stop_word=pd.read_csv(r'C:\Users\HP OMEN\Downloads\stopwords-en-master\stopwords-en-master\stopwords-en.txt').iloc[:,0].tolist()
neg=pos_neg['Negative Sense Word List'].dropna().tolist()
pos=pos_neg['Positive Sense Word List'].dropna().tolist()


for i in stop_word:
    if i in pos:
        stop_word.remove(i)
for i in stop_word:
    if i in neg:
        stop_word.remove(i)    

check_data=pd.read_csv(r'C:\Users\HP OMEN\Downloads\sentiment_test\sentiment_no_emoticons.csv',encoding='latin-1')
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
    # removal of url
    non_url=re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", test_data[i])
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
    temp_text=[]
    for i in text:
        if i in stop_word:
            pass
        else:
            temp_text.append(i)
    pos_count=0

    for i in temp_text:
        if i in pos:
            pos_count=pos_count+1

    # checking for negative words
    neg_count=0

    for i in temp_text:
        if i in neg:
            neg_count=neg_count+1

    # calculating emotion of text

    result = pos_count-neg_count

    if(result>0):
        our_result.append(4)
    elif(result==0):
        our_result.append(2)
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

