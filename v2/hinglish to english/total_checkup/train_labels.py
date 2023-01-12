import pandas as pd

# data=pd.read_csv(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\texts.csv")
# labels=data["class"].tolist()
# # print(labels)

# translated=pd.read_csv(r'total_translated_1st_method.csv')
# translated=translated.iloc[:,0].tolist()

# df = pd.DataFrame(list(zip(translated, labels)),columns =['text', 'label'])
# print(df)
# df.to_csv('total_translated_1st_method_labels.csv', index=False)
data=pd.read_csv(r'training_data_translated.csv')
print(data)