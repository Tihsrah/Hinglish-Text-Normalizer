
# import the module
import pandas as pd
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
from gingerit.gingerit import GingerIt
from googletrans import Translator
from tqdm import tqdm 

stop_word=pd.read_csv(r'datasets\converted\stop_word.csv')
neg=pd.read_csv(r'datasets\converted\neg.csv')
pos=pd.read_csv(r'datasets\converted\pos.csv')
neg_slang=pd.read_csv(r'datasets\converted\neg_slang.csv')

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
# stop_word_hin.to_csv(r'datasets\converted\stop_word_hin.csv', index=False)

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