import tkinter as tk
from tkinter import filedialog, messagebox
import vobject
import re
import pygame

# Fungsi untuk memformat nomor telepon dengan tanda +
def format_phone_number(phone_number):
    phone_number = re.sub(r'[^0-9]', '', phone_number)  # Menghapus karakter selain angka
    if not phone_number.startswith('+'):
        phone_number = '+' + phone_number
    return phone_number

# Fungsi untuk mengonversi file TXT ke VCF
def txt_to_vcf(txt_file_path, user_name, output_vcf_name):
    # Menggunakan dialog untuk menanyakan lokasi dan nama file untuk disimpan
    vcf_file_path = filedialog.asksaveasfilename(defaultextension=".vcf", filetypes=[("VCF Files", "*.vcf")], title="Simpan file VCF sebagai", initialfile=output_vcf_name + '.vcf')

    if not vcf_file_path:
        raise ValueError("Lokasi penyimpanan tidak dipilih!")

    with open(txt_file_path, 'r') as file:
        content = file.readlines()

    vcf_cards = []
    
    # Proses setiap baris yang mewakili satu nomor telepon
    for idx, line in enumerate(content, start=1):
        line = line.strip()
        if line:  # Pastikan baris tidak kosong
            # Mengambil nama dengan nomor urut
            name = f"{user_name} {idx}"  # Menambahkan nomor urut pada nama
            phone = format_phone_number(line)  # Menambahkan tanda + pada nomor telepon

            # Debug: Menampilkan data yang akan diproses
            print(f"Processing contact {name}: Phone={phone}")

            # Membuat vCard
            vcard = vobject.vCard()
            vcard.add('fn').value = name
            vcard.add('tel').value = phone

            vcf_cards.append(vcard)

    # Menyimpan file VCF jika ada data yang berhasil diproses
    if vcf_cards:
        with open(vcf_file_path, 'w') as vcf_file:
            for card in vcf_cards:
                vcf_file.write(card.serialize())
        return vcf_file_path
    else:
        raise ValueError("Tidak ada nomor yang valid untuk dikonversi")

# Fungsi untuk split file VCF
def split_vcf(vcf_file_path, max_contacts_per_file):
    with open(vcf_file_path, 'r') as vcf_file:
        vcf_data = vcf_file.read().split("END:VCARD")
    
    split_files = []
    for i in range(0, len(vcf_data) - 1, max_contacts_per_file):
        split_data = "END:VCARD".join(vcf_data[i:i + max_contacts_per_file]) + "END:VCARD"
        new_vcf_path = f"{vcf_file_path.replace('.vcf', '')}_part_{i//max_contacts_per_file + 1}.vcf"
        with open(new_vcf_path, 'w') as split_file:
            split_file.write(split_data)
        split_files.append(new_vcf_path)
    
    return split_files

# Fungsi untuk mengubah nama pada file VCF
def change_name_in_vcf(vcf_file_path, old_name, new_name):
    with open(vcf_file_path, 'r') as vcf_file:
        vcf_data = vcf_file.read()

    vcf_data = vcf_data.replace(f"FN:{old_name}", f"FN:{new_name}")

    with open(vcf_file_path, 'w') as vcf_file:
        vcf_file.write(vcf_data)

    return vcf_file_path

# Fungsi untuk mengonversi VCF ke TXT (nomor telepon saja)
def vcf_to_txt(vcf_file_path):
    with open(vcf_file_path, 'r') as vcf_file:
        vcf_data = vcf_file.read().split("END:VCARD")

    numbers = []
    for card in vcf_data:
        if "TEL:" in card:
            lines = card.splitlines()
            for line in lines:
                if "TEL:" in line:
                    numbers.append(line.split(":")[1].strip())  

    txt_file_path = vcf_file_path.replace('.vcf', '.txt')
    with open(txt_file_path, 'w') as txt_file:
        for number in numbers:
            txt_file.write(f"{number}\n")
    
    return txt_file_path

# Fungsi untuk memutar lagu secara otomatis
def play_song():
    song_path = filedialog.askopenfilename(title="Pilih Lagu", filetypes=[("MP3 Files", "*.mp3")])
    
    if song_path:  # Jika file dipilih
        try:
            pygame.mixer.music.load(song_path)
            pygame.mixer.music.play(-1)  # Memutar lagu secara berulang
        except Exception as e:
            print(f"Terjadi kesalahan saat memutar lagu: {e}")
    else:
        print("Tidak ada file yang dipilih.")

