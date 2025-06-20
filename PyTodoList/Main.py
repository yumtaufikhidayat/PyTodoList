def menu():
    print("Selamat Datang di Aplikasi To-Do List")
    print("1. Lihat Semua Tugas")
    print("2. Tambah Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")


def main():
    tasks = [
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
            see_all_tasks(tasks)
        elif choice == '2':
            add_new_tasks(tasks)
            pass
        elif choice == '3':
            mark_complete(tasks)
            pass
        elif choice == '4':
            # Logika untuk menghapus tugas
            pass
        elif choice == '5':
            print("Terima kasih telah menggunakan aplikasi To-Do List.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

def see_all_tasks(tasks):
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

def add_new_tasks(task):
    title = input("Masukkan judul tugas: ")
    description = input("Masukkan deskripsi tugas: ")
    status = input("Masukkan status tugas (Selesai/Belum Selesai): ")
    estimasi_waktu = input("Masukkan estimasi waktu pengerjaan (menit): ")

    new_task = {
        "id": len(task) + 1,  # Auto-increment ID
        "title": title,
        "description": description,
        "status": status,
        "estimasi_waktu_pengerjaan": estimasi_waktu
    }
    task.append(new_task)
    print("Tugas berhasil ditambahkan!")

def mark_complete(task):
    id_tugas = int(input("Masukkan ID tugas yang ingin ditandai selesai: "))
    for tugas_item in task:
        if tugas_item["id"] == id_tugas:
            tugas_item["status"] = "Selesai"
            print("Tugas berhasil diperbarui menjadi selesai!")
            return
    print("ID tugas tidak ditemukan.")

if __name__ == "__main__":
    main()