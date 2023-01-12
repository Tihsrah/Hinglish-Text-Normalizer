import pandas as pd
from indictrans import Transliterator
from tqdm import tqdm

# stop_word_hin_new=pd.read_csv(r'C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\stop_word_hin_new.csv')
# neg_hin_new=pd.read_csv(r'C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\neg_hin_new.csv')
# pos_hin_new=pd.read_csv(r'C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\pos_hin_new.csv')
# # neg_slang_hinglish=pd.read_csv(r'C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\neg_slang_hinglish.csv')

# stop_word_hin_new=stop_word_hin_new.iloc[:,0].tolist()
# neg_hin_new=neg_hin_new.iloc[:,0].tolist()
# pos_hin_new=pos_hin_new.iloc[:,0].tolist()

# inv_trn = Transliterator(source='hin', target='eng')
# transliterated_dictionary=[]
# dictionary=[stop_word_hin_new,neg_hin_new,pos_hin_new]
# transliterated_dictionary=[]
# for i in tqdm(dictionary):
#     for j in i:
#         res=inv_trn.transform(j)
#         transliterated_dictionary.append(res)
    
# transliterated_dictionary=pd.DataFrame(transliterated_dictionary)
# transliterated_dictionary.to_csv(rf"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\old_hinglish_vocabulary.csv", index=False)

# dupli remove
# dictionary=pd.read_csv(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\old_hinglish_vocabulary.csv",encoding='utf-8')
# dictionary=dictionary.iloc[:,0].tolist()
# duplicate_dictionary=[]
# print(len(dictionary))
# for i in range(len(dictionary)):
#     if dictionary[i] not in duplicate_dictionary:
#         duplicate_dictionary.append(dictionary[i])
# dictionary=duplicate_dictionary
# print(len(dictionary))
# dictionary=pd.DataFrame(dictionary)
# dictionary.to_csv(rf"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\old_hinglish_vocabulary.csv", index=False)
alpha=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
dictionary_all=[]
for j in range(len(alpha)):
    dictionary=pd.read_csv(rf"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\Dictionary_hinglish_new\{alpha[j]}word_hinglish_new.csv", engine="python", sep=',', quotechar='"', error_bad_lines=False,encoding="utf8")
    dictionary=dictionary.iloc[:,0].tolist()
    dictionary_all.extend(dictionary)

dictionary=pd.read_csv(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\old_hinglish_vocabulary.csv",encoding='utf-8')
dictionary=dictionary.iloc[:,0].tolist()
dictionary_all.extend(dictionary)

temp_dictionary_all=[]

for i in dictionary_all:
    try:
        i=float(i)
    except:
        temp_dictionary_all.append(i)
dictionary_all=temp_dictionary_all
# dictionary_all=pd.DataFrame(dictionary_all)
# dictionary_all.to_csv(rf"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\all_hinglish_vocabulary.csv", index=False)
