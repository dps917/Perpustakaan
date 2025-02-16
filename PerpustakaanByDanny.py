from tabulate import tabulate

# Data awal
books = [
    {'ISBN': '9780451526342', 'namaBuku': 'Animal Farm', 'kategoriBuku': 'Novel Fiksi', 'stokBuku': 8, 'harga': 7000},
    {'ISBN': '9780060850524', 'namaBuku': 'Brave New World', 'kategoriBuku': 'Novel Fiksi', 'stokBuku': 2, 'harga': 9500},
    {'ISBN': '9780747532699', 'namaBuku': "Harry Potter and the Philosopher's Stone", 'kategoriBuku': 'Novel Fiksi', 'stokBuku': 11, 'harga': 12000},
    {'ISBN': '9780141439518', 'namaBuku': 'Pride and Prejudice', 'kategoriBuku': 'Novel Fiksi', 'stokBuku': 4, 'harga': 8500},
    {'ISBN': '9780316769488', 'namaBuku': 'The Catcher in the Rye', 'kategoriBuku': 'Novel Fiksi', 'stokBuku': 9, 'harga': 10000},
    {'ISBN': '9780743273565', 'namaBuku': 'The Great Gatsby', 'kategoriBuku': 'Novel Fiksi', 'stokBuku': 10, 'harga': 8000},
    {'ISBN': '9780345339683', 'namaBuku': 'The Hobbit', 'kategoriBuku': 'Novel Fiksi', 'stokBuku': 3, 'harga': 11000},
    {'ISBN': '9780061120084', 'namaBuku': 'To Kill a Mockingbird', 'kategoriBuku': 'Novel Fiksi', 'stokBuku': 9, 'harga': 10000},
    {'ISBN': '9781524763138', 'namaBuku': 'Becoming', 'kategoriBuku': 'Novel Non-Fiksi', 'stokBuku': 12, 'harga': 15000},
    {'ISBN': '9780399590504', 'namaBuku': 'Educated', 'kategoriBuku': 'Novel Non-Fiksi', 'stokBuku': 15, 'harga': 15000},
    {'ISBN': '9780316322409', 'namaBuku': 'I Am Malala', 'kategoriBuku': 'Novel Non-Fiksi', 'stokBuku': 6, 'harga': 11000},
    {'ISBN': '9780385494786', 'namaBuku': 'Into Thin Air', 'kategoriBuku': 'Novel Non-Fiksi', 'stokBuku': 4, 'harga': 13000},
    {'ISBN': '9780062316110', 'namaBuku': 'Sapiens: A Brief History of Humankind', 'kategoriBuku': 'Novel Non-Fiksi', 'stokBuku': 10, 'harga': 18000},
    {'ISBN': '9780553296983', 'namaBuku': 'The Diary of a Young Girl', 'kategoriBuku': 'Novel Non-Fiksi', 'stokBuku': 3, 'harga': 14000},
    {'ISBN': '9781400052189', 'namaBuku': 'The Immortal Life of Henrietta Lacks', 'kategoriBuku': 'Novel Non-Fiksi', 'stokBuku': 9, 'harga': 16000},
    {'ISBN': '9780812974492', 'namaBuku': 'Unbroken', 'kategoriBuku': 'Novel Non-Fiksi', 'stokBuku': 1, 'harga': 10000},
    {'ISBN': '9780812988404', 'namaBuku': 'When Breath Becomes Air', 'kategoriBuku': 'Novel Non-Fiksi', 'stokBuku': 1, 'harga': 12000},
    {'ISBN': '9780735211292', 'namaBuku': 'Atomic Habits', 'kategoriBuku': 'Pengembangan Diri', 'stokBuku': 9, 'harga': 14000},
    {'ISBN': '9781592408412', 'namaBuku': 'Daring Greatly', 'kategoriBuku': 'Pengembangan Diri', 'stokBuku': 7, 'harga': 12000},
    {'ISBN': '9781455586691', 'namaBuku': 'Deep Work', 'kategoriBuku': 'Pengembangan Diri', 'stokBuku': 8, 'harga': 14000},
    {'ISBN': '9781501111105', 'namaBuku': 'Grit', 'kategoriBuku': 'Pengembangan Diri', 'stokBuku': 4, 'harga': 12000},
    {'ISBN': '9780345472328', 'namaBuku': 'Mindset', 'kategoriBuku': 'Pengembangan Diri', 'stokBuku': 3, 'harga': 15000},
    {'ISBN': '9780743269513', 'namaBuku': 'The 7 Habits of Highly Effective People', 'kategoriBuku': 'Pengembangan Diri', 'stokBuku': 2, 'harga': 16000},
    {'ISBN': '9781577314806', 'namaBuku': 'The Power of Now', 'kategoriBuku': 'Pengembangan Diri', 'stokBuku': 13, 'harga': 15000},
    {'ISBN': '9780062457714', 'namaBuku': 'The Subtle Art of Not Giving a F*ck', 'kategoriBuku': 'Pengembangan Diri', 'stokBuku': 2, 'harga': 11000},
    {'ISBN': '9780449214923', 'namaBuku': 'Think and Grow Rich', 'kategoriBuku': 'Pengembangan Diri', 'stokBuku': 11, 'harga': 18000},
    {'ISBN': '9780393317558', 'namaBuku': 'Guns, Germs, and Steel', 'kategoriBuku': 'Sejarah Dunia', 'stokBuku': 9, 'harga': 14000},
    {'ISBN': '9780802121102', 'namaBuku': 'SPQR', 'kategoriBuku': 'Sejarah Dunia', 'stokBuku': 2, 'harga': 10000},
    {'ISBN': '9780743210752', 'namaBuku': 'Team of Rivals', 'kategoriBuku': 'Sejarah Dunia', 'stokBuku': 9, 'harga': 15000},
    {'ISBN': '9780060889572', 'namaBuku': 'The Crusades', 'kategoriBuku': 'Sejarah Dunia', 'stokBuku': 5, 'harga': 8000},
    {'ISBN': '9781605209848', 'namaBuku': 'The Habsburgs', 'kategoriBuku': 'Sejarah Dunia', 'stokBuku': 3, 'harga': 11000},
    {'ISBN': '9780393059748', 'namaBuku': 'The History of the Ancient World', 'kategoriBuku': 'Sejarah Dunia', 'stokBuku': 6, 'harga': 9000},
    {'ISBN': '9780805059524', 'namaBuku': 'The Plantagenets', 'kategoriBuku': 'Sejarah Dunia', 'stokBuku': 11, 'harga': 12000},
    {'ISBN': '9781451651683', 'namaBuku': 'The Rise and Fall of the Third Reich', 'kategoriBuku': 'Sejarah Dunia', 'stokBuku': 1, 'harga': 8500},
    {'ISBN': '9781408839975', 'namaBuku': 'The Silk Roads', 'kategoriBuku': 'Sejarah Dunia', 'stokBuku': 5, 'harga': 13000}
]

