# 🚗 GaleriAsisst

**GaleriAsisst**, bir oto galeri yönetim sistemidir. Kullanıcılar, doğal dilde komut vererek araç ekleme, güncelleme ve silme işlemlerini gerçekleştirebilir. Bu proje, **Introspective Agent** kullanarak veritabanı işlemlerini otomatik hale getirir.

## ✨ Özellikler

- 🚘 **Araç ekleme** (marka, model, yıl, fiyat, renk, plaka bilgileriyle)
- 🔄 **Araç güncelleme** (fiyat değişikliği vb.)
- ❌ **Araç silme** (marka ve model bazında)
- 📊 **Tüm araçları listeleme**
- ✅ **Yanlış marka/model girişlerinde doğrulama**
- 🛠 **SQL Server ile entegrasyon**
- 🤖 **LLM tabanlı Introspective Agent entegrasyonu** (SQL sorgularının doğruluğunu kontrol eder)

## 🚀 Kurulum

### 1️⃣ Gerekli Bağımlılıkları Yükleme
```bash
pip install -r requirements.txt
```

### 2️⃣ .env Dosyasını Oluşturma
`.env` dosyanın içine aşağıdaki bilgileri ekleyerek **OpenAI API anahtarını** ayarla:
```
OPENAI_API_KEY=your-api-key-here
```

### 3️⃣ Veritabanı Ayarları
`database_connection.py` dosyasında **MS SQL Server** bilgilerini güncelle:
```python
server = "GORKEM"
database = "GaleriDB"
```

## 📜 Kullanım

### ✅ Yeni Araç Ekleme
```python
agent.invoke("Toyota Corolla 2022 model aracını 750000 TL fiyatla ekle.")
```

### 🔄 Araç Fiyat Güncelleme
```python
agent.invoke("Hyundai i20 aracının fiyatını 500000 TL yap.")
```

### ❌ Araç Silme
```python
agent.invoke("Opel Astra modelini galeriden kaldır.")
```

### 🚗 Tüm Araçları Listeleme
```python
agent.invoke("Galerideki tüm araçları listele.")
```

## 🏗 Kullanılan Teknolojiler
- **Python** 🐍
- **MS SQL Server** 🗄️
- **LangChain & LlamaIndex** 🧠
- **OpenAI API** 🤖

