import os
import sys
import csv
import passengers

def clear_screen():
    """
    Untuk membersihkan layar pengguna
    """
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')

def akses_db():
    """
    Untuk mengakses database, memunculkannya dalam bentuk dictionary
    """
    with open(PATH, 'r') as file:
        print(PATH)
        reader = csv.reader(file, delimiter=";")
        database = {}
        for row in reader:
            name, NIK, airlane, flight_code, ori_airport, dest_airport, ori_region, dest_region, dep_time, ar_time, date = row
            database.update({NIK: [name, int(NIK), str(airlane), str(flight_code), str(ori_airport), str(dest_airport), str(ori_region), str(dest_region), str(dep_time), str(ar_time), str(date)]})
    return database

def main():
    """
    Program utama dari semua program yang ada
    """
    global database
    while True:
        choice = passengers.validasi_int(main_menu)
        if choice == 1:
            passengers.nomor_1(database)
        elif choice == 2:
            passengers.nomor_2(database)
        elif choice == 3:
            passengers.nomor_3(database)
        elif choice == 4:
            passengers.nomor_4(database)
        elif choice == 5:
            clear_screen()
            print(f"\n\n{'='*70}\n{'='*8} Terima kasih sudah menggunakan aplikasi e-MotorMabur {'='*8}\n{'='*23} by: Kristian Brilyawan {'='*23}\n{'='*70}")
            break
        
        else:
            print('\nAngka yang Anda masukkan diluar jangkauan.\n')
            continue

        """
        Memastikan data yang berubah akan diperbarui ke database
        """
        with open(PATH, 'w') as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerows(database.values())

if __name__ == "__main__":
    """
    Tampilan utama menu aplikasi
    """
    main_menu = '''
==========================================
      Selamat datang di e-MotorMabur
Aplikasi pencatatan data penumpang pesawat
==========================================

          Ada yang bisa dibantu?
Silahkan pilih nomor sesuai keperluan Anda!

1. Daftar Penumpang
2. Registrasi Data Penumpang
3. Ubah Data Penumpang
4. Hapus Data Penumpang
5. Keluar

==========================================

Masukkan pilihan Anda: '''
clear_screen()

"""
Memastikan aplikasi mengakses file database yang dibutuhkan
"""
if getattr(sys, 'frozen', False):
    PATH = sys._MEIPASS
    PATH = os.path.join(PATH, 'data/data_penumpang.csv') 
else:
    PATH = os.getcwd()
    PATH = os.path.join(PATH, 'data/data_penumpang.csv') 

database = akses_db()

main()