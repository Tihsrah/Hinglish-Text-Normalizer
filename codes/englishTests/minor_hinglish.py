
# import the module
import pandas as pd
# from indic_transliteration import sanscript
# from indic_transliteration.sanscript import transliterate
# from gingerit.gingerit import GingerIt
from googletrans import Translator
from tqdm import tqdm 

stop_word=pd.read_csv(r'C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\stop_word.csv')
neg=pd.read_csv(r'C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\neg.csv')
pos=pd.read_csv(r'C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\pos.csv')
neg_slang=pd.read_csv(r'C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\neg_slang.csv')

stop_word=stop_word.iloc[:,0].tolist()
neg=neg.iloc[:,0].tolist()
pos=pos.iloc[:,0].tolist()
neg_slang=neg_slang.iloc[:,0].tolist()

pos_hin=[]
neg_hin=[]
neg_slang_hin=[]
stop_word_hin=[]

translator = Translator()


# for i in pos:

# for i in tqdm(pos):
#     translated_text = translator.translate(i ,src='en',dest='hi')
#     pos_hin.append(translated_text.text)

# for i in tqdm(neg):
#     try:
#         translated_text = translator.translate(i ,src='en',dest='hi')
#     except:
#         print("exception happened")
#     neg_hin.append(translated_text.text)

# for i in tqdm(stop_word):
#     try:
#         translated_text = translator.translate(i ,src='en',dest='hi')
#     except:
#         print("exception happened")
#     stop_word_hin.append(translated_text.text)

# for i in tqdm(neg_slang):
#     try:
#         translated_text = translator.translate(i ,src='en',dest='hi')
#     except:
#         print("exception happened")
#     neg_slang_hin.append(translated_text.text)

# for i in tqdm(neg_slang):
#     translated_text = translator.translate(i ,src='en',dest='hi')
#     neg_slang_hin.append(translated_text.text)

# pos_hin=pd.DataFrame(pos_hin)
# pos_hin.to_csv(r'datasets\converted\pos_hin.csv', index=False)

# neg_hin=pd.DataFrame(neg_hin)
# neg_hin.to_csv(r'datasets\converted\neg_hin.csv', index=False)

# stop_word_hin=pd.DataFrame(stop_word_hin)
# stop_word_hin.to_csv(r'C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\new_stop_word_hin.csv',sep=",", index=False)

# neg_slang_hin=pd.DataFrame(neg_slang_hin)
# neg_slang_hin.to_csv(r'datasets\converted\neg_slang_hin.csv', index=False)

'''

# the text to be transliterated
text = "Tum ussey pyar kyu nahi karti?"
        

# Apa sabhii kaa yahaan svaagat hai.
# printing the transliterated text
transliterated_text=transliterate(text, sanscript.ITRANS, sanscript.DEVANAGARI)
print(transliterated_text)



translator = Translator()

translated_text = translator.translate(transliterated_text)
print(translated_text.text)

# from gingerit.gingerit import GingerIt

# text = 'The smelt of fliwers bring back memories.'

# parser = GingerIt()
# print(parser.parse(text))

'''


import csv
# with open(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\stop_word_hinglish.csv") as stop_word_hinglish:
#     reader_obj = csv.reader(stop_word_hinglish)

#     for i in reader_obj:
#         test=i[0].split()
#         for j in test:
#             # print(j)
#             fhw=open(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\new_stop_word_hinglish.csv",'a')
#             fhw.write(j+'\n')
#             fhw.close()

# with open(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\stop_word_hin.csv",encoding = 'utf-8', errors='ignore') as stop_word_hinglish:
#     reader_obj = csv.reader(stop_word_hinglish)

#     for i in reader_obj:
#         test=i[0].split()
#         for j in test:
#             # print(j)
#             fhw=open(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\new_stop_word_hin.csv",'a',encoding = 'utf-8', errors='ignore')
#             fhw.write(j+'\n')
#             fhw.close()

# with open(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\stop_word_hinglish.csv") as stop_word_hinglish:
#     reader_obj = csv.reader(stop_word_hinglish)

