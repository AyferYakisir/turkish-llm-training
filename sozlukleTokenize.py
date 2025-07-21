text = "Türkiyenin başkenti"
text1= "marketten bir litre süt aldı"
vocab ={
    "marketten" :0,
    "bir":1,
    "litre":2,
    "süt":3,
    "aldı":4,
    "Türkiyenin":5,
    "başkenti":6,
    "<unk>":7
    }

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

