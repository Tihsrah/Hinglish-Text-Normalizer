from indictrans import Transliterator
from googletrans import Translator
from tqdm import tqdm 
import pandas as pd
from langdetect import detect
import fasttext

translator = Translator()
# trn = Transliterator(source='hin', target='eng', build_lookup=True)
# from minor_official import df1
trn = Transliterator(source='eng', target='hin')
# inv_trn = Transliterator(source='hin', target='eng')
# res=inv_trn.transform("कलम")
# print(res)


# hin_ = trn.transform(eng)
# hin_=df1['Text'].tolist()


hin_="bhaiyon and cmputr sister mai pagal hu".split()

# Import libraries
from transformers import pipeline
# Load pipeline
# classifier = pipeline("text-classification", model = "papluca/xlm-roberta-base-language-detection")
import joblib
# joblib.dump(classifier,'classifer.joblib')
classifier=joblib.load(r"classifer.joblib")
classify=[]
# Example sentence
for i in hin_:
    test_classify=classifier(i)
    classify.append(test_classify[0].get("label"))
print(hin_)
print(classify)

for i in range(len(classify)):
    if classify[i]=='en':
        hin_[i]=translator.translate(hin_[i] ,src='en',dest='hi').text
    print(detect(classify[i]))
print(hin_)


conversion_list=[]
c=0
for i in tqdm(hin_):
    conversion_list.append(trn.transform(i))
print(conversion_list)

import enchant
 
# create dictionary for the language
# in use(en_US here)
dict = enchant.Dict("en_US")
 
# list of words
words = ["cmputr", "watr", "study", "wrte","karta","kahan"]
 
# find those words that may be misspelled
misspelled =[]
for word in words:
    if dict.check(word) == False:
        misspelled.append(word)
        print("Suggestion for " + word + " : " + str(dict.suggest(word)))
print("The misspelled words are : " + str(misspelled))


# suggest the correct spelling of
# the misspelled words
# import Levenshtein
# from pyphonetics import RefinedSoundex
# rs = RefinedSoundex()
# for word in misspelled:
#     lit=dict.suggest(word)
#     print(lit)
#     phoneme=[]
#     suggested=[]
#     for i in lit:
#         suggested.append(i)
#         phoneme.append(rs.distance(word,i))
#     for i in range(len(phoneme)):
#         if phoneme[i]==0:
#             phoneme.pop(i)
#             suggested.pop(i)
#     testify=[]
#     # Example sentence
#     for i in suggested:
#         test_testify=classifier(i)
#         testify.append(test_testify[0].get("label"))
#         testify.append(detect(i))
        # pretrained_lang_model = r"C:\Users\harsh\Downloads\lid.176.bin"
        # model = fasttext.load_model(pretrained_lang_model)
        # predictions = model.predict(i, k=1)
        # testify.append(predictions)

    # print(suggested)
    # print(testify)
    # for i in range(len(testify)):
    #     if testify[i]=='en':

    # print("Suggestion for " + word + " : " + str(dict.suggest(word)))

#     if c==1:
#         break
#     c=c+1
# # print(hin_[0:100])
# # print(conversion_list[0:100])

# c=0
# translated=[]
# for i in tqdm(conversion_list):
#     translated_text = translator.translate(i ,src='hi',dest='en')
#     translated.append(translated_text.text)
#     if c==20:
#         break
#     c=c+1
# print(translated)
# final=pd.DataFrame(translated)
# final.to_csv('final.csv')
