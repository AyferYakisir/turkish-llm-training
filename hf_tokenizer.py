from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.trainers import BpeTrainer
from tokenizers.pre_tokenizers import Whitespace
from sozlukleTokenize import text1

hf_tokenizer = Tokenizer(BPE())
hf_tokenizer.pre_tokenizer = Whitespace()
trainer = BpeTrainer(vocab_size=49, special_tokens=["<unk>"])
print("BPE Trainer oluşturuldu. Vocab size: 49, Special token: <unk>")
hf_tokenizer.train(["text.txt"], trainer)

hf_tokenizer.get_vocab_size(), hf_tokenizer.encode(text1).ids
encoded = hf_tokenizer.encode(text1)
print("Token ID'leri:", encoded.ids)
print("Token'lar:", encoded.tokens)

hf_tokenizer.save("hf_tokenizer.json")