from tabulate import tabulate
import __main__

def validasi_int(prompt):
    """
    Fungsi untuk melakukan validasi masukan integer / angka.
    """
    while True:
        try:
            num = float(input(prompt))
            if num < 0:
                print('\nAnda memasukkan angka negatif, silahkan masukkan angka yang sesuai.')
            else:
                return num
        except ValueError:
            print('\nAnda memasukkan selain angka, silahkan masukkan angka yang sesuai.')

def validasi_str(prompt):
    """
    Fungsi untuk melakukan validasi masukan string / huruf.
    """
    while True:
        word = input(prompt)
        if word.replace(' ','').isalpha():
            return word.title()
        else:
            print('\nAnda hanya bisa memasukkan karakter alfabet.')

def validasi_waktu(prompt):
    """
    Fungsi untuk melakukan validasi masukan format waktu.
    """
    while True:
        time_input = input(prompt)
        split_time = time_input.split(':')
        if len(split_time) != 2 or not split_time[0].isdigit() or not split_time[1].isdigit():
            print("\nFormat waktu tidak valid. Pastikan formatnya adalah 'jam:menit' (contoh: 10:25)")
            continue
        hour = int(split_time[0])
        minute = int(split_time[1])
        if hour < 0 or hour > 23 or minute < 0 or minute > 59:
            print("\nFormat waktu tidak valid. Pastikan jam berada dalam rentang 0-23 dan menit berada dalam rentang 0-59")
            continue
        return time_input
    
def validasi_tanggal(prompt):
    """
    Fungsi untuk melakukan validasi masukan format tanggal.
    """
    while True:
        date_input = input(prompt)
        split_date = date_input.split('-')
        if len(split_date) != 3 or not all(part.isdigit() for part in split_date):
            print("\nFormat tanggal tidak valid. Pastikan formatnya adalah 'tahun-bulan-tanggal' (contoh: 2024-01-14)")
            continue
        year = int(split_date[0])
        month = int(split_date[1])
        day = int(split_date[2])
        if year < 0 or month < 1 or month > 12 or day < 1 or day > 31:
            print("\nFormat tanggal tidak valid. Pastikan tahun, bulan, dan tanggal berada dalam rentang yang sesuai")
            continue
        return date_input            

def ubah_ke_tabel(data, columns, title):
    """
    Fungsi untuk mengkonversi data yang ada menjadi tabel.
    """
    print(title)
    print(tabulate(data, headers=columns, tablefmt="grid"))

def nomor_1(pilihan):
    """
    Fungsi menu di pilihan nomor 1
    """
    while True:
        print('''
        ======== Daftar Data Penumpang ========
        1. Data Semua Penumpang
        2. Data Penumpang Tertentu
        3. Kembali ke Menu Utama
        =======================================
        ''')
        pilihan = validasi_int('\nSilahkan tentukan pilihan Anda [1-3]: ')
        if pilihan == 1:
            data_semua(__main__.database)
        elif pilihan == 2:
            data_tertentu(__main__.database)
        elif pilihan == 3:
            __main__.clear_screen()
            return
        else:
            print(f'\n*****Pilihan {int(pilihan)} tidak terdapat di daftar!*****')
            
                
def data_semua(table):
    """
    Fungsi untuk menampilkan semua daftar penumpang.
    """
    if not __main__.database.values():
        print(f'\nDatabase kosong, silahkan tambahkan data.\n')
        pilihan_tambah = validasi_str(f'Apakah Anda ingin menambahkan data [Yes(Y)/No(N)]: ').upper()
        if pilihan_tambah == 'YES' or pilihan_tambah == 'Y':
            tambah_data(table)
        elif pilihan_tambah == 'NO' or pilihan_tambah == 'N':
            return
        else: 
            print(f"\nMasukkan 'Yes[Y]' atau 'No[N]'!")
        
    else:
        ubah_ke_tabel(
            data=__main__.database.values(), 
            columns=['Nama Penumpang', 'Nomor Induk\nKependudukan', 'Maskapai\nPenerbangan', 'Kode\nPenerbangan', 'Kode\nBandara\nKeberangkatan', 'Kode\nBandara Tujuan', 'Kota\nKeberangkatan', 'Kota Tujuan', 'Waktu\nKeberangakatan', 'Waktu Tiba', 'Tanggal'],
            title=f'\nBerikut Daftar Semua Penumpang:\n'
            )
    
