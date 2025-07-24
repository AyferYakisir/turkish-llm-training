from tokenizer import Tokenizer  # Tokenizer sınıfını içeri aktar
import json

# Girdi metinleri
input = "Gökyüzünde bulutlar usulca süzülüyor,"
output = "usulca süzülüyor,hava taze"

# Tokenizer nesnesini yükle
tokenizer = Tokenizer("tokenizer.json")

# text.txt içeriğini oku
with open("text.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Token ID'lerini al
token_ids = tokenizer.encode(text)

# ID'leri string olarak birleştir
ids_text = " ".join(str(tid) for tid in token_ids)

# Sonucu dosyaya yaz
with open("token_ids.txt", "w", encoding="utf-8") as f:
    f.write(ids_text)

# Konsola çıktı ver
print("✅ Token ID'leri:", token_ids)