members = [{'fullname': 'Danny Permata Simanjuntak', 'username': 'danny123', 'usia': 33, 'jenis_kelamin': 'L', 'borrowed': []}]
admin_username = "admin"
current_member = None

KATEGORI_BUKU = {
    "1": "Novel Fiksi",
    "2": "Novel Non-Fiksi",
    "3": "Pengembangan Diri",
    "4": "Sejarah Dunia"
}

# Helper functions
def enter_to_continue():
    input("\nTekan Enter untuk melanjutkan...")

def display_error(message):
    print(f"\nError: {message}")
    enter_to_continue()

def validate_numeric_input(prompt, error_msg="Input harus berupa angka"):
    while True:
        value = input(prompt)
        if value.isdigit():
            return int(value)
        print(error_msg)

def validate_name_input(prompt, error_msg="Nama hanya boleh berisi huruf dan spasi"):
    while True:
        value = input(prompt).strip()
        if value and value.replace(" ", "").isalpha():
            return value
        print(error_msg)

def display_books(book_list):
    if not book_list:
        print("Tidak ada buku yang tersedia.")
        return

    headers = ["No", "ISBN", "Nama Buku", "Kategori Buku", "Stok", "Harga"]
    table = [[i, b["ISBN"], b["namaBuku"], b["kategoriBuku"], b["stokBuku"], b["harga"]]
             for i, b in enumerate(book_list, start=1)]
    print(tabulate(table, headers=headers, tablefmt="grid"))

