import pandas as pd
from bs4 import BeautifulSoup
import re

# def clean_tweet(tweet):
#     text=re.sub(r'@ [A-Za-z0-9\']+','',tweet)
#     text=BeautifulSoup(text,'lxml').get_text()
#     text=re.sub(r'https (//)[A-Za-z0-9. ]*(/) [A-Za-z0-9]+','',text)
#     text=re.sub(r'https[A-Za-z0-9/. ]*','',text)
#     text=re.sub("[^a-zA-Z]"," ",text)
#     text=re.sub(r'\bRT\b',' ',text)
#     text=re.sub(r'\bnan\b',' ',text)
#     return text

# df1=pd.read_csv(r'timepass.csv')
# df1['Text']=df1['Text'].apply(clean_tweet)
# text=df1['Text'].tolist()
label = pd.read_csv(
    r"C:\Users\harsh\OneDrive - UPES\Desktop\hinglish to english\test translated\labels2_incomplete.csv")
label = label.iloc[:, 0].tolist()
changed_label = []
for i in label:
    if i == 1:
        changed_label.append("neutral")
    if i == 0:
        changed_label.append("negative")
    if i == 2:
        changed_label.append("positive")

original_label = pd.read_csv(
    r"C:\Users\harsh\OneDrive - UPES\Desktop\hinglish to english\Hinglish dataset\Hinglish_test_labels.txt")
original_label = original_label['Sentiment'].tolist()
total = len(original_label)
print(total)
del original_label[1500:1600]
del original_label[2300:2400]
del original_label[2500:2600]
del original_label[2600:2700]
total = len(original_label)
print(total)
print(len(label))
correct = 0
for i in range(len(changed_label)):
    if original_label[i] == changed_label[i]:
        correct = correct+1
print("correct predictions :", correct)
print("Accuracy : ", correct/total)
