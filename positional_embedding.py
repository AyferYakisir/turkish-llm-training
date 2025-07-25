import torch

from tokenizer import tokenizer
from contextLength import context_length

torch.manual_seed(1)
embeddings = torch.nn.Embedding(num_embeddings=context_length, embedding_dim=4)

sentence = "Gökyüzünde bulutlar usulca süzülüyor, hava taze ve ferah."

sentence1 = "Ali Ayşe'yi itti."
sentence2 = "Ayşe Ali'yi itti."

tokens = tokenizer.encode(sentence)
tokens = torch.tensor(tokens)
print(tokens.shape)

meanings = embeddings(tokens)
print(meanings)