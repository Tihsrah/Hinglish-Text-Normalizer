for i in tqdm(conversion_list):
    translated_text = translator.translate(i ,src='hi',dest='en')
    translated.append(translated_text.text)
print(translated)