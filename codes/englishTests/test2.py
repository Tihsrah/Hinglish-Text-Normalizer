import pandas as pd
data=pd.read_csv(r"C:\Users\harsh\Downloads\dataset\rev\normalized_string_final100-200.csv")
data=data.iloc[:,0].tolist()
inverted=[]
print(data)




for i in data:
    i=i.split()
    string=""
    for j in i:
        string=j+" "+string
    inverted.append(string)


inverted=pd.DataFrame(inverted)
inverted.to_csv("normalized_string_final100-200.csv",index=False)

