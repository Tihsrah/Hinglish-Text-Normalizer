import csv
import sys

reader = csv.reader(open(r'datasets\converted\svar.csv', 'r',encoding = 'utf-8', errors='ignore'))
vowels = {}
for row in reader:
	k, v = row
	vowels[v] = k

reader = csv.reader(open(r'datasets\converted\vyanjan.csv', 'r',encoding = 'utf-8', errors='ignore'))
consonants = {}
for row in reader:
	k, v = row
	consonants[v] = k



def hing_to_dev(content):
    str1 = ""
    for x in content:
        for y in x.split():
            for i in range(len(y)):
                if (i+1<len(y) and y[i+1].strip()==' ़'.strip()):
                    c = y[i]+y[i+1]
                    p=2
                else:
                    c = y[i]
                    p=1
                if (c in vowels.keys()):
                    str1 = str1 + vowels[c]
                elif (c in consonants.keys()):
                    if(i+p<len(y) and y[i+p] in consonants.keys()):
                        if ((c=='झ' and i!=0) or (i!=0 and i+p+1<len(y) and y[i+p+1] in vowels.keys())): # add 'a' after 'jh', only if झ appears in the starting of the word
                            str1 = str1 + consonants[c]
                        else:
                            str1 = str1 + consonants[c]+'a'
                    else:
                        str1 = str1 + consonants[c]
                elif y[i] in ['\n','\t',' ','!',',','।','-',':','\\','_','?'] or c.isalnum():
                    str1 = str1 + c.replace('।','.')
            str1 = str1 + " "
        str1 = str1 + "\n"
    return str1
