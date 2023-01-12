from minor_methods import *
import pickle
import pandas as pd
english_vocab_2 = pd.read_csv(r'all_english_no_dupli_final.csv',
                              engine="python", sep=',', quotechar='"', error_bad_lines=False)
hinglish_vocab_2 = pd.read_csv(r'all_hinglish_no_dupli_final.csv',
                               engine="python", sep=',', quotechar='"', error_bad_lines=False)
english_vocab_2 = english_vocab_2.iloc[:, 0].tolist()
hinglish_vocab_2 = hinglish_vocab_2.iloc[:, 0].tolist()

# print(english_vocab_2[0])


english_vocab_2 = create_dictionary(english_vocab_2)
hinglish_vocab_2 = create_dictionary(hinglish_vocab_2)


# create a binary pickle file
f = open("english_vocab_2.pkl", "wb")

# write the python object (dict) to pickle file
pickle.dump(english_vocab_2, f)

# close file
f.close()


f = open("hinglish_vocab_2.pkl", "wb")

# write the python object (dict) to pickle file
pickle.dump(hinglish_vocab_2, f)

# close file
f.close()