def display_borrowed_books(book_list):
    if not book_list:
        print("Tidak ada buku yang dipinjam.")
        return

    headers = ["No", "ISBN", "Nama Buku", "Kategori Buku", "Stok", "Harga", "SubTotal"]
    table = [[i, b["ISBN"], b["namaBuku"], b["kategoriBuku"], b["stokBuku"],
              b["harga"], b.get("SubTotal", b["harga"])]
             for i, b in enumerate(book_list, start=1)]
    print(tabulate(table, headers=headers, tablefmt="grid"))

def find_book(isbn_or_title):
    return next((book for book in books
                 if book["ISBN"] == isbn_or_title or
                 book["namaBuku"].lower() == isbn_or_title.lower()), None)

def sort_books_by_command(book_list, command):
    sort_options = {
        "1": lambda x: x["harga"],
        "2": lambda x: (-x["harga"]),
        "3": lambda x: x["namaBuku"].lower(),
        "4": lambda x: x["namaBuku"].lower(),
    }

    if command in sort_options:
        return sorted(book_list, key=sort_options[command],
                     reverse=(command == "4"))
    return book_list
# Main Menu
def main_menu():
    global books
    while True:
        books = sorted(books, key=lambda x: (x["kategoriBuku"].lower(), x["namaBuku"].lower()))
        print("\n=== Menu Utama ===")
        print("1. Tamu")
        print("2. Anggota Perpustakaan")
        print("3. Pustakawan")
        print("4. Keluar")
        choice = input("Pilih menu: ")
        if choice == "1":
            menu_tamu()
        elif choice == "2":
            menu_anggota_perpustakaan()
        elif choice == "3":
            menu_pustakawan()
        elif choice == "4":
            print("Terima kasih telah menggunakan program ini.")
            break
        else:
            print("Pilihan tidak valid.")

# Menu Tamu
def menu_tamu():
    while True:
        print("\n--- Menu Tamu ---")
        print("1. Tampilkan rak buku")
        print("2. Kembali")
        choice = input("Pilih opsi: ")
        if choice == "1":
            menu_rak_buku()
        elif choice == "2":
            break
        else:
            print("Pilihan tidak valid.")

# Menu Rak Buku
def menu_rak_buku():
    global books
    while True:
        print("\n--- Menu Rak Buku ---")
        display_books(books)
        print("\nPerintah yang tersedia:")
        print("1. Urutkan berdasarkan harga terendah")
        print("2. Urutkan berdasarkan harga tertinggi")
        print("3. Urutkan berdasarkan judul A-Z")
        print("4. Urutkan berdasarkan judul Z-A")
        print("5. Kembali")
        cmd = input("Perintah: ")
        if cmd in ["1", "2", "3", "4"]:
            books = sort_books_by_command(books, cmd)
        elif cmd == "5":
            break
        else:
            print("Perintah tidak dikenali!")

# Menu Anggota Perpustakaan
def menu_anggota_perpustakaan():
    while True:
        print("\n--- Menu Anggota Perpustakaan ---")
        print("1. Login")
        print("2. Daftar Anggota Baru")
        print("3. Kembali")
        choice = input("Pilih opsi: ")
        if choice == "1":
            login_anggota()
        elif choice == "2":
            menu_daftar_anggota_baru()
        elif choice == "3":
            break
        else:
            print("Pilihan tidak valid.")

