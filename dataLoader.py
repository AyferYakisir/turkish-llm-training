from tokenizer import Tokenizer  # Tokenizer sınıfını içeri aktar
import json
import torch
from torch.utils.data import DataLoader
from dataset import TextDataset
from contextLength import context_length


input = "Gökyüzünde bulutlar usulca süzülüyor,"
output = "usulca süzülüyor,hava taze"

tokenizer = Tokenizer("tokenizer.json")

with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()


token_ids = tokenizer.encode(text)


ids_text = " ".join(str(tid) for tid in token_ids)

with open("token_ids.txt", "w", encoding="utf-8") as f:
    f.write(ids_text)

stride = 7

def create_data_loader(token_ids: list, context_length: int, stride: int,
                       batch_size: int, shuffle: bool = True, device: str = "cpu"):
  dataset = TextDataset(token_ids, context_length, stride)
  dataloader = DataLoader(
      dataset,
      batch_size=batch_size,
      shuffle=shuffle,
      generator=torch.Generator(device=device)
    )
  
  return dataloader

train_data_loader = create_data_loader(token_ids, context_length, stride, 4,False)

print(len(train_data_loader))

i = 0
for batch in enumerate(train_data_loader):
  print(batch)
  i += 1
  if i > 2:
    break