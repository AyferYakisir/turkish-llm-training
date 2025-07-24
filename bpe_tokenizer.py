import sentencepiece as spm
from sozlukleTokenize import text1

spm.SentencePieceTrainer.Train(
    input="text.txt",
    model_prefix="spm_tokenizer",
    vocab_size=49,
    model_type="bpe",
)

spm_tokenizer = spm.SentencePieceProcessor(model_file="spm_tokenizer.model")
spm_ids = spm_tokenizer.Encode("text1")
print("Token ID'leri:", spm_ids)
spm_tokens = spm_tokenizer.Encode(text1, out_type=str)
print("Token Stringleri:", spm_tokens)
spm_ids, spm_tokens