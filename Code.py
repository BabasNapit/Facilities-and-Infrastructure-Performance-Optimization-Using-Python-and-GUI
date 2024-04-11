# 14S20001 - Sebastian Jeremia Napitupulu
# 14S20002 - Ando Samuel Sitinjak
# 14S20003 - Christiano Doni Simatupang

# modul python sqlite3 mengubah datetime ke dalam format string
from sqlite3 import Date
from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkcalendar import DateEntry

# Penerapan OOP


class Mahasiswa():
    # Construtor
    def __init__(self, nama, nim, prodi):  # atribut
        self.__nama = nama
        self.__nim = nim
        self.__prodi = prodi

    def getNama(self):  # metod untuk mengakses atribut
        return self.__nama

    def getNim(self):
        return self.__nim

    def getProdi(self):
        return self.__prodi

    # method untuk nampilin data-datanya
    def display(self):  # mengembalikan tipe data str
        str = "Nama\t: " + self.getNama()
        str += "\nNIM\t: " + self.getNim()  # angka diubah kedalam tipe data string
        # += nilai awal kosong, lalu di tambahkan dengan inputan
        str += "\nProdi\t: " + self.getProdi()
        return str

# Inheritance dari class Mahasiswa


class Customer(Mahasiswa):  # subclass
    def __init__(self, nama, nim, prodi, alat, waktu_in, waktu_out):  # atribut tambahan di subclass
        # memanggil super class agar menggabungkan atribut di Class dan subclass
        super().__init__(nama, nim, prodi)
        self.__alat = alat
        self.__waktu_in = str(waktu_in)
        self.__waktu_out = str(waktu_out)

    # Polymorphism yaitu overriding method display dari parent
    def display(self):
        str = super().display()  # memanggil super class jadi di gabung
        str += "\nAlat\t:"
        for a in self.__alat:  # alat yang di pinjam lebih dari 1 / looping
            str += "\n- " + a.get()  # menampilkan string alat dalam bentuk data
        str += "\nWaktu\t:"
        str += "\nIn\t: " + self.__waktu_in
        str += "\nOut\t: " + self.__waktu_out
        return str


# Penerapan GUI dengan tkinter
root = Tk()
root.title("SARANA DAN PRASARANA")
root.config(padx=10, pady=5)
title = Label(root, text="SARANA DAN PRASARANA", font="Helvetica 14 bold")
title.grid(row=0, column=0, columnspan=4, pady=15)

# Setting global
root.option_add("*Label.font", "Helvetica 11")
root.option_add("*Checkbutton.font", "Helvetica 10")
root.option_add("*Entry.font", "Helvetica 10")
root.option_add("*Button.font", "Helvetica 10")

# Komponen Label
label_nama = Label(root, text="Nama")
label_nim = Label(root, text="NIM")
label_prodi = Label(root, text="Prodi")
label_alat = Label(root, text="Alat")
label_waktu = Label(root, text="Waktu")

# Komponen form input
entry_nama = Entry(root)
entry_nim = Entry(root)
entry_prodi = Entry(root)
cal_in = DateEntry(root, font="Helvetiva 10")
cal_out = DateEntry(root, font="Helvetica 10")

# Masukin komponen label dan form input ke window utama
label_nama.grid(row=1, column=0, sticky=W, padx=10)
entry_nama.grid(row=1, column=1, columnspan=4,
                sticky=N+S+E+W, pady=10, ipady=3)
label_nim.grid(row=2, column=0, sticky=W, padx=10)
entry_nim.grid(row=2, column=1, columnspan=4, sticky=N+S+E+W, pady=10, ipady=3)
label_prodi.grid(row=3, column=0, sticky=W, padx=10)
entry_prodi.grid(row=3, column=1, columnspan=4,
                 sticky=N+S+E+W, pady=10, ipady=3)

# daftar alat
alat = ["Gitar", "Bass", "Drum", "Kajon", "Sexophone", "Dll"]
list_alat = []  # array kosong
for i in range(6):
    var = StringVar()  # mendefinisikan variabel string di dalam tkinter
    list_alat.append(var)  # menambahkan (append) ke array kosong

# Komponen checkbox
label_alat.grid(row=4, column=0, sticky=W, padx=10)
c0 = Checkbutton(
    root, text=alat[0], variable=list_alat[0], onvalue=alat[0], offvalue="off")
c0.grid(row=4, column=1, sticky="W")
c1 = Checkbutton(
    root, text=alat[1], variable=list_alat[1], onvalue=alat[1], offvalue="off")
c1.grid(row=4, column=2, sticky="W")
c2 = Checkbutton(
    root, text=alat[2], variable=list_alat[2], onvalue=alat[2], offvalue="off")