def data_tertentu(table):
    """
    Fungsi untuk menampilkan daftar penumpang tertentu.
    """
    while True:
        NIK = input("\nMasukkan Nomor Induk Kependudukan (NIK) 16 digit untuk mencari data penumpang: ")
        if len(NIK) == 16 and NIK.isdigit():
            break
        else:
            print("\nNIK harus berupa angka dan terdiri dari 16 digit. Silakan coba lagi.")
    data_penumpang = table.get(NIK)
    if data_penumpang:
        ubah_ke_tabel(
        data=[data_penumpang], 
        columns=['Nama Penumpang', 'Nomor Induk\nKependudukan', 'Maskapai\nPenerbangan', 'Kode\nPenerbangan', 'Kode\nBandara\nKeberangkatan', 'Kode\nBandara Tujuan', 'Kota\nKeberangkatan', 'Kota Tujuan', 'Waktu\nKeberangakatan', 'Waktu Tiba', 'Tanggal'],
        title=f'\nBerikut Daftar Penumpang dengan NIK: {NIK}\n'
        )
    else:
        print(f"\nData untuk NIK {NIK} tidak ditemukan. Pastikan NIK Anda terdaftar.\n")
        
def nomor_2(pilihan):
    """
    Fungsi menu di pilihan nomor 2
    """
    while True:
        print('''
        ======== Registrasi Data Penumpang ========
        1. Registrasi Penumpang Baru
        2. Kembali ke Menu Utama
        =======================================
        ''')
        pilihan = validasi_int('\nSilahkan tentukan pilihan Anda [1-2]: ')
        if pilihan == 1:
            tambah_data(__main__.database)
        elif pilihan == 2:
            __main__.clear_screen()
            return
        else:
            print(f'\n*****Pilihan {int(pilihan)} tidak terdapat di daftar!*****')
    
def tambah_data(table):
    """
    Fungsi untuk menambah data penumpang baru
    """
    list_NIK = [nik for nik, data in table.items()]
    while True:
        NIK = input("\nMasukkan Nomor Induk Kependudukan (NIK) 16 digit untuk menambah data baru: ")
        if len(NIK) == 16 and NIK.isdigit():
            if NIK in list_NIK:
                print(f"\nData untuk NIK:'{NIK}' sudah ada, silahkan masukkan NIK yang lain")
            else:
                break
        else:
            print("\nNIK harus berupa angka dan terdiri dari 16 digit. Silakan coba lagi.")
    name = validasi_str('\nMasukkan nama penumpang baru: ').title()
    airlane = validasi_str('\nMasukkan nama maskapai penerbangan: ').title()  
    while True:
        flight_code = input("\nMasukkan kode penerbangan (contoh: JT2098): ").upper()
        if len(flight_code) == 6 and flight_code.isalnum() and any(c.isalpha() for c in flight_code) and any(c.isdigit() for c in flight_code):
            break
        else:
            print("\nKode penerbangan tidak sesuai, harus terdiri dari dua huruf dan empat angka (contoh: JT1234)")
    while True:
        ori_airport = validasi_str("\nMasukkan kode bandara keberangkatan (contoh: CGK): ").upper()
        if len(ori_airport) == 3:
            break
        else:
            print("\nKode bandara harus terdiri dari 3 huruf. Silakan coba lagi.")
    while True:
        dest_airport = validasi_str("\nMasukkan bandara penerbangan tujuan (contoh: CGK): ").upper()
        if len(ori_airport) == 3:
            break
        else:
            print("\nKode bandara harus terdiri dari 3 huruf. Silakan coba lagi.")
    ori_region = validasi_str("\nMasukkan daerah keberangkatan: ").title()
    dest_region = validasi_str("\nMasukkan daerah tujuan: ").title()
    dep_time = validasi_waktu("\nMasukkan waktu keberangkatan dalam format 'jam:menit' (contoh: 10:25): ")
    ar_time = validasi_waktu("\nMasukkan waktu kedatangan dalam format 'jam:menit' (contoh: 10:25): ")
    date = validasi_tanggal("\nMasukkan tanggal penerbangan dengan format 'tahun-bulan-tanggal' (contoh: 2024-01-14): ")
    data_baru = ({NIK: [name, int(NIK), str(airlane), str(flight_code), str(ori_airport), str(dest_airport), str(ori_region), str(dest_region), str(dep_time), str(ar_time), str(date)]})
    
    ubah_ke_tabel(
            data=data_baru.values(), 
            columns=['Nama Penumpang', 'Nomor Induk\nKependudukan', 'Maskapai\nPenerbangan', 'Kode\nPenerbangan', 'Kode\nBandara\nKeberangkatan', 'Kode\nBandara Tujuan', 'Kota\nKeberangkatan', 'Kota Tujuan', 'Waktu\nKeberangakatan', 'Waktu Tiba', 'Tanggal'],
            title=f'\nBerikut Data Penumpang Baru:\n'
            )
    
    while True:
        konfirmasi = validasi_str('\nApakah Anda yakin untuk menyimpan data? [Yes(Y)/No(N)]: ').upper()
        if konfirmasi == 'Y' or konfirmasi == 'YES':
            print('Data Berhasil Tersimpan')
            table[NIK] = [
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
            return  
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
        pilihan = validasi_int('\nSilahkan tentukan pilihan Anda [1-2]: ')
        if pilihan == 1:
            ubah_data(__main__.database)
        elif pilihan == 2:
            __main__.clear_screen()
            return
        else:
            print(f'\n*****Pilihan {int(pilihan)} tidak terdapat di daftar!*****')
            
def ubah_data(table):
    """
    Fungsi untuk mengubah data penumpang
    """
    while True:
        NIK = input("\nMasukkan Nomor Induk Kependudukan(NIK) untuk data penumpang yang ingin diubah: ")
        if NIK in table:
            data_penumpang = table.get(NIK)
            ubah_ke_tabel(
                data=[data_penumpang], 
                columns=['Nama Penumpang', 'Nomor Induk\nKependudukan', 'Maskapai\nPenerbangan', 'Kode\nPenerbangan', 'Kode\nBandara\nKeberangkatan', 'Kode\nBandara Tujuan', 'Kota\nKeberangkatan', 'Kota Tujuan', 'Waktu\nKeberangkatan', 'Waktu Tiba', 'Tanggal'],
                title=f'\nBerikut Daftar Penumpang dengan NIK: {NIK}\n'
            )
            while True:
                konfirmasi = input("\nApakah Anda ingin mengubah data penumpang ini [Yes(Y)/No(N)]: ").upper()
                if konfirmasi == 'Y' or konfirmasi == 'YES':
                    print("\nSilahkan pilih kolom data yang ingin Anda ubah:")
                    print("1. Nama")
                    print("2. Nomor Induk Kependudukan")
                    print("3. Maskapai Penerbangan")
                    print("4. Kode Penerbangan")
                    print("5. Kode bandara keberangkatan")
                    print("6. Bandara Tujuan")
                    print("7. Kota Keberangkatan")
                    print("8. Kota Tujuan")
                    print("9. Waktu Keberangkatan")
                    print("10. Waktu Tiba")
                    print("11. Tanggal Penerbangan")

                    while True:
                        pilihan = input("\nSilahkan masukkan angka dari kolom data yang ingin Anda ubah: ")
                        if pilihan.isdigit() and 1 <= int(pilihan) <= 11:
                            pilihan = int(pilihan)
                            break
                        else:
                            print("\nYang Anda pilih tidak terdapat di daftar.")
                    
                    if pilihan == 1:
                        update = validasi_str('\nMasukkan nama penumpang yang baru: ').title()
                    elif pilihan == 2:
                        list_NIK = [nik for nik, data in table.items()]
                        while True:
                            NIK = input("\nMasukkan Nomor Induk Kependudukan (NIK) 16 digit untuk menambah data baru: ")
                            if len(NIK) == 16 and NIK.isdigit():
                                if NIK in list_NIK:
                                    print(f"\nNIK:'{NIK}' sudah ada, silahkan masukkan NIK yang lain.")
                                else:
                                    break   
                            else:
                                print("\nNIK harus berupa angka dan terdiri dari 16 digit. Silakan coba lagi.")
                    elif pilihan == 3:
                        update = validasi_str("\nMasukkan maskapai penerbangan yang baru: ").title()
                    elif pilihan == 4:
                        while True:
                            update = input("\nMasukkan kode penerbangan yang baru: ").upper()
                            if len(update) == 6 and update.isalnum() and any(c.isalpha() for c in update) and any(c.isdigit() for c in update):
                                break
                            else:
                                print("\nKode penerbangan tidak sesuai, harus terdiri dari dua huruf dan empat angka (contoh: JT1234)")
                    elif pilihan == 5:
                        while True:
                            update = validasi_str("\nMasukkan kode bandara keberangkatan yang baru: ").upper()
                            if len(update) == 3:
                                break
                            else:
                                print("\nKode bandara harus terdiri dari 3 huruf. Silakan coba lagi.")
                    elif pilihan == 6:
                        while True:
                            update = validasi_str("\nMasukkan bandara tujuan yang baru: ").upper()
                            if len(update) == 3:
                                break
                            else:
                                print("\nKode bandara harus terdiri dari 3 huruf. Silakan coba lagi.")
                    elif pilihan == 7:
                        update = validasi_str("\nMasukkan kota keberangkatan yang baru: ").title()
                    elif pilihan == 8:
                        update = validasi_str("\nMasukkan kota tujuan yang baru: ").title
                    elif pilihan == 9:
                        update = validasi_waktu("\nMasukkan waktu keberangkatan yang baru dalam format 'jam:menit' (contoh: 10:25): ")
                    elif pilihan == 10:
                        update = validasi_waktu("\nMasukkan waktu tiba yang baru dalam format 'jam:menit' (contoh: 10:25): ")
                    elif pilihan == 11:
                        update = validasi_tanggal("\nMasukkan tanggal penerbangan yang baru dengan format 'tahun-bulan-tanggal' (contoh: 2024-01-14): ")

                    while True:
                        konfirmasi = input('\nApakah Anda yakin data akan disimpan [Yes(Y)/No(N)]: ').upper()
                        if konfirmasi == 'Y' or konfirmasi == 'YES':
                            print('\nData Berhasil Tersimpan!')
                            if pilihan == 1:
                                table[NIK][0] = update
                            elif pilihan == 2:
                                table[NIK][1] = update    
                            elif pilihan == 3:
                                table[NIK][2] = update
                            elif pilihan == 4:
                                table[NIK][3] = update
                            elif pilihan == 5:
                                table[NIK][4] = update
                            elif pilihan == 6:
                                table[NIK][5] = update
                            elif pilihan == 7:
                                table[NIK][6] = update
                            elif pilihan == 8:
                                table[NIK][7] = update
                            elif pilihan == 9:
                                table[NIK][8] = update
                            elif pilihan == 10:
                                table[NIK][9] = update
                            elif pilihan == 11:
                                table[NIK][10] = update
                            data_semua(table)
                            return
                        elif konfirmasi == 'N' or konfirmasi == 'NO':
                            print('\nData Gagal Tersimpan!')
                            return 
                        else:
                            print(f"\nMasukkan 'Yes[Y]' atau 'No[N]'!")
                elif konfirmasi == 'N' or konfirmasi == 'NO':
                    print('\nBatal mengubah data.')
                    return
                else:
                    print("\nMasukkan 'Yes[Y]' atau 'No[N]'!")
        else:
            print(f"\nData untuk NIK:'{NIK}' tidak tersedia. Silahkan masukkan NIK yang sesuai.")
            
def nomor_4(pilihan):
    while True:
        print('''
        ======== Hapus Data Penumpang ========
        1. Hapus Data Penumpang
        2. Kembali ke Menu Utama
        =======================================
        ''')
        pilihan = validasi_int('\nSilahkan tentukan pilihan Anda [1-2]: ')
        if pilihan == 1:
            hapus_data(__main__.database)
        elif pilihan == 2:
            __main__.clear_screen()
            return
        else:
            print(f'\n*****Pilihan {int(pilihan)} tidak terdapat di daftar!*****')
               
def hapus_data(table):
    """
    Fungsi untuk menghapus data penumpang berdasarkan NIK dari database.
    """
    data_semua(table)
    while True:
        NIK = input("\nMasukkan Nomor Induk Kependudukan(NIK) untuk data penumpang yang ingin dihapus: ")
        if len(NIK) == 16 and NIK.isdigit():
            found = False
            keys_to_delete = []  
            for key, val in table.items():
                if val[1] == int(NIK):
                    while True:
                        konfirmasi = input(f"Apakah Anda yakin ingin menghapus data untuk NIK '{NIK}'? [Yes(Y)/No(N)]: ").upper()
                        if konfirmasi == 'YES' or konfirmasi == 'Y':
                            keys_to_delete.append(key) 
                            print(f"\nData untuk NIK:'{NIK}' berhasil dihapus.")
                            found = True
                            break
                        elif konfirmasi == 'NO' or konfirmasi == 'N':
                            print(f"\nData untuk NIK:'{NIK}' tidak jadi dihapus.")
                            return
                        else:
                            print(f"\nMasukkan 'Yes[Y]' atau 'No[N]'!")
            for key in keys_to_delete:
                del table[key]

            if not found:
                print(f"\nData untuk NIK:'{NIK}' tidak tersedia. Silahkan masukkan NIK yang sesuai.")
            else:
                break
        else:
            print("\nNIK harus berupa angka dan terdiri dari 16 digit. Silakan coba lagi.")
    data_semua(table)  