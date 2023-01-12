import pandas as pd
from indictrans import Transliterator
from tqdm import tqdm

data = pd.read_csv(r"English-Hindi Dictionary.csv")
# print(data)
# e_word = data['eword'].to_list()
# # print(e_word)
# h_word = data['hword'].to_list()
# # print(h_word)

# e_word = pd.DataFrame(e_word)
# e_word.to_csv('english.csv', index=False)

# h_word = pd.DataFrame(h_word)
# h_word.to_csv('hindi.csv', index=False)

english = pd.read_csv('english.csv')
print(len(english))

hindi = pd.read_csv('hindi.csv')
print(len(hindi))

# transliteration to hinglish
# inv_trn = Transliterator(source='hin', target='eng')
# transliterated_dictionary = []

# for i in tqdm(hindi):
#     res = inv_trn.transform(i)
#     transliterated_dictionary.append(res)

# transliterated_dictionary = pd.DataFrame(transliterated_dictionary)
# transliterated_dictionary.to_csv("hinglish.csv", index=False)
