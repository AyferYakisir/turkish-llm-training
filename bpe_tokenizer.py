import sentencepiece as spm

spm.SentencePieceTrainer.Train(
    input="text.txt",
    model_prefix="spm_tokenizer",
    vocab_size=49,
    model_type="bpe",
)