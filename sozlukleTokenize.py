text = "Türkiyenin başkenti"
text1= "marketten bir litre süt aldı"
import json

with open("tokenizer.json","r") as f:
    vocab = json.load(f)

def tokenize(text):
    parts = text.split()
    ids = []
    for part in parts:
        if part in vocab:
            value =vocab[part]
        else:
            value = vocab["<unk>"]
        ids.append(value)
    return ids

print(tokenize(text1))