# Login Anggota
def login_anggota():
    global current_member
    attempts = 0
    while attempts < 3:
        username = input("Masukkan username: ")
        member = next((m for m in members if m["username"] == username), None)
        if member:
            current_member = member
            print(f"Selamat datang, {member['fullname']}!")
            menu_anggota_logged_in()
            break
        else:
            attempts += 1
            print(f"Username tidak ditemukan. Percobaan ke-{attempts}/3.")
    if attempts >= 3:
        print("Kesempatan habis. Kembali ke menu sebelumnya.")

# Menu Anggota yang Sudah Login
def menu_anggota_logged_in():
    global current_member
    while True:
        print("\n--- Menu Anggota (Logged In) ---")
        print("1. Tampilkan rak buku")
        print("2. Pinjam buku")
        print("3. Kembalikan buku")
        print("4. Logout")
        choice = input("Pilih opsi: ")
        if choice == "1":
            menu_rak_buku()
        elif choice == "2":
            pinjam_buku()
        elif choice == "3":
            kembalikan_buku()
        elif choice == "4":
            current_member = None
            print("Anda telah berhasil logout.")
            break
        else:
            print("Pilihan tidak valid.")

# Menu Daftar Anggota Baru
def menu_daftar_anggota_baru():
    global current_member
    print("\n--- Menu Daftar Anggota Baru ---")
    fullname = validate_name_input("Masukkan nama lengkap: ")
    username = ""
    while not username.isalnum():
        username = input("Masukkan username: ")
        if not username.isalnum():
            print("Username harus berupa karakter alfanumerik (hanya huruf dan angka).")
        elif any(member["username"] == username for member in members):
            print("Username sudah digunakan. Silakan pilih username lain.")
            username = ""
    usia = validate_numeric_input("Masukkan usia: ")
    gender = ""
    while gender not in ["L", "P"]:
        gender = input("Masukkan jenis kelamin (L/P): ").upper()
        if gender not in ["L", "P"]:
            print("Jenis kelamin hanya boleh 'L' (laki-laki) atau 'P' (perempuan).")
    new_member = {
        "fullname": fullname,
        "username": username,
        "usia": usia,
        "jenis_kelamin": gender,
        "borrowed": []
    }
    members.append(new_member)
    print("Pendaftaran berhasil!")

# Pinjam Buku
def pinjam_buku():
    display_books(books)
    global current_member
    borrowed_books = {}  # key: ISBN, value: book info + 'quantity'
    
    while True:
        isbn_or_title = input("Masukkan ISBN atau judul buku ('c' untuk membatalkan, 'x' untuk selesai): ")
        
        if isbn_or_title.lower() == "c":
            print("Peminjaman dibatalkan.")
            break
        
        elif isbn_or_title.lower() == "x":
            if borrowed_books:
                total_cost = display_selected_books(borrowed_books)
                payment = validate_numeric_input("Masukkan jumlah uang untuk membayar: ")
                
                if payment >= total_cost:
                    print("Pembayaran berhasil! Buku berhasil dipinjam.")
                    print(f"Sisa uang kembalian: Rp {payment - total_cost}")
                    break
                else:
                    print("Pembayaran gagal. Silakan coba lagi.")
            else:
                print("Tidak ada buku yang dipilih.")
                break
        else:
            found_book = find_book(isbn_or_title)
            if found_book:
                reserved_qty = borrowed_books.get(found_book["ISBN"], {}).get("quantity", 0)
                if found_book["stokBuku"] - reserved_qty > 0:
                    if found_book["ISBN"] in borrowed_books:
                        borrowed_books[found_book["ISBN"]]["quantity"] += 1
                    else:
                        borrowed_books[found_book["ISBN"]] = {
                            "ISBN": found_book["ISBN"],
                            "namaBuku": found_book["namaBuku"],
                            "kategoriBuku": found_book["kategoriBuku"],
                            "harga": found_book["harga"],
                            "quantity": 1
                        }
                    print(f"Buku '{found_book['namaBuku']}' berhasil ditambahkan ke daftar pinjaman.")
                    x = 0
                else:
                    print("Stok buku habis.")
                    x = 1
            else:
                print("Buku tidak ditemukan.")
            enter_to_continue()
        if borrowed_books:
            for isbn, selected in borrowed_books.items():
                for b in books:
                    if b["ISBN"] == isbn:
                        if b["stokBuku"] > 0:
                            b["stokBuku"] -= 1
                        break
                if x == 0:
                    for copy_index in range(selected["quantity"]):
                        current_member.setdefault("borrowed", []).append(isbn)        
        display_books(books)
    

