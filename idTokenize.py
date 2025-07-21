from sozlukleTokenize import tokenize

text = "Türkiyenin başkenti"
text1= "marketten bir litre süt aldı"

tokenize_ids1=tokenize(text1)

idVocab ={
    0:"marketten",
    1:"bir",
    2:"litre",
    3:"süt",
    4:"aldı",
    5:"Türkiyenin",
    6:"başkenti",
    7:"<unk>"
}

def detokenize(ids):
    text=""
    for id in ids:
        part=idVocab[id]
        text+=part+" "
    text = text.strip()
    return text

print(detokenize(tokenize_ids1))
    
