import os
import sys
import csv
import passengers

def clear_screen():
    """Untuk membersihkan layar pengguna"""
    _ = os.system('clear')

def initialize_db():
    """
    Untuk mengakses database, memunculkannya dalam bentuk dictionary"""
    with open(PATH, 'r') as file:
        # Membuat objek reader
        reader = csv.reader(file, delimiter=";")
        # Inisialisasi database kosong
        database = {}
        # Mengisi data ke dalam database
        for row in reader:
            nomor, name, NIK, airlane, flight_code, ori_airport, dest_airport, ori_region, dest_region, dep_time, ar_time, date = row
            database.update({NIK: [int(nomor), name, int(NIK), str(airlane), str(flight_code), str(ori_airport), str(dest_airport), str(ori_region), str(dest_region), str(dep_time), str(ar_time), str(date)]})

    return database

def main():
    """
    The main program to run the whole process
    """
    global database
    while True:
        # Meminta input berupa opsi fitur yang akan dijalankan
        choice = passengers.validasi_int(main_menu)
        # Jalankan fitur sesuai opsi yang di pilih 
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
            print("\n\nTerima kasih sudah menggunakan aplikasi 'e-MotorMabur'.\n\n")
            break
        
        # Jika opsi tidak ada, maka minta input ulang
        else:
            print('Angka yang Anda masukkan diluar jangkauan.\n')
            continue

        # Menjaga agar database selalu diperbarui
        with open(PATH, 'w') as file:
            # Membuat objek writer
            writer = csv.writer(file, delimiter=";")
            # Menulis data ke dalam file csv
            writer.writerows(database.values())

if __name__ == "__main__":
    # Mendefinisikan tampilan utama aplikasi
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
    
# Membersihkan tampilan user
clear_screen()

    # Setting the path of database file
if getattr(sys, 'frozen', False):
    PATH = sys._MEIPASS
    PATH = os.path.join(PATH, 'data/data_penumpang.csv') 
else:
    PATH = os.getcwd()
    PATH = os.path.join(PATH, 'data/data_penumpang.csv') 

# Initializing database
database = initialize_db()

# Menjalankan menu utama
main()