import pandas as pd
from indictrans import Transliterator
from tqdm import tqdm
import csv
import pickle
pos_neg=pd.read_excel(r'C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\Positive and Negative Word List.xlsx')
stop_word=pd.read_csv(r'C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\stopwords-en-master\stopwords-en.txt').iloc[:,0].tolist()
neg=pos_neg['Negative Sense Word List'].dropna().tolist()
pos=pos_neg['Positive Sense Word List'].dropna().tolist()

english_vocab=[]
for i in [stop_word,neg,pos]:
    for j in i:
        english_vocab.append(j)

alpha=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
for j in range(len(alpha)):
    print(alpha[j])
    dictionary=pd.read_csv(rf"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\Dictionary_eng_temp\{alpha[j]}word_new.csv", engine="python", sep=',', quotechar='"', error_bad_lines=False,encoding='cp1252')
    dictionary=dictionary.iloc[:,0].tolist()
    

    #  duplicates stopwords
    # duplicate_dictionary=[]
    # print(len(dictionary))
    # for i in range(len(dictionary)):
    #     if dictionary[i] not in duplicate_dictionary:
    #         duplicate_dictionary.append(dictionary[i])
    # dictionary=duplicate_dictionary
    # print(len(dictionary))
    # dictionary=pd.DataFrame(dictionary)
    # dictionary.to_csv(rf"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\Dictionary_eng_new\{alpha[j]}word_new.csv", index=False)


        # converting multispaced hinglish data to one word data
    # with open(rf"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\Dictionary_eng_new\{alpha[j]}word_new.csv",encoding="utf-8") as dictionary_hinglish:
    #     reader_obj = csv.reader(dictionary_hinglish)

    #     for i in tqdm(reader_obj):
    #         test=i[0].split()
    #         for k in test:
    #             # print(j)
    #             fhw=open(rf"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\Dictionary_eng_temp\{alpha[j]}word_new.csv",'a',encoding="utf-8")
    #             fhw.write(k+'\n')
    #             fhw.close()
    
    english_vocab.extend(dictionary)
temp_english_vocab=[]
print(len(english_vocab))
# no_integers = [x for x in english_vocab if not (x.isdigit() or x[0] == '-' and x[1:].isdigit())]
print(len(english_vocab))

for i in english_vocab:
    try:
        i=float(i)
    except:
        temp_english_vocab.append(i)

# print("one word",len(english_vocab))
# for i in english_vocab.copy():
#     if len(i)<=1:
#         english_vocab.remove(i)
# print("1 word",len(english_vocab))

# print(temp_english_vocab)
english_vocab=temp_english_vocab

from hinglish_dictionary_collection import *

english_vocab.extend(dictionary_all)
print(len(english_vocab))


english_vocab=pd.DataFrame(english_vocab)
english_vocab.to_csv(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\all_vocabulary.csv", index=False)

# with open("all_vocab.pkl", "rb") as fp:   # Unpickling
#    english = pickle.load(fp)
# english_vocab=english
# english_vocab=pd.DataFrame(english_vocab)
# english_vocab.to_csv(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\all_vocabulary.csv", index=False)


# # create a binary pickle file 
# f = open("all_vocab.pkl","wb")

# # write the python object (dict) to pickle file
# pickle.dump(english_vocab,f)

# # close file
# f.close()