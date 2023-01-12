import pandas as pd
data=pd.read_csv(r"training_data_translated.csv")
# print(data)
# for i in range(1,6):
#     data2=pd.read_csv(rf"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\train_dataset\{i}.csv")
#     data=pd.concat([data,data2])
# data.to_csv("training_data_translated.csv", index=False)
# data=data.iloc[:,0].tolist()
# total_translated=[]
# for i in data:
#     try:
#         normalized_string2=i.split()
#         string=""
    
#         for i in normalized_string2:
#             string=i+" "+string
#         total_translated.append(string)
#     except:
#         total_translated.append("")
# total_translated=pd.DataFrame(total_translated)
# total_translated.to_csv("training_data.csv", index=False)
# texts=pd.read_csv(r"C:\Users\harsh\OneDrive - UPES\Desktop\d_drive\NNST-Sentiment-Analyser\texts.csv")
# labels=texts["class"].tolist()
# data["labels"]=labels
# data.to_csv("training_data_translated.csv", index=False)
print(data)
# import enchant

# print(enchant.__version__)