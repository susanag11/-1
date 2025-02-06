meme_dict = {
            "FR" : "algo de verdad o verdadero ",
            "SO?" : "porque o enserio",
            "SUNSET" : "bobo o boba"
            }

word = input(" escribe una palabra que no entiendas ( con mayùsculas" )
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("esta palabra no esta en el diccionario")
