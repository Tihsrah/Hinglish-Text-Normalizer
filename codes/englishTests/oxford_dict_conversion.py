import pandas as pd
from googletrans import Translator
from tqdm import tqdm
from indictrans import Transliterator
import csv
alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
         "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
dictionary_all = []
for j in range(len(alpha)):
    print(alpha[j])
    # dictionary=pd.read_csv(rf"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\Dictionary_hindi_new\{alpha[j]}word_hin_new.csv", engine="python", sep=',', quotechar='"', error_bad_lines=False,encoding="utf8")

    # # # 'cp1252'
    # dictionary=dictionary.iloc[:,0].tolist()
    # translator = Translator()
    # dictionary_translated=[]

    # # # duplicates stopwords
    # duplicate_dictionary=[]
    # print(len(dictionary))
    # for i in range(len(dictionary)):
    #     if dictionary[i] not in duplicate_dictionary:
    #         duplicate_dictionary.append(dictionary[i])
    # dictionary=duplicate_dictionary
    # print(len(dictionary))
    # dictionary=pd.DataFrame(dictionary)
    # dictionary.to_csv(rf"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\Dictionary_hindi_new\{alpha[j]}word_hin_new.csv", index=False)

    # translation
    # for i in tqdm(dictionary):
    #     translated_text = translator.translate(i ,src='en',dest='hi')
    #     dictionary_translated.append(translated_text.text)
    #     try:
    #         translated_text = translator.translate(i ,src='en',dest='hi')
    #         dictionary_translated.append(translated_text.text)
    #     except Exception as e:
    #         # translator.raise_Exception = True
    #         print(e)
    # dictionary_translated=pd.DataFrame(dictionary_translated)
    # dictionary_translated.to_csv(rf'C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\Dictionary_hindi\{alpha[i]}word_hin.csv', index=False)

    # transliteration to hinglish
    # inv_trn = Transliterator(source='hin', target='eng')
    # transliterated_dictionary=[]

    # for i in tqdm(dictionary):
    #     res=inv_trn.transform(i)
    #     transliterated_dictionary.append(res)

    # transliterated_dictionary=pd.DataFrame(transliterated_dictionary)
    # transliterated_dictionary.to_csv(rf"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\Dictionary_hinglish_new\{alpha[j]}word_hinglish_new.csv", index=False)

    # converting multispaced hinglish data to one word data
    # with open(rf"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\Dictionary_hinglish\{alpha[j]}word_hinglish.csv") as dictionary_hinglish:
    #     reader_obj = csv.reader(dictionary_hinglish)

    #     for i in tqdm(reader_obj):
    #         test=i[0].split()
    #         for k in test:
    #             # print(j)
    #             fhw=open(rf"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\Dictionary_hinglish_new\{alpha[j]}word_hinglish_new.csv",'a')
    #             fhw.write(k+'\n')
    #             fhw.close()

    # converting multispaced hindi data to one word data
    # with open(rf"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\Dictionary_hindi\{alpha[j]}word_hin.csv",encoding='utf-8') as dictionary_hinglish:
    #     reader_obj = csv.reader(dictionary_hinglish)

    #     for i in tqdm(reader_obj):
    #         test=i[0].split()
    #         for k in test:
    #             # print(j)
    #             fhw=open(rf"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\Dictionary_hindi_new\{alpha[j]}word_hin_new.csv",'a',encoding='utf-8')
    #             fhw.write(k+'\n')
    #             fhw.close()

    # dictionary_hinglish_new=pd.read_csv(rf"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\Dictionary_hinglish\{alpha[j]}word_hinglish.csv")
    # dictionary_hindi_new=pd.read_csv(rf"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\Dictionary_hindi\{alpha[j]}word_hin.csv",encoding='utf-8')

    # print(len(dictionary_hinglish_new))
    # print(len(dictionary_hindi_new))

    # dictionary_hinglish_new=dictionary_hinglish_new.iloc[:,0].tolist()
    # dictionary_hindi_new=dictionary_hindi_new.iloc[:,0].tolist()
    # print("old",len(dictionary_hinglish_new))
    # # removing duplicates from new formed dataset
    # no_duplicate_dictionary_hinglish=[]
    # no_duplicate_dictionary_hindi=[]

    # for i in range(len(dictionary_hinglish_new)):
    #     if dictionary_hinglish_new[i] not in no_duplicate_dictionary_hinglish:
    #         no_duplicate_dictionary_hinglish.append(dictionary_hinglish_new[i])
    #         no_duplicate_dictionary_hindi.append(dictionary_hindi_new[i])

    # dictionary_hinglish_new=no_duplicate_dictionary_hinglish
    # dictionary_hindi_new=no_duplicate_dictionary_hindi

    # dictionary_hinglish_new=pd.DataFrame(dictionary_hinglish_new)
    # dictionary_hindi_new=pd.DataFrame(dictionary_hindi_new)

    # dictionary_hinglish_new.to_csv(rf'C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\Dictionary_hinglish_new\{alpha[j]}word_hinglish_new.csv', index=False)
    # dictionary_hindi_new.to_csv(rf'C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\datasets\Dictionary_hindi_new\{alpha[j]}word_hindi_new.csv', index=False)

    # print("new",len(dictionary_hinglish_new))
