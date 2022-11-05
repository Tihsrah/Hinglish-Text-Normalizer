from indictrans import Transliterator
from googletrans import Translator
from tqdm import tqdm 
import pandas as pd
# trn = Transliterator(source='hin', target='eng', build_lookup=True)
from minor_official import df1
trn = Transliterator(source='eng', target='hin')

# hin_ = trn.transform(eng)
hin_=df1['Text'].tolist()
conversion_list=[]
c=0
for i in tqdm(hin_):
    conversion_list.append(trn.transform(i))
    if c==200:
        break
    c=c+1
print(hin_[0:100])
print(conversion_list[0:100])
translator = Translator()
c=0
translated=[]
for i in tqdm(conversion_list):
    translated_text = translator.translate(i ,src='hi',dest='en')
    translated.append(translated_text.text)
    if c==20:
        break
    c=c+1
print(translated)
final=pd.DataFrame(translated)
final.to_csv('final.csv')