# Kembalikan Buku
def kembalikan_buku():
    global current_member
    if "borrowed" not in current_member or not current_member["borrowed"]:
        print("Anda belum meminjam buku apapun.")
        return
    while True:
        borrowed_list = current_member["borrowed"]
        table = []
        for idx, isbn in enumerate(borrowed_list, start=1):
            book_info = next((b for b in books if b["ISBN"] == isbn), None)
            if book_info:
                table.append([idx, isbn, book_info["namaBuku"]])
        headers = ["No", "ISBN", "Nama Buku"]
        print("\nDaftar buku yang Anda pinjam:")
        print(tabulate(table, headers=headers, tablefmt="grid"))
        choice = input("Masukkan nomor buku untuk dikembalikan ('semua' untuk mengembalikan semua): ")
        if choice.lower() == "semua":
            confirm = input("Apakah Anda yakin ingin mengembalikan semua buku? (y/n): ")
            if confirm.lower() == "y":
                for isbn in borrowed_list:
                    for b in books:
                        if b["ISBN"] == isbn:
                            b["stokBuku"] += 1
                            break
                current_member["borrowed"] = []
                print("Semua buku telah dikembalikan.")
                break
        elif choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(borrowed_list):
                chosen_isbn = borrowed_list[idx - 1]
                book_info = next((b for b in books if b["ISBN"] == chosen_isbn), None)
                if book_info:
                    confirm = input(f"Apakah Anda yakin ingin mengembalikan buku '{book_info['namaBuku']}'? (y/n): ")
                    if confirm.lower() == "y":
                        book_info["stokBuku"] += 1
                        current_member["borrowed"].remove(chosen_isbn)
                        print(f"Buku '{book_info['namaBuku']}' telah dikembalikan.")
                if not current_member["borrowed"]:
                    print("Semua buku telah dikembalikan.")
                    break
            else:
                print("Nomor indeks tidak valid.")
        else:
            print("Input tidak valid.")

def display_selected_books(borrowed_books):
    borrowed_list = []
    total_cost = 0
    for book in borrowed_books.values():
        book_copy = book.copy()
        book_copy["SubTotal"] = book_copy["quantity"] * book_copy["harga"]
        total_cost += book_copy["SubTotal"]
        borrowed_list.append(book_copy)
    print("\nDaftar buku yang dipilih:")
    headers = ["No", "ISBN", "Nama Buku", "Kategori Buku", "Quantity", "Harga", "SubTotal"]
    table = []
    for idx, b in enumerate(borrowed_list, start=1):
        table.append([idx, b["ISBN"], b["namaBuku"], b["kategoriBuku"], b["quantity"], b["harga"], b["SubTotal"]])
    print(tabulate(table, headers=headers, tablefmt="grid"))
    print(f"Total biaya sewa: Rp {total_cost}")
    return total_cost

# Menu Pustakawan
def menu_pustakawan():
    attempts = 0
    while attempts < 3:
        admin_input = input("Masukkan username pustakawan: ")
        if admin_input == admin_username:
            print("Selamat datang, Pustakawan.")
            menu_pustakawan_logged_in()
            break
        else:
            attempts += 1
            print(f"Username admin tidak valid. Percobaan ke-{attempts}/3.")
    if attempts >= 3:
        print("Kesempatan habis. Kembali ke Menu Utama.")

