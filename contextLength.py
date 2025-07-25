from tokenizer import Tokenizer
prompt = "Gökyüzünde bulutlar usulca süzülüyor, "

next_token = " "

output = " hava taze ve ferah."
data = "Gökyüzünde bulutlar <pad> <pad> "
hedef = "hava taze <pad> <pad> "
 
context_length = 50


tokenizer = Tokenizer("tokenizer.json")

ids = tokenizer.encode(prompt)

print(len(ids), ids)