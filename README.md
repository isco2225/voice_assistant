# 🗣️ Python Tabanlı Akıllı Sesli Asistan

Bu proje, Python diliyle geliştirilen, bilgisayarla sesli etkileşim kurmayı sağlayan bir **akıllı sesli asistan** uygulamasıdır. Özellikle görme veya hareket kısıtlılığı olan bireyler için bilgisayar kullanımını kolaylaştırmayı amaçlar.

---

## 🎯 Temel Özellikler

- 🎤 Sürekli mikrofon dinleme (konuşma başladığında otomatik algılama)
- 🔊 Doğal sesli geri bildirim (TTS)
- 🌐 Hava durumu bilgisi alma (Open-Meteo API)
- 🗓️ “Tarihte Bugün Ne Oldu?” özelliği
- 📚 Wikipedia’dan sesli bilgi araştırma (TR)
- 💬 FLAN-T5 destekli AI sohbet modülü
- 🌍 Çoklu dil desteği (isteğe bağlı çeviri)
- ⚙️ Modüler mimari: `core/`, `features/`, `utils/`, `interface/`
- ⏳ Zaman tabanlı karşılama mesajı ve döviz/hava durumu önerileri

---

## 🧠 Kullanılan Teknolojiler

| Teknoloji | Açıklama |
|----------|----------|
| `speech_recognition` | Sesli komut algılama |
| `gTTS` veya `pyttsx3` | Metni sese çevirme |
| `threading` | Eşzamanlı işlemler |
| `requests` | API çağrıları |
| `transformers` (HuggingFace) | AI sohbet motoru |
| `pyaudio` veya `sounddevice` | Mikrofon erişimi |
| `Google Translate API` | (isteğe bağlı) çeviri desteği |

---


🖼️ Proje Sunumundan Kareler

<img src="images/WhatsApp Görsel 2025-06-18 saat 10.37.53_db034588.jpg" width="500"/>
<img src="images/WhatsApp Görsel 2025-06-18 saat 10.37.52_edf7aa8e.jpg" width="400"/>
<img src="images/WhatsApp Görsel 2025-06-18 saat 10.37.53_d6924f78.jpg" width="500"/>