c2.grid(row=4, column=3, sticky="W")
c3 = Checkbutton(
    root, text=alat[3], variable=list_alat[3], onvalue=alat[3], offvalue="off")
c3.grid(row=5, column=1, sticky="W")
c4 = Checkbutton(
    root, text=alat[4], variable=list_alat[4], onvalue=alat[4], offvalue="off")
c4.grid(row=5, column=2, sticky="W")
c5 = Checkbutton(
    root, text=alat[5], variable=list_alat[5], onvalue=alat[5], offvalue="off")
c5.grid(row=5, column=3, sticky="W")

# Komponen waktu/calendar
label_waktu.grid(row=6, column=0, sticky=W, padx=10)
label_waktu_in = Label(root, text="IN:")
label_waktu_in.grid(row=6, column=1, sticky=W, pady=5)
cal_in.grid(row=7, column=1, sticky=N+S+E+W)
label_waktu_out = Label(root, text="OUT: ")
label_waktu_out.grid(row=6, column=2, sticky=W, padx=10, pady=5)
cal_out.grid(row=7, column=2, sticky=N+S+E+W, padx=10)

# Method untuk cek apakah ada alat yang dipilih


def cek_pilihan_alat():  # fungsi cek alat
    for alat in list_alat:
        if(alat.get() != "off"):
            return True  # jika ada yang dipilih dari array alat

    return False  # jika tidak ada alat yang di pilih array alat


# Method untuk save data yang diinput ke file


def save():
    nama = entry_nama.get()  # dipanggil dari komponen form input (get)
    nim = entry_nim.get()
    prodi = entry_prodi.get()
    waktu_in = cal_in.get_date()
    waktu_out = cal_out.get_date()
    # untuk menyimpan alat yang di pilih dalam bentuk string / berupa list dari line 97
    alat = [value for value in list_alat if value.get() != "off"]

    if (not nama):  # not berfungsi jika string kosong maka eror
        messagebox.showerror("Kesalahan", "Input data nama terlebih dahulu.")
        return
    elif (not nim):
        messagebox.showerror("Kesalahan", "Input data nim terlebih dahulu.")
        return
    elif (not prodi):
        messagebox.showerror("Kesalahan", "Input data prodi terlebih dahulu.")
        return
    elif (not waktu_in or not waktu_out):
        messagebox.showerror("Kesalahan", "Input data waktu terlebih dahulu.")
        return
    elif (not cek_pilihan_alat()):
        messagebox.showerror("Kesalahan", "Pilih minimal 1 alat.")
        return
    else:
        # jika sudah terisi maka else dan kembali ke subclass
        cust = Customer(nama, nim, prodi, alat, waktu_in, waktu_out)

    f = open("data.txt", "w")
    f.write(cust.display())
    f.close()

    messagebox.showinfo("Informasi", "Berhasil menyimpan data")

#  Method untuk reset semua form input


def reset_form():
    entry_nama.delete(0, END)  # END bagian dari library tkinter
    # END, Jika kita tidak menentukan nilai apa pun ke parameter "end", secara default itu dianggap sebagai karakter baris baru yaitu "\n".
    entry_nim.delete(0, END)
    entry_prodi.delete(0, END)
    c0.deselect()  # deselect berfungsi agar cek box yang sudah di cek kembali menjadi kosong
    c1.deselect()
    c2.deselect()
    c3.deselect()
    c4.deselect()
    c5.deselect()

#  Method untuk nampilin data ke box


def print_data():
    try:
        f = open("data.txt", "r")
        label_display.config(text=f.read())
        f.close()
    except:
        messagebox.showerror("Kesalahan", "Belum ada file yang tersimpan.")


# reset form dipanggil agar semua form masih kosong dan tidak ada checkbox yang terpilih
reset_form()

#  Frame button dan komponen tombol2
btn_frame = Frame(root)
btn_save = Button(btn_frame, text="Save", command=save,
                  pady=5, padx=5, background="lightgreen")
btn_reset = Button(btn_frame, text="Reset", command=reset_form,
                   pady=5, padx=5, background="#FF5555")
btn_print = Button(btn_frame, text="Print", command=print_data,
                   pady=5, padx=5, background="lightgrey")

btn_save.pack(padx=5, side=LEFT)
btn_reset.pack(padx=5, side=LEFT)
btn_print.pack(padx=5, side=LEFT)

btn_frame.grid(row=8, column=1, pady=20, sticky=W)

# Box tempat print
box = Frame(root, width=300, height=150, relief='raised',
            borderwidth=1, background="white")
box.grid(row=9, column=1, columnspan=4, sticky=W, pady=10)

# Isi box
label_display = Label(box, font="Helvetica 10", justify=LEFT)
label_display.pack()

root.mainloop()