# Fungsi untuk membuka dialog file dan mengonversi TXT ke VCF
def browse_file():
    txt_file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    
    if txt_file_path:
        # Meminta pengguna untuk memasukkan nama
        name = name_entry.get()
        output_vcf_name = output_vcf_name_entry.get()
        
        if not name:
            messagebox.showerror("Error", "Nama pengguna harus diisi!")
            return
        if not output_vcf_name:
            messagebox.showerror("Error", "Nama file VCF harus diisi!")
            return
        
        try:
            vcf_file_path = txt_to_vcf(txt_file_path, name, output_vcf_name)
            messagebox.showinfo("Sukses", f"File VCF berhasil dibuat: {vcf_file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Fungsi untuk memilih dan memproses split file VCF
def split_file():
    vcf_file_path = filedialog.askopenfilename(filetypes=[("VCF Files", "*.vcf")])
    if vcf_file_path:
        max_contacts = int(max_contacts_entry.get())
        try:
            split_files = split_vcf(vcf_file_path, max_contacts)
            messagebox.showinfo("Sukses", f"VCF berhasil dibagi menjadi {len(split_files)} file.")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Fungsi untuk mengubah nama dalam VCF
def change_name():
    vcf_file_path = filedialog.askopenfilename(filetypes=[("VCF Files", "*.vcf")])
    if vcf_file_path:
        old_name = old_name_entry.get()
        new_name = new_name_entry.get()
        try:
            changed_file = change_name_in_vcf(vcf_file_path, old_name, new_name)
            messagebox.showinfo("Sukses", f"Nama berhasil diubah di file: {changed_file}")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Fungsi untuk mengonversi VCF ke TXT
def convert_vcf_to_txt():
    vcf_file_path = filedialog.askopenfilename(filetypes=[("VCF Files", "*.vcf")])
    if vcf_file_path:
        try:
            txt_file_path = vcf_to_txt(vcf_file_path)
            messagebox.showinfo("Sukses", f"File TXT berhasil dibuat: {txt_file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {e}")

# Membuat aplikasi GUI
def create_gui():
    root = tk.Tk()
    root.title("CV @Xiaomei0031 - Tools Converter")

    # Memulai pygame mixer
    pygame.mixer.init()

    # Memutar lagu otomatis
    play_song()

    # Frame untuk mengonversi TXT ke VCF
    label1 = tk.Label(root, text="Pilih file TXT untuk dikonversi menjadi VCF", padx=10, pady=10)
    label1.pack()
    name_label = tk.Label(root, text="Masukkan Nama Kontak", padx=10, pady=10)
    name_label.pack()
    global name_entry
    name_entry = tk.Entry(root, width=30)
    name_entry.pack(pady=5)
    
    label_vcf_name = tk.Label(root, text="Masukkan Nama File VCF", padx=10, pady=10)
    label_vcf_name.pack()
    global output_vcf_name_entry
    output_vcf_name_entry = tk.Entry(root, width=30)
    output_vcf_name_entry.pack(pady=5)
    
    browse_button = tk.Button(root, text="Pilih File TXT", command=browse_file, padx=10, pady=10)
    browse_button.pack()

# Frame untuk split VCF
    label2 = tk.Label(root, text="Pilih file VCF untuk dibagi", padx=10, pady=10)
    label2.pack()
    max_contacts_label = tk.Label(root, text="Jumlah kontak per file", padx=10, pady=10)
    max_contacts_label.pack()
    global max_contacts_entry
    max_contacts_entry = tk.Entry(root, width=30)
    max_contacts_entry.pack(pady=5)
    split_button = tk.Button(root, text="Split VCF", command=split_file, padx=10, pady=10)
    split_button.pack()

    # Frame untuk mengubah nama dalam VCF
    label3 = tk.Label(root, text="Ubah Nama dalam VCF", padx=10, pady=10)
    label3.pack()
    old_name_label = tk.Label(root, text="Nama Lama", padx=10, pady=10)
    old_name_label.pack()
    global old_name_entry
    old_name_entry = tk.Entry(root, width=30)
    old_name_entry.pack(pady=5)
    new_name_label = tk.Label(root, text="Nama Baru", padx=10, pady=10)
    new_name_label.pack()
    global new_name_entry
    new_name_entry = tk.Entry(root, width=30)
    new_name_entry.pack(pady=5)
    change_name_button = tk.Button(root, text="Ubah Nama", command=change_name, padx=10, pady=10)
    change_name_button.pack()

    # Frame untuk mengonversi VCF ke TXT
    convert_button = tk.Button(root, text="Konversi VCF ke TXT", command=convert_vcf_to_txt, padx=10, pady=10)
    convert_button.pack()

    root.mainloop()

# Menjalankan aplikasi GUI
if name == 'main':
    create_gui()