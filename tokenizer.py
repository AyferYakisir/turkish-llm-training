import json
class Tokenizer:
    def __init__(self,vocab_file):
        with open(vocab_file,"r") as f:
            self.vocab =json.load(f)
            self.reverse_vocab={v: k for k, v in self.vocab.items()}

    def encode(self, text):
        tokens = []

        for word in text.split():
            i=0
            while i<len(word):
                found_mach =False
                for j in range(len(word), i, -1):
                    sub_word = word[i:j]
                    if sub_word in self.vocab:
                        tokens.append(self.vocab[sub_word])
                        i=j
                        found_mach = True
                        break
                if not found_mach:
                    tokens.append(self.vocab["<unk>"])
                    i+=1
            tokens.append(self.vocab[" "])
        
        tokens.pop()
        return tokens
    

    def tokenize(self,text):
        token_ids= self.encode(text)
        return [self.reverse_vocab[id] for id in token_ids]

    def decode(self, ids):
        text = ""
        for id in ids:
            text += self.reverse_vocab[id]
        return text
 
tokenizer = Tokenizer("tokenizer.json")

text = "Dağlar uzaklarda heybet"
ids = tokenizer.encode(text)
print(ids)  

decoded = tokenizer.decode(ids)
print(decoded) 

with open("text.txt","r") as f:
    text = f.read()
text

tokens=tokenizer.encode(text)
print(tokens)