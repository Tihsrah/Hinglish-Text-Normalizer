vowels=['a','e','i','o','u']
mistakes={}
similar_vowels={
    'a':'e',
    'e':'i',
    'i':'e',
    'o':'u',
    'u':'o',
}
similar={
    "quran":["kuran"],
    "q":["k"],

}

def generate_erronious_vowel_text(string):
    string_lit=[]
    string_lit.append(string)
    num_vol=0
    for i in string:
        if i in vowels:
            num_vol=num_vol+1
    
    for i in range(len(string)):
        for k in range(len(vowels)):
            # print("ith = ",i,k,vowels[k])
            try:
                vol_idx=string.index(vowels[k])
                # print("vol idx",vol_idx,vowels[k])
                
            except ValueError:
                # print("substring not found")
                pass
            else:
                # print("printing all iters")
                for j in range(len(vowels)):
                    if(vol_idx>(len(string)/2)):
                        temp = string[:vol_idx] + vowels[j] + string[vol_idx + 1:]
                        # print("text = ",vowels[j]," = ",temp)
                        string_lit.append(temp)
                # print("printing similar vowels")
                for j in similar_vowels:
                    if(vowels[k]==j and vol_idx<(len(string)/2)):
                        temp = string[:vol_idx] + similar_vowels[j] + string[vol_idx + 1:]
                        # print("text = ",similar_vowels[j]," = ",temp)
                        string_lit.append(temp)
    return string_lit
generate_erronious_vowel_text("khelo")

def create_dictionary(data):
    dictionary={}
    for i in data:
        returned_list=generate_erronious_vowel_text(i)
        dictionary[returned_list[0]]=list(set(returned_list[:]))
    return dictionary