def menu_pustakawan_logged_in():
    while True:
        print("\n--- Menu Pustakawan (Logged In) ---")
        print("1. Cek data buku")
        print("2. Menambah buku baru")
        print("3. Mengupdate data buku")
        print("4. Melihat data anggota perpustakaan")
        print("5. Melihat buku yang dipinjam")
        print("6. Logout")
        choice = input("Pilih opsi: ")
        if choice == "1":
            menu_rak_buku()
        elif choice == "2":
            tambah_buku()
        elif choice == "3":
            update_buku()
        elif choice == "4":
            tampilkan_data_anggota()
        elif choice == "5":
            tampilkan_buku_dipinjam()
        elif choice == "6":
            print("Anda telah berhasil logout.")
            break
        else:
            print("Pilihan tidak valid.")

def tambah_buku():
    print("\n--- Menambah Buku Baru ---")
    isbn = input("Masukkan ISBN: ")
    existing_book = find_book(isbn)

    if existing_book:
        print(f"Buku dengan ISBN {isbn} sudah ada:")
        display_books([existing_book])
        update_choice = input("Apakah Anda ingin mengupdate stok dan harga buku ini? (y/n): ").lower()
        if update_choice == "y":
            new_stok = input("Masukkan stok baru (kosongkan jika tidak ingin mengubah): ")
            new_harga = input("Masukkan harga baru (kosongkan jika tidak ingin mengubah): ")
            if new_stok and new_stok.isdigit():
                existing_book["stokBuku"] = int(new_stok)
            if new_harga and new_harga.isdigit():
                existing_book["harga"] = int(new_harga)
            print("Buku berhasil diupdate.")
            display_books([existing_book])
    else:
        namaBuku = input("Masukkan nama buku: ")
        while True:
            print("\nKategori yang tersedia:")
            for key, value in KATEGORI_BUKU.items():
                print(f"{key}. {value}")
            pilihkategori = input("Masukkan kategori buku: ")
            if pilihkategori in KATEGORI_BUKU:
                kategoriBuku = KATEGORI_BUKU[pilihkategori]
                break
            print("Kategori tidak valid.")

        stok = validate_numeric_input("Masukkan stok buku: ")
        harga = validate_numeric_input("Masukkan harga buku: ")

        new_book = {
            "ISBN": isbn,
            "namaBuku": namaBuku,
            "kategoriBuku": kategoriBuku,
            "stokBuku": stok,
            "harga": harga
        }
        books.append(new_book)
        print("Buku baru berhasil ditambahkan.")

def update_buku():
    print("\n--- Update Buku ---")
    isbn = input("Masukkan ISBN buku yang ingin diupdate: ")
    book = find_book(isbn)
    if not book:
        print("Buku dengan ISBN tersebut tidak ditemukan.")
        return

    print("Data buku saat ini:")
    display_books([book])
    new_stok = input("Masukkan stok baru (kosongkan jika tidak ingin mengubah): ")
    new_harga = input("Masukkan harga baru (kosongkan jika tidak ingin mengubah): ")

    if new_stok and new_stok.isdigit():
        book["stokBuku"] = int(new_stok)
    if new_harga and new_harga.isdigit():
        book["harga"] = int(new_harga)
    print("Buku berhasil diupdate.")

def tampilkan_data_anggota():
    if not members:
        print("Belum ada data anggota.")
        return

    headers = ["No", "Nama Lengkap", "Username", "Usia", "Jenis Kelamin"]
    table = [[i, m["fullname"], m["username"], m["usia"], m["jenis_kelamin"]]
             for i, m in enumerate(members, start=1)]
    print(tabulate(table, headers=headers, tablefmt="grid"))

def tampilkan_buku_dipinjam():
    borrowed_records = []
    for member in members:
        if member.get("borrowed"):
            for isbn in member["borrowed"]:
                book_info = find_book(isbn)
                if book_info:
                    borrowed_records.append([
                        len(borrowed_records) + 1,
                        isbn,
                        book_info["namaBuku"],
                        member["fullname"]
                    ])

    if borrowed_records:
        headers = ["No", "ISBN", "Nama Buku", "Nama Peminjam"]
        print(tabulate(borrowed_records, headers=headers, tablefmt="grid"))
    else:
        print("Tidak ada buku yang dipinjam.")

# Main program execution
if __name__ == "__main__":
    main_menu()