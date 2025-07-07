"""
Temporary storage untuk catatan pengguna
Untuk production, ganti dengan database yang proper (SQLite, PostgreSQL, dll)
"""

# Dictionary untuk menyimpan catatan pengguna
user_notes = {}

# Fungsi-fungsi untuk manajemen storage bisa ditambahkan di sini
def save_note(user_id: str, note: dict):
    """Simpan catatan untuk user tertentu"""
    if user_id not in user_notes:
        user_notes[user_id] = []
    user_notes[user_id].append(note)

def get_notes(user_id: str):
    """Ambil semua catatan user"""
    return user_notes.get(user_id, [])

def clear_notes(user_id: str):
    """Hapus semua catatan user"""
    if user_id in user_notes:
        user_notes[user_id] = []

def get_note_count(user_id: str):
    """Hitung jumlah catatan user"""
    return len(user_notes.get(user_id, []))