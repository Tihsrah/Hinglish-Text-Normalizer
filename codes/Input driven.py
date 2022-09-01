import re
import string
import pandas as pd

inappropriate=pd.read_csv(r'C:\Users\HP OMEN\Downloads\archive\Inappropriate words classification.csv')
pos_neg=pd.read_excel(r'C:\Users\HP OMEN\Downloads\pos_neg\Positive and Negative Word List.xlsx')
stop_word=pd.read_csv(r'C:\Users\HP OMEN\Downloads\stopwords-en-master\stopwords-en-master\stopwords-en.txt').iloc[:,0].tolist()
neg=pos_neg['Negative Sense Word List'].dropna().tolist()
pos=pos_neg['Positive Sense Word List'].dropna().tolist()


# print("good" in stop_word)
# print(inappropriate)


text=input()

# removing url
# non_url = re.sub(r'\w+:\/{2}[\d\w-]+(\.[\d\w-]+)*(?:(?:\/[^\s/]*))*', '', text)
non_url=re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''', " ", text)
non_url = non_url.strip()

# hastag removal
non_hashtag=' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",non_url).split())


# punctuation removal
non_punctuation = non_hashtag.translate(str.maketrans('', '', string.punctuation))



# new line and /r removal
no_newline = non_punctuation.replace('\n', ' ').replace('\r', '')
print(no_newline)

# removal of stop words
text=no_newline.split()
temp_text=[]
for i in text:
    if i in stop_word:
        pass
    else:
        temp_text.append(i)
print("temp text: ",temp_text)
text=temp_text
# checking for positive words
pos_count=0

for i in text:
    if i in pos:
        print(i)
        pos_count=pos_count+1

# checking for negative words
neg_count=0

for i in text:
    if i in neg:
        neg_count=neg_count+1

# calculating emotion of text

result = pos_count-neg_count
print(pos_count)
print(neg_count)
print(text)

if(result>0):
    print("positive")
else:
    print("negative")