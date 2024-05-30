# daftar deklarasi fungsi
def baca_data(filename):
    # fungsi digunakan untuk membaca file teks, kemudian merubah ke dalam tipe data terstrukur
    file = open(filename, "r")
    
    kamus = {}
    
    teks = file.readline().replace("\n","")# replace untuk menghapus newline 
    
    while teks != "":
       #perulangan untuk mengisi dict kamus
        list_kata = teks.split() 
        if 'id' in kamus:
            kamus['id'].append(list_kata[0])
        else:
            kamus['id'] = [list_kata[0]]
            
        if 'en' in kamus:
            kamus['en'].append(list_kata[1])
        else:
            kamus['en'] = [list_kata[1]]
            
        if 'su' in kamus:
            kamus['su'].append(list_kata[2])
        else:
            kamus['su'] = [list_kata[2]]

        if 'ja' in kamus:
            kamus['ja'].append(list_kata[3])
        else:
            kamus['ja'] = [list_kata[3]]
            
        teks = file.readline().replace("\n","")
    file.close()
    return kamus

def print_data(data):
   #fungsi untuk menampilkan dict bahasa indonesia, inggris, sunda, dan jawa
    for key in data:
        print(key, "=", data[key])

def id_to_en(kata):
    #fungsi untuk menerjemahkan kata indonesia menjadi bahasa inggris
    if kata in kamus['id']:
        index_kata = kamus['id'].index(kata)
        print("Angka", kata, "dalam bahasa Inggris adalah: ",kamus['en'][index_kata])

def id_to_su(kata):
    #fungsi untuk menerjemahkan kata indonesia menjadi sunda
    if kata in kamus['id']:
        index_kata = kamus['id'].index(kata)
        print("Angka", kata, "dalam bahasa Sunda adalah: ",kamus['su'][index_kata])

def id_to_ja(kata):
    #fungsi untuk menerjemahkan kata indonesia menjadi jawa
    if kata in kamus['id']:
        index_kata = kamus['id'].index(kata)
        print("Angka", kata, "dalam bahasa Jawa adalah: ",kamus['ja'][index_kata])

def su_to_ja(kata):
    #fungsi untuk menerjemahkan kata sunda menjadi jawa
    if kata in kamus['su']:
        index_kata = kamus['su'].index(kata)
        print("Angka", kata, "dalam bahasa Jawa adalah: ",kamus['ja'][index_kata])

# main program
# nama dari file teks
nama_file = "file.txt"
#menjalankan fungsi baca_data dengan parameter nama_file
kamus = baca_data(nama_file)
# menjalankan fungsi print_data  dengan parameter kamus
print_data(kamus)
# menjalankan fungsi id_to_en  dengan parameter "satu"
id_to_en("satu")
# menjalankan fungsi id_to_su  dengan parameter "dua"
id_to_su("dua")
# menjalankan fungsi id_to_ja  dengan parameter "tiga"
id_to_ja("tiga")
# menjalankan fungsi su_to_ja  dengan parameter "opat"
su_to_ja("opat")
