"""
    Kelas: 2023E
    Prodi: D4 Manajemen Informatika
    Kelompok: 1

    Nama Anggota:
    1. Gerry Moeis M.D.P - 23091397164
    2. M. Faiz Noer Rizky - 23091397147
    3. Dea Ayu Novita Putri - 23091397173
"""

# Membuat fungsi turn_right
def turn_right():
    # Looping fungsi turn_left() sebanyak 3 kali
    for i in range(3):
        turn_left()

# Membuat fungsi jump()
def jump():
    # Memanggil fungsi turn_right() dan move()
    turn_right()
    move()
    
