def menu():
    print("Selamat Datang di Aplikasi To-Do List")
    print("1. Lihat Semua Tugas")
    print("2. Tambah Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")


def main():
    tasks = []  # List untuk menyimpan tugas

    while True:
        menu()
        choice = input("Masukkan pilihan Anda: ")

        if choice == '1':
            # Logika untuk menampilkan tugas
            pass
        elif choice == '2':
            # Logika untuk menambahkan tugas
            pass
        elif choice == '3':
            # Logika untuk menandai tugas selesai
            pass
        elif choice == '4':
            # Logika untuk menghapus tugas
            pass
        elif choice == '5':
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()