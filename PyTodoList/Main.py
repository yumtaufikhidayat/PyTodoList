def menu():
    print("\nSelamat Datang di Aplikasi To-Do List")
    print("1. Lihat Semua Tugas")
    print("2. Tambah Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Keluar")

def see_all_tasks(tasks):
    if not tasks:
        print("\nBelum ada tugas yang ditambahkan.")
        return

    print("\nDaftar Semua Tugas:\n" + "-" * 50)
    for task in tasks:
        print(f"ID            : {task['id']}")
        print(f"Judul         : {task['title']}")
        print(f"Deskripsi     : {task['description']}")
        print(f"Status        : {task['status']}")
        print(f"Estimasi Waktu: {task['estimasi_waktu_pengerjaan']} menit")
        print("-" * 50)


def generate_new_id(tasks):
    return max([task["id"] for task in tasks], default=0) + 1


def add_new_task(tasks):
    title = input("Masukkan judul tugas: ")
    description = input("Masukkan deskripsi tugas: ")

    status = input("Masukkan status tugas (Selesai/Belum Selesai): ").strip()
    while status not in ["Selesai", "Belum Selesai"]:
        print("Status tidak valid. Masukkan 'Selesai' atau 'Belum Selesai'.")
        status = input("Masukkan status tugas (Selesai/Belum Selesai): ").strip()

    try:
        estimasi = int(input("Masukkan estimasi waktu pengerjaan (menit): "))
    except ValueError:
        print("Estimasi harus berupa angka.")
        return

    new_task = {
        "id": generate_new_id(tasks),
        "title": title,
        "description": description,
        "status": status,
        "estimasi_waktu_pengerjaan": estimasi
    }
    tasks.append(new_task)
    print("Tugas berhasil ditambahkan!")


def mark_complete(tasks):
    try:
        task_id = int(input("Masukkan ID tugas yang ingin ditandai selesai: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    for task in tasks:
        if task["id"] == task_id:
            if task["status"] == "Selesai":
                print("Tugas ini sudah selesai sebelumnya.")
            else:
                task["status"] = "Selesai"
                print("Tugas berhasil ditandai selesai.")
            return
    print("ID tugas tidak ditemukan.")

def delete_task(tasks):
    see_all_tasks(tasks)
    try:
        task_id = int(input("Masukkan ID tugas yang ingin dihapus: "))
    except ValueError:
        print("ID harus berupa angka.")
        return

    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("🗑️  Tugas berhasil dihapus.")
            return
    print("ID tugas tidak ditemukan.")


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
        choice = input("Masukkan pilihan Anda: ").strip()

        if choice == '1':
            see_all_tasks(tasks)
        elif choice == '2':
            add_new_task(tasks)
        elif choice == '3':
            mark_complete(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("👋 Terima kasih telah menggunakan aplikasi To-Do List.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")


if __name__ == "__main__":
    main()