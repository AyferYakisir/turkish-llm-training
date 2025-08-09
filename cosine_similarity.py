import torch
from master_model import MasterModel
from tokenizer import Tokenizer

u_tokenizer = Tokenizer("tokenizer.json")

prompt = "Gökyüzünde bulutlar usulca süzülüyor, hava taze ve ferah."

tokens = u_tokenizer.encode(prompt)

torch.manual_seed(1)
u_model = MasterModel(vocab_size=len(u_tokenizer.vocab), embedding_dim=4, context_length=50)

sentence_meanings = u_model(tokens)
sentence_meanings.shape




gokyuzunde_pos = [-0.5065,  0.0998, -0.6540,  0.7317]
bulutlar_pos = [ 0.7295, -0.3170,  1.5783,  1.3409]

dot_product = (
    gokyuzunde_pos[0] * bulutlar_pos[0] +
    gokyuzunde_pos[1] * bulutlar_pos[1] +
    gokyuzunde_pos[2] * bulutlar_pos[2] +
    gokyuzunde_pos[3] * bulutlar_pos[3]
)
print(dot_product) 

cos_sim_uzakligi = gokyuzunde_pos[0] * bulutlar_pos[0]
cos_sim_parlakligi = gokyuzunde_pos[1] * bulutlar_pos[1]
cos_sim_kizilligi = gokyuzunde_pos[2] * bulutlar_pos[2]
cos_sim_maviligi = gokyuzunde_pos[3] * bulutlar_pos[3]

total_cos_sim = cos_sim_uzakligi + cos_sim_parlakligi + cos_sim_kizilligi + cos_sim_maviligi

print(cos_sim_uzakligi, cos_sim_parlakligi, cos_sim_kizilligi, cos_sim_maviligi, total_cos_sim)

cs_0_0 = torch.dot(sentence_meanings[0][0], sentence_meanings[0][0])
cs_0_1 = torch.dot(sentence_meanings[0][0], sentence_meanings[0][1])
cs_0_2 = torch.dot(sentence_meanings[0][0], sentence_meanings[0][2])
cs_0_3 = torch.dot(sentence_meanings[0][0], sentence_meanings[0][3])

print(cs_0_0, cs_0_1, cs_0_2, cs_0_3)

the_similarities = []

for i in range(sentence_meanings.shape[0]):
  cs_the_i = sentence_meanings[0][0] * sentence_meanings[i][0] + sentence_meanings[0][1] * sentence_meanings[i][1] + sentence_meanings[0][2] * sentence_meanings[i][2] + sentence_meanings[0][3] * sentence_meanings[i][3]
  the_similarities.append(cs_the_i)

print(the_similarities)

all_similarities = torch.zeros(sentence_meanings.shape[0], sentence_meanings.shape[0])

for j in range(sentence_meanings.shape[0]):
    j_similarities = torch.zeros(sentence_meanings.shape[0])

    for i in range(sentence_meanings.shape[0]):
        for k in range(sentence_meanings.shape[1]):
            cs_j_i = torch.dot(sentence_meanings[j][k], sentence_meanings[i][k])
            j_similarities[i] += cs_j_i

    all_similarities[j] = j_similarities

print(all_similarities.detach().numpy())

print(sentence_meanings.shape, sentence_meanings.T.shape)

sentence_meanings_2d = sentence_meanings.squeeze(0)  # (15, 4)

# Tokenlar arasındaki benzerlik matrisi (15 x 15)
all_sim_torch = sentence_meanings_2d @ sentence_meanings_2d.T  # (15,4) @ (4,15) -> (15,15)

print(all_sim_torch.shape)
print(all_sim_torch)

attention_weights = torch.softmax(all_similarities, dim=1)
print(attention_weights)

attention_weights = torch.tensor([[[1.0, 0.0, 0.0]]])  # (1, 1, 3) örnek attention weights
sentence_meanings = torch.randn(1, 3, 4)  # (1, 3 token, 4 embedding_dim)

sentence_context_vector = torch.bmm(attention_weights, sentence_meanings)  # (1, 1, 4)
print(sentence_context_vector.shape)

