# 🤖 Livales Discord Bot

Bot Discord sederhana untuk menyapa pengguna dengan slash command `/halo`.

---

## ✨ Fitur

- `/halo` → Bot akan membalas sapaan dengan nama pengguna.
- `/take-note` - Simpan catatan pribadi
- `/my-notes` - Lihat catatan tersimpan
- `/ask` - Tanyakan apa saja tentang Livales
- `/about-livales` - Info lengkap tentang perusahaan
- `/clear-notes` - Hapus semua catatan
- `/vale` - Sapa seseorang

---

## ⚙️ Instalasi

### 1. Clone repository (atau download source code)

```bash
git clone https://github.com/livales/bot-discord-livales.git
cd bot-discord-livales
```

## ⚙️ 2. Siapkan environment

Pastikan sudah menginstall **Python 3.9+** (disarankan Python standar, bukan Anaconda).

Buat virtual environment:

```bash
python -m venv venv
```

### Aktifkan virtual environment:

- Windows:

```bash
venv\Scripts\activate
```

- MacOS/Linux:

```bash
source venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 4. Konfigurasi token bot

Buat file `.env` atau salin dari `.env.example` di root project (sejajar dengan `main.py`):

> Salin file contoh `.env.example` menjadi `.env`:
>
> ```bash
> cp .env.example .env
> ```
>
> Di Windows (cmd/powershell), bisa juga:
>
> ```powershell
> copy .env.example .env
> ```

Edit file `.env` dan ganti:

```bash
DISCORD_TOKEN=your_bot_token
OPENAI_API_KEY=your_openai_api_key_here
```

Ganti `your_bot_token` dengan token bot dari Discord Developer Portal.

# 🚀 Menjalankan bot

```bash
python main.py
```

> Jika berhasil, terminal akan menampilkan:
>
> ```php-template
> Bot sudah online sebagai <nama_bot>!
> Bot siap menerima perintah.
> ```

# 🧪 Testing

1. Pastikan bot sudah diundang ke server Discord kamu.

2. Di text channel, ketik /halo

3. Bot akan membalas:

```php-template
Halo juga, <username>! 👋
```

## 📂 Struktur Project

Project ini terdiri dari dua file utama untuk bot:

- **`main.py`**  
  Berisi _full syntax_ lengkap untuk menjalankan bot Discord.  
  Cocok untuk kamu yang ingin melihat struktur utuh program dari awal hingga akhir.

- **`bot.py`**  
  Berisi logika bot yang terpisah di folder `bot/` (misalnya: command, event handler, dsb).  
  File ini di-_import_ oleh `main.py` agar struktur kode lebih modular dan mudah dirawat.
