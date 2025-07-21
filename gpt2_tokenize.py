import tiktoken
from sozlukleTokenize import text1

enc = tiktoken.get_encoding("gpt2")
gpt2_ids = enc.encode(text1)
print(gpt2_ids)

enc.decode(gpt2_ids)