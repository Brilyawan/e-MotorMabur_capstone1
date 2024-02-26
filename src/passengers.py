from tabulate import tabulate
import __main__

def validasi_int(prompt):
    """Fungsi untuk melakukan validasi input integer / angka."""
    while True:
        try:
            num = int(input(prompt))
            if num < 0:
                print('Anda memasukkan angka negatif, silahkan masukkan angka yang sesuai.')
            else:
                return num
        except ValueError:
            print('Anda memasukkan selain angka, silahkan masukkan angka yang sesuai.')

def validasi_str(prompt):
    """Fungsi untuk melakukan validasi input string / huruf."""
    while True:
        word = input(prompt)
        if word.replace(' ','').isalpha():
            return word.title()
        else:
            print('Anda hanya bisa memasukkan karakter alfabet.')

def convert_to_table(data, columns, title):
    """Fungsi untuk mengkonversi data yang ada menjadi tabel."""
    print(title)
    print(tabulate(data, headers=columns, tablefmt="grid"))

def nomor_1(pilihan):
    """Fungsi menu di pilihan nomor 1"""
    while True:
        print('''
        ======== Daftar Data Penumpang ========
        1. Data Semua Penumpang
        2. Data Penumpang Tertentu
        3. Kembali ke Menu Utama
        =======================================
        ''')
        pilihan = validasi_int('Silahkan tentukan pilihan Anda [1-3]: ')
        if pilihan == 1:
            data_semua(__main__.database)
        elif pilihan == 2:
            data_tertentu(__main__.database)
        elif pilihan == 3:
            return
        else:
            print(f'*****Pilihan {pilihan} tidak terdapat di daftar!*****')
            
                
def data_semua(table):
    """Fungsi untuk menampilkan semua daftar penumpang."""
    # Mengkonversi dictionary menjadi list of dictionary
    data_list = [v for v in table.values()]
    # Menampilkan database penumpang dalam format tabulasi
    if not data_list:
        print(f'Database kosong, silahkan tambahkan data.')
    else:
        convert_to_table(
            data=data_list, 
            columns=['Nomor', 'Nama Penumpang', 'Nomor Induk\nKependudukan', 'Maskapai\nPenerbangan', 'Kode\nPenerbangan', 'Bandara\nKeberangkatan', 'Bandara Tujuan', 'Kota\nKeberangkatan', 'Kota Tujuan', 'Waktu\nKeberangakatan', 'Waktu Tiba', 'Tanggal'],
            title=f'\nBerikut Daftar Semua Penumpang:\n'
            )
    
def data_tertentu(table):
    """Fungsi untuk menampilkan daftar penumpang tertentu."""
    while True:
    # Meminta input NIK untuk melakukan filter
        NIK = input("\nMasukkan Nomor Induk Kependudukan (NIK) 16 digit untuk mencari data penumpang: ")
        if len(NIK) == 16 and NIK.isdigit():
            break
        else:
            print("\nNIK harus berupa angka dan terdiri dari 16 digit. Silakan coba lagi.")
    # Mencari data penumpang berdasarkan NIK
    data_penumpang = table.get(NIK)
    # Menampilkan data penumpang jika ditemukan
    if data_penumpang:
        convert_to_table(
        data=[data_penumpang], 
        columns=['Nomor', 'Nama Penumpang', 'Nomor Induk\nKependudukan', 'Maskapai\nPenerbangan', 'Kode\nPenerbangan', 'Bandara\nKeberangkatan', 'Bandara Tujuan', 'Kota\nKeberangkatan', 'Kota Tujuan', 'Waktu\nKeberangakatan', 'Waktu Tiba', 'Tanggal'],
        title=f'\nBerikut Daftar Penumpang dengan NIK: {NIK}\n'
        )
    else:
        print(f"\nData untuk NIK {NIK} tidak ditemukan. Pastikan NIK Anda terdaftar.\n")
        
def nomor_2(pilihan):
    """Fungsi menu di pilihan nomor 2"""
    while True:
        print('''
        ======== Registrasi Data Penumpang ========
        1. Tambah Data Baru
        2. Kembali ke Menu Utama
        =======================================
        ''')
        pilihan = validasi_int('Silahkan tentukan pilihan Anda [1-2]: ')
        if pilihan == 1:
            tambah_data(__main__.database)
        elif pilihan == 2:
            return
        else:
            print(f'*****Pilihan {pilihan} tidak terdapat di daftar!*****')
    
def tambah_data(table):
    """Fungsi untuk menambah data penumpang baru"""
    # Mengambil daftar NIK yang sudah ada
    list_NIK = [nik for nik, data in table.items()]

    # Meminta input NIK untuk data baru
    while True:
        NIK = input("\nMasukkan Nomor Induk Kependudukan (NIK) 16 digit untuk menambah data baru: ")
        if len(NIK) == 16 and NIK.isdigit():
            if NIK in list_NIK:
                print(f"Data untuk NIK:'{NIK}' sudah ada, silahkan masukkan NIK yang lain")
            else:
                break
        else:
            print("\nNIK harus berupa angka dan terdiri dari 16 digit. Silakan coba lagi.")
    name = validasi_str('\nMasukkan nama penumpang baru: ').title()
    airlane = validasi_str('\nMasukkan nama maskapai penerbangan: ').title()  
    while True:
        flight_code = input("\nMasukkan kode penerbangan: ").upper()
        if flight_code.isalnum() and any(c.isalpha() for c in flight_code) and any(c.isdigit() for c in flight_code):
            break
        else:
            print("\nKode penerbangan yang Anda masukkan tidak sesuai")
    input_ori_airport = validasi_str("\nMasukkan bandara keberangkatan baru: ")
    ori_airport = ' '.join(word.capitalize() if word.isalpha() else word.upper() for word in input_ori_airport.split())
    input_dest_airport = validasi_str("\nMasukkan bandara penerbangan tujuan: ")
    dest_airport = ' '.join(word.capitalize() if word.isalpha() else word.upper() for word in input_dest_airport.split())
    ori_region = validasi_str("\nMasukkan daerah asal: ").title()
    dest_region = validasi_str("\nMasukkan daerah tujuan: ").title()
    dep_time = input("\nMasukkan waktu keberangkatan dalam format 'jam:menit' (contoh: 10:25): ")
    ar_time = input("\nMasukkan waktu kedatangan dalam format 'jam:menit' (contoh: 10:25): ")
    date = input("\nMasukkan tanggal penerbangan dengan format 'tahun-bulan-tanggal' (contoh: 2024-01-14): ")

    # Meminta konfirmasi untuk menyimpan data
    while True:
        konfirmasi = validasi_str('Apakah Anda yakin untuk menyimpan data? [Yes/No]: ').upper()
        if konfirmasi == 'Y' or konfirmasi == 'YES':
            print('Data Berhasil Tersimpan')
            table[NIK] = [
                len(table) + 1,
                name, 
                int(NIK),
                airlane, 
                flight_code, 
                ori_airport,
                dest_airport,
                ori_region,
                dest_region,
                dep_time,
                ar_time,
                date
            ]
            data_semua(table)
            break
        elif konfirmasi == 'N' or konfirmasi == 'NO':
            print('\nData Gagal Tersimpan')
            return  # Kembali ke menu utama
        else:
            print(f"\nMasukkan 'Yes[Y]' atau 'No[N]'!")
    return

def nomor_3(pilihan):
    while True:
        print('''
        ======== Ubah Data Penumpang ========
        1. Ubah Data Penumpang
        2. Kembali ke Menu Utama
        =======================================
        ''')
        pilihan = validasi_int('Silahkan tentukan pilihan Anda [1-2]: ')
        if pilihan == 1:
            ubah_data(__main__.database)
        elif pilihan == 2:
            return
        else:
            print(f'*****Pilihan {pilihan} tidak terdapat di daftar!*****')
            
def ubah_data(table):
    """Fungsi untuk mengubah data penumpang"""
    # Meminta NIK untuk memilih data yang akan diubah data
    while True:
        NIK = input("\nMasukkan Nomor Induk Kependudukan(NIK) untuk data penumpang yang ingin diubah: ")
        if len(NIK) == 16 and NIK.isdigit():
            if NIK in table:
                break
            else:
                print(f"\nData untuk NIK:'{NIK}' tidak tersedia. Silahkan masukkan NIK yang sesuai.")
        else:
            print("\nNIK harus berupa angka dan terdiri dari 16 digit. Silakan coba lagi.")

    # Menampilkan pilihan kolom yang akan diubah
    print("\nSilahkan pilih kolom data yang ingin Anda ubah:")
    print("1. Nama")
    print("2. Nomor Induk Kependudukan")
    print("3. Maskapai Penerbangan")
    print("4. Kode Penerbangan")
    print("5. Bandara Asal")
    print("6. Bandara Tujuan")
    print("7. Kota Asal")
    print("8. Kota Tujuan")
    print("9. Waktu Keberangkatan")
    print("10. Waktu Tiba")
    print("11. Tanggal Penerbangan")

    # Meminta pilihan kolom yang kana diubah
    while True:
        pilihan = validasi_int("\nSilahkan masukkan angka dari kolom data yang ingin Anda ubah: ")
        if pilihan.isdigit() and 1 <= pilihan <= 11:
            break
        else:
            print("\nAngka yang Anda pilih tidak terdapat di daftar.")

    # Meminta data baru untuk kolom yang dipilih
    if pilihan == 1:
        update = validasi_str('\nMasukkan nama penumpang yang baru: ').title()
    elif pilihan == 2:
        while True:
            update = input("\nMasukkan Nomor Induk Kependudukan(NIK) yang baru: ")
            if len(NIK) == 16 and NIK.isdigit():
                break
            else:
                print("\nNIK harus berupa angka dan terdiri dari 16 digit. Silakan coba lagi.")
    elif pilihan == 3:
        update = validasi_str("\nMasukkan maskapai penerbangan yang baru: ").title()
    elif pilihan == 4:
        while True:
            update = input("\nMasukkan kode penerbangan yang baru: ").upper()
            if update.isalnum() and any(c.isalpha() for c in update) and any(c.isdigit() for c in update):
                break
            else:
                print("\nKode penerbangan yang Anda masukkan tidak sesuai")
    elif pilihan == 5:
        update = validasi_str("\nMasukkan bandara keberangkatan yang baru: ").title()
    elif pilihan == 6:
        update = validasi_str("\nMasukkan bandara tujuan yang baru: ").title()
    elif pilihan == 7:
        update = validasi_str("\nMasukkan kota asal yang baru: ").title()
    elif pilihan == 8:
        update = validasi_str("\nMasukkan kota tujuan yang baru: ").title
    elif pilihan == 9:
        update = input("\nMasukkan waktu keberangkatan yang baru dalam format 'jam:menit' (contoh: 10:25): ")
    elif pilihan == 10:
        update = input("\nMasukkan waktu tiba yang baru dalam format 'jam:menit' (contoh: 10:25): ")
    elif pilihan == 11:
        update = input("\nMasukkan tanggal penerbangan yang baru dengan format 'tahun-bulan-tanggal' (contoh: 2024-01-14): ")

    # Konfirmasi untuk mengubah data
    while True:
        konfirmasi = validasi_str('Apakah Anda yakin data akan disimpan [Yes/No]: ').upper()
        if konfirmasi == 'Y' or konfirmasi == 'YES':
            print('\nData Berhasil Tersimpan!')
            # Melakukan ubah data di database
            if pilihan == 1:
                table[NIK][1] = update
            elif pilihan == 2:
                table[NIK][2] = update    
            elif pilihan == 3:
                table[NIK][3] = update
            elif pilihan == 4:
                table[NIK][4] = update
            elif pilihan == 5:
                table[NIK][5] = update
            elif pilihan == 6:
                table[NIK][6] = update
            elif pilihan == 7:
                table[NIK][7] = update
            elif pilihan == 8:
                table[NIK][8] = update
            elif pilihan == 8:
                table[NIK][9] = update
            elif pilihan == 9:
                table[NIK][10] = update
            elif pilihan == 11:
                table[NIK][11] = update

            # Menampilkan data setelah diubah
            data_semua(table)
            break
        elif konfirmasi == 'N' or konfirmasi == 'NO':
            print('\nData Gagal Tersimpan!')
            return  # Return to the main menu
        else:
            print(f"\nMasukkan 'Yes[Y]' atau 'No[N]'!")
    return

def nomor_4(pilihan):
    while True:
        print('''
        ======== Hapus Data Penumpang ========
        1. Hapus Data Penumpang
        2. Kembali ke Menu Utama
        =======================================
        ''')
        pilihan = validasi_int('Silahkan tentukan pilihan Anda [1-2]: ')
        if pilihan == 1:
            hapus_data(__main__.database)
        elif pilihan == 2:
            return
        else:
            print(f'*****Pilihan {pilihan} tidak terdapat di daftar!*****')
            
    
def hapus_data(table):
    """Fungsi untuk menghapus data penumpang berdasarkan NIK dari database."""
    # Menampilkan daftar buah yang tersedia
    data_semua(table)
    while True:
        NIK = input("\nMasukkan Nomor Induk Kependudukan(NIK) untuk data penumpang yang ingin dihapus: ")
        if len(NIK) == 16 and NIK.isdigit():
            found = False
            keys_to_delete = []  # Membuat daftar untuk menyimpan kunci yang akan dihapus
            for key, val in table.items():
                if val[2] == int(NIK):
                    while True:
                        konfirmasi = input(f"Apakah Anda yakin ingin menghapus data untuk NIK '{NIK}'? [Yes/No]: ").upper()
                        if konfirmasi == 'YES' or konfirmasi == 'Y':
                            keys_to_delete.append(key)  # Menambahkan kunci ke daftar hapus
                            print(f"\nData untuk NIK:'{NIK}' berhasil dihapus.")
                            found = True
                            break
                        elif konfirmasi == 'NO' or konfirmasi == 'N':
                            print(f"\nData untuk NIK:'{NIK}' tidak jadi dihapus.")
                            return
                        else:
                            print(f"\nMasukkan 'Yes[Y]' atau 'No[N]'!")
            # Menghapus item dari tabel setelah iterasi selesai
            for key in keys_to_delete:
                del table[key]

            if not found:
                print(f"\nData untuk NIK:'{NIK}' tidak tersedia. Silahkan masukkan NIK yang sesuai.")
            else:
                break
        else:
            print("\nNIK harus berupa angka dan terdiri dari 16 digit. Silakan coba lagi.")

    # Proses update indeks 
    for idx, item in enumerate(list(table.values())):
        if idx < item[0]:
            item[0] -= 1
    # Menampilkan daftar terkini
    data_semua(table)  