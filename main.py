import os
import requests
import time
import random

# --- SETTINGAN UTAMA ---
# Link Blog Anda (Jembatan)
LINK_TUJUAN = "https://sysnetlab.blogspot.com/2026/01/premium-gallery-top-viral-aesthetic.html"

# Kata kunci gambar (Bot akan ambil random)
KEYWORDS = ["aesthetic girl", "korean fashion", "luxury travel", "home decor", "healthy food", "makeup tutorial"]

# --- FUNGSI CARI GAMBAR ---
def get_random_image_url():
    # Kita pakai LoremFlickr karena lebih stabil buat bot daripada Unsplash Source
    keyword = random.choice(KEYWORDS).replace(" ", ",")
    # Mengambil URL gambar random ukuran 800x1200
    return f"https://loremflickr.com/800/1200/{keyword}/all"

# --- FUNGSI UPLOAD ---
def upload_to_pinterest():
    token = os.environ.get("PINTEREST_TOKEN")
    board_id = os.environ.get("BOARD_ID")

    if not token or not board_id:
        print("❌ ERROR: Token atau Board ID belum disetting di GitHub Secrets!")
        return

    print("1. Sedang mencari gambar random...")
    image_url = get_random_image_url()
    print(f"   Dapat gambar: {image_url}")

    print("2. Sedang upload ke Pinterest...")
    api_url = "https://api.pinterest.com/v5/pins"
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    # Judul & Deskripsi Clickbait
    judul_list = [
        "Viral Aesthetic Ideas 2026", 
        "Must Try Trends!", 
        "Full Gallery Ideas", 
        "Best Inspiration For You"
    ]
    
    payload = {
        "board_id": board_id,
        "media_source": {
            "source_type": "image_url",
            "url": image_url
        },
        "title": random.choice(judul_list),
        "description": "Check full gallery and details here 👇",
        "link": LINK_TUJUAN
    }

    try:
        response = requests.post(api_url, headers=headers, json=payload)
        
        if response.status_code == 201:
            print("✅ SUKSES! Pin berhasil tayang.")
            print("   Link Blog yang ditempel: " + LINK_TUJUAN)
        else:
            print(f"❌ GAGAL UPLOAD. Kode: {response.status_code}")
            print(f"   Pesan Error: {response.text}")
            
    except Exception as e:
        print(f"❌ Error Koneksi: {e}")

# --- EKSEKUSI ---
if __name__ == "__main__":
    upload_to_pinterest()
