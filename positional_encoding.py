import math
from positional_embedding import meanings
import torch

def get_position_encoding(context_length, embedding_dim, base=10000, device="cpu"):
  p_embeddings = torch.zeros(context_length, embedding_dim, device=device)
  for pos in range(context_length):
    for i in range(embedding_dim // 2):
      p_embeddings[pos, 2 * i] = math.sin(pos / (base ** (2 * i / embedding_dim)))
      if i + 1 < embedding_dim:
        p_embeddings[pos, 2 * i + 1] = math.cos(pos / (base ** (2 * i + 1 / embedding_dim)))
  
  return p_embeddings.unsqueeze(0)
pos_embeddings = get_position_encoding(15, 4)
print(pos_embeddings.shape)

meanings_in_sentence = meanings + pos_embeddings
print(meanings_in_sentence)