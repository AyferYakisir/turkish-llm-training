import torch
from master_model import MasterModel
from tokenizer import Tokenizer

u_tokenizer = Tokenizer("tokenizer.json")

prompt = "Gökyüzünde bulutlar usulca süzülüyor, hava taze ve ferah."
tokens = u_tokenizer.encode(prompt)

# Liste -> Tensor (batch dimension ile)
input_tensor = torch.tensor([tokens], dtype=torch.long)

torch.manual_seed(1)
model = MasterModel(vocab_size=len(u_tokenizer.vocab), embedding_dim=4, context_length=50)

output = model(input_tensor)
print(model)  # (batch, seq_len, embed_dim)