#     for i in reader_obj:
#         test=i[0].split()
#         for j in test:
#             # print(j)
#             fhw=open(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\stop_word_hinglish_new.csv",'a')
#             fhw.write(j+'\n')
#             fhw.close()

# with open(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\stop_word_hin.csv",encoding = 'utf-8', errors='ignore') as stop_word_hinglish:
#     reader_obj = csv.reader(stop_word_hinglish)
#     for i in reader_obj:
#         test=i[0].split()
#         for j in test:
#             # print(j)
#             fhw=open(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\stop_word_hin_new.csv",'a',encoding = 'utf-8', errors='ignore')
#             fhw.write(j+'\n')
#             fhw.close()

# # 
# with open(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\neg_hinglish.csv") as stop_word_hinglish:
#     reader_obj = csv.reader(stop_word_hinglish)

#     for i in reader_obj:
#         test=i[0].split()
#         for j in test:
#             # print(j)
#             fhw=open(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\neg_hinglish_new.csv",'a')
#             fhw.write(j+'\n')
#             fhw.close()

# with open(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\neg_hin.csv",encoding = 'utf-8', errors='ignore') as stop_word_hinglish:
#     reader_obj = csv.reader(stop_word_hinglish)

#     for i in reader_obj:
#         test=i[0].split()
#         for j in test:
#             # print(j)
#             fhw=open(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\neg_hin_new.csv",'a',encoding = 'utf-8', errors='ignore')
#             fhw.write(j+'\n')
#             fhw.close()

# with open(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\pos_hinglish.csv") as stop_word_hinglish:
#     reader_obj = csv.reader(stop_word_hinglish)

#     for i in reader_obj:
#         test=i[0].split()
#         for j in test:
#             # print(j)
#             fhw=open(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\pos_hinglish_new.csv",'a')
#             fhw.write(j+'\n')
#             fhw.close()

# with open(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\pos_hin.csv",encoding = 'utf-8', errors='ignore') as stop_word_hinglish:
#     reader_obj = csv.reader(stop_word_hinglish)

#     for i in reader_obj:
#         test=i[0].split()
#         for j in test:
#             # print(j)
#             fhw=open(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\pos_hin_new.csv",'a',encoding = 'utf-8', errors='ignore')
#             fhw.write(j+'\n')
#             fhw.close()

stop_word_hinglish_new=pd.read_csv(r'C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\stop_word_hinglish_new.csv')
neg_hinglish_new=pd.read_csv(r'C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\neg_hinglish_new.csv')
pos_hinglish_new=pd.read_csv(r'C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\pos_hinglish_new.csv')
# neg_slang_hinglish=pd.read_csv(r'C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\neg_slang_hinglish.csv')

stop_word_hinglish_new=stop_word_hinglish_new.iloc[:,0].tolist()
neg_hinglish_new=neg_hinglish_new.iloc[:,0].tolist()
pos_hinglish_new=pos_hinglish_new.iloc[:,0].tolist()


stop_word_hin_new=pd.read_csv(r'C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\stop_word_hin_new.csv')
# neg_hin_new=pd.read_csv(r'C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\neg_hin_new.csv')
pos_hin_new=pd.read_csv(r'C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\pos_hin_new.csv')
# neg_slang_hinglish=pd.read_csv(r'C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\converted\neg_slang_hinglish.csv')

stop_word_hin_new=stop_word_hin_new.iloc[:,0].tolist()
# neg_hin_new=neg_hin_new.iloc[:,0].tolist()
pos_hin_new=pos_hin_new.iloc[:,0].tolist()

print(pos_hinglish_new[12])
print(pos_hin_new[12])

text=input().split()
temp=[]
for i in range(len(text)):
    if text[i] in stop_word_hinglish_new:
        idx=stop_word_hinglish_new.index(text[i])
        temp.append(stop_word_hin_new[idx])
    elif text[i] in pos_hinglish_new:
        idx=pos_hinglish_new.index(text[i])
        temp.append(pos_hin_new[idx])
print(temp)
temp_new=[]
text_temp=""

for i in temp:
   
  # concatenating the strings
  # using + operator
  text_temp = text_temp+ ' '+ i

print(text_temp)

text_temp=translator.translate(text_temp).text
print(text_temp)