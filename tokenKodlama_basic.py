text1="Kedi köpeği kovaladı"
text2= "Köpek Kediyi kovaladı"

text="Türkiyenin başkenti"

def tokenize(text):
    return text.split()

print(tokenize(text1))