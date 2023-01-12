

import pandas as pd
from googletrans import Translator
from tqdm import tqdm
from indictrans import Transliterator
import csv
# alpha = [
#     "अ",	"आ", "इ", "ई",	"उ",	"ऊ",	"ए",	"ऐ",	"ओ",	"औ",	"अं",
#     "क",	"ख",	"ग",	"घ",	"च",	"छ",	"ज",	"झ",	"ञ",	"ट",	"ठ",	"ड",	"ढ",
#     "त",	"थ",	"द",	"ध",	"न",	"प",	"फ",	"ब",	"भ",	"म",	"य",	"र",	"ल",
#     "व",	"श",	"ष",	"स",	"ह",	"क्ष",	"त्र", "ज्ञ"
# ]
alpha = ["A"]

# alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
#  "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# alpha = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
#          "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
dictionary_all = []
for j in tqdm(range(len(alpha))):
    print(alpha[j])
    # dictionary = pd.read_csv(
    #     rf"C:\Users\harsh\OneDrive - UPES\Desktop\hinglish to english\Hindi Dictionary\{alpha[j]}.csv", engine="python", sep=',', quotechar='"', error_bad_lines=False, encoding="utf8")
    # # print(dictionary)
    # dictionary = dictionary.iloc[:, 0].tolist()

    # transliteration
    # inv_trn = Transliterator(source='hin', target='eng')
    # translated_dictionary = []

    # for i in tqdm(dictionary):
    #     try:
    #         res = inv_trn.transform(i)
    #         translated_dictionary.append(res)
    #     except:
    #         print("exception happend")
    # translated_dictionary = pd.DataFrame(translated_dictionary)
    # translated_dictionary.to_csv(
    #     rf"C:\Users\harsh\OneDrive - UPES\Desktop\hinglish to english\Hinglish Dictionary\{alpha[j]}.csv", index=False)

    # converting multispaced hinglish data to one word data
    # with open(rf"C:\Users\harsh\OneDrive - UPES\Desktop\hinglish to english\Hinglish Dictionary\{alpha[j]}.csv", encoding="utf8") as dictionary_hinglish:
    #     reader_obj = csv.reader(dictionary_hinglish)

    #     for i in tqdm(reader_obj):
    #         test = i[0].split()
    #         for k in test:
    #             # print(j)
    #             fhw = open(
    #                 rf"C:\Users\harsh\OneDrive - UPES\Desktop\hinglish to english\Hinglish Dictionary\hindlish one word\{alpha[j]}_one_word.csv", 'a', encoding='utf8')
    #             fhw.write(k+'\n')
    #             fhw.close()
    dictionary_hinglish_new = pd.read_csv(
        rf"C:\Users\harsh\OneDrive - UPES\Desktop\hinglish to english\English Dictionary\all_english_no_dupli.csv", engine="python", sep=',', quotechar='"', error_bad_lines=False, encoding="utf8")
    dictionary_hinglish_new = dictionary_hinglish_new.iloc[:, 0].tolist()
    no_duplicate_dictionary_hinglish = []
    for i in tqdm(range(len(dictionary_hinglish_new))):
        if dictionary_hinglish_new[i] not in no_duplicate_dictionary_hinglish:
            no_duplicate_dictionary_hinglish.append(dictionary_hinglish_new[i])
    dictionary_hinglish_new = no_duplicate_dictionary_hinglish

    # dictionary_all.extend(dictionary_hinglish_new)

    dictionary_hinglish_new = pd.DataFrame(dictionary_hinglish_new)
    dictionary_hinglish_new.to_csv(
        rf'C:\Users\harsh\OneDrive - UPES\Desktop\hinglish to english\English Dictionary\all_english_no_dupli_final.csv', index=False)
