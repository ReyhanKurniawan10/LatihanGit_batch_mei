# Code Completion

# == Program Manajemen Koleksi Film Favorit ==
# Tujuan: menyimpan dan menampilkan informasi film yang dimiliki pengguna


"""
============= Deskripsi Singkat Program =============

Program ini membantu pengguna mencatat daftar film favorit mereka, termasuk informasi:
- Judul
- Genre
- Tahun rilis

Data akan disimpan dalam sebuah list of dictionaries, dan peserta diminta melengkapi fungsi-fungsi utama seperti:
- Menambahkan film
- Menampilkan seluruh film
- Menampilkan film berdasarkan genre tertentu
"""


# List untuk menyimpan koleksi film (setiap film disimpan dalam dictionary)
koleksi_film = []

print("=== Selamat Datang di Program Koleksi Film ===")

# Program berjalan hingga pengguna memilih keluar
while True:
    print("\nMenu:")
    print("1. Tambah Film")
    print("2. Tampilkan Semua Film")
    print("3. Cari Film Berdasarkan Genre")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan (1-4): ")

    if pilihan == '1':
        print("\n== Tambah Film Baru ==")
        judul = input("Judul film: ")
        genre = input("Genre film: ").lower()
        tahun = input("Tahun rilis: ")

        # TODO: Buat dictionary untuk menyimpan data film
        film_baru = {}

        # TODO: Tambahkan dictionary ke dalam koleksi_film
        film_baru['Judul Film'] = judul
        film_baru['Genre Film'] = genre
        film_baru['Tahun Rilis'] = tahun

        koleksi_film.append(film_baru)

        print("Film berhasil ditambahkan!")

        # print(koleksi_film)

    elif pilihan == '2':
        print("\n== Daftar Koleksi Film ==")

        # TODO: Cek apakah koleksi kosong
        berisi = len(koleksi_film)
        if len(koleksi_film) == 0:
            print("Belum ada film dalam koleksi.")
        else:
            print("Jumlah film:", len(koleksi_film))
            print("Berikut daftar film:")
            # TODO: Gunakan loop untuk menampilkan semua film
            # Format: "Judul (Genre, Tahun)"
            for item in koleksi_film:
                # formFilm = ''
                # formFilm2 = ''
                for value in len(item):
                    print(f'{item['Judul Film'][value]} ({item['Genre Film'][value]}, {item['Tahun Rilis'][value]})')
                    # formFilm = value
                    # formFilm2 = formFilm2 + ' ' + formFilm
                # print(formFilm2)
                # pass

    elif pilihan == '3':
        print("\n== Cari Film Berdasarkan Genre ==")
        cari_genre = input("Masukkan genre yang ingin dicari: ").lower()
        ditemukan = False

        # TODO: Loop untuk mencari film dengan genre yang sesuai
        for dictionary in koleksi_film:
            if cari_genre in dictionary['Genre Film']:
                print(dictionary['Judul Film'])
                ditemukan = True

        if not ditemukan:
            print("Tidak ada film dengan genre tersebut.")

    elif pilihan == '4':
        print("\nTerima kasih telah menggunakan program ini!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1 - 4.")
