# turkish-LLM-from-scratch 🧠🇹🇷

Bu proje, **sıfırdan Türkçe bir LLM (Large Language Model)** geliştirme sürecini adım adım belgelemektedir. Amaç; tokenizer'dan embedding'e, model mimarisinden eğitime kadar tüm süreci elle inşa ederek dil modeli mimarisini derinlemesine anlamaktır.

📌 **Durum:** Geliştirme aşamasında (aktif olarak güncelleniyor)

---

## 🔍 Amaç

- Türkçe metinlerle çalışan, kendi kelime dağarcığına sahip bir LLM oluşturmak
- Tokenizasyon, kelime-ID eşlemeleri, detokenizasyon gibi temel adımları öğrenmek
- Eğitim verileriyle çalışarak sıfırdan embedding ve model katmanları inşa etmek
- Eğitilebilir basit bir dil modeli mimarisi (örneğin: mini-Transformer) kurmak

---

## 📁 Şu Ana Kadar Yapılanlar

| Dosya                  | Açıklama                                                                 |
|------------------------|--------------------------------------------------------------------------|
| `tokenKodlama_basic.py`   | Boşluklara göre basit tokenizasyon                                      |
| `sozlukleTokenize.py`     | Ön tanımlı bir sözlük ile kelimeleri ID’lere çeviren tokenizer          |
| `idTokenize.py`           | Token ID’lerini tekrar metne çeviren (detokenization) fonksiyonu        |
| `gpt2_tokenize.py`        | GPT-2 modelinin tokenizer’ı (tiktoken) ile örnek tokenizasyon ve çözümleme |




---

## 📌 Not

Bu proje şu anda aktif geliştirilmektedir ve deneysel niteliktedir. Kodlar sade ve anlaşılır tutulmaya çalışılmaktadır.

> - İlerledikçe tüm gelişmeler bu repoya commit'lenerek eklenecektir.

---
