import bpy
import os
import re

# === PATH FILE TXT ===
file_path = r"G:\My Drive\Beta Pictoris - shooter robot\3D file\3D_print_part\part_list.txt"  # GANTI dengan path file kamu

# === CEK FILE ADA ATAU TIDAK ===
if not os.path.exists(file_path):
    print("File tidak ditemukan!")
else:
    with open(file_path, "r") as f:
        lines = f.readlines()

    # Ambil nama tanpa versi (_XP1, _XP2, dst)
    part_names = set()

    for line in lines:
        # Bersihkan tanda kutip dan spasi
        clean_name = line.strip().replace('"', '')

        # Hapus _XP dan angka di belakangnya
        base_name = re.sub(r'_XP\d+$', '', clean_name)

        part_names.add(base_name)

    # === HIDE OBJEK YANG NAMANYA SESUAI ===
    for obj in bpy.data.objects:
        if obj.name in part_names:
            obj.hide_set(True)
            print(f"Objek di-hide: {obj.name}")

print("Selesai!")