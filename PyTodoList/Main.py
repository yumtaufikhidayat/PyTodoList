def menu():
    print("Selamat Datang di Aplikasi To-Do List")
    print("1. Lihat Semua Tugas")
    print("2. Tambah Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")


def main():
    tasks = [  # Contoh data dummy
        {
            "id": 1,
            "title": "Belajar dasar Python",
            "description": "Mempelajari variabel, tipe data, dan operator",
            "status": "Selesai",
            "estimasi_waktu_pengerjaan": 60
        },
        {
            "id": 2,
            "title": "Mengerjakan latihan soal",
            "description": "Latihan membuat fungsi dan pengkondisian",
            "status": "Belum Selesai",
            "estimasi_waktu_pengerjaan": 45
        }
    ]

    while True:
        menu()
        choice = input("Masukkan pilihan Anda: ")

        if choice == '1':
            lihat_semua_tugas(tasks)
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
            print("Terima kasih telah menggunakan aplikasi To-Do List.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi untuk melihat semua tugas
def lihat_semua_tugas(tasks):
    if not tasks:
        print("\nBelum ada tugas yang ditambahkan.")
        return

    print("\nDaftar Semua Tugas:\n" + "-"*50)
    for task in tasks:
        print(f"ID            : {task['id']}")
        print(f"Judul         : {task['title']}")
        print(f"Deskripsi     : {task['description']}")
        print(f"Status        : {task['status']}")
        print(f"Estimasi Waktu: {task['estimasi_waktu_pengerjaan']} menit")
        print("-"*50)

if __name__ == "__main__":
    main()