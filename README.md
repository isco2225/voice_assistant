# Voice Assistant

Türkçe sesli asistan uygulaması. Sesli komutları algılayıp işleyebilen ve yanıt verebilen bir Python uygulaması.

## Özellikler

- Sesli komut algılama
- Metin-konuşma dönüşümü
- Not alma özelliği
- Hata yönetimi ve loglama
- Türkçe dil desteği

## Kurulum

1. Gerekli Python paketlerini yükleyin:
```bash
pip install -r requirements.txt
```

2. Windows için PyAudio kurulumu:
```bash
pip install pipwin
pipwin install pyaudio
```

## Kullanım

Uygulamayı başlatmak için:
```bash
python main.py
```

### Komutlar

- "not al" - Yeni bir not almak için
- "çık" veya "kapat" - Uygulamadan çıkmak için

## Geliştirme

Proje yapısı:
```
voice_assistant/
├── core/           # Temel ses işleme modülleri
├── features/       # Özellik modülleri
├── utils/          # Yardımcı fonksiyonlar
├── config/         # Yapılandırma dosyaları
└── logs/           # Log dosyaları
```

## Lisans

MIT