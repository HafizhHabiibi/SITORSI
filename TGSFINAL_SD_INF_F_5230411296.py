from tabulate import tabulate

class Node:
    def __init__(self, no_sku, nama_barang, harga_satuan, jml_stok):
        self.no_sku = no_sku
        self.nama_barang = nama_barang
        self.harga_satuan = harga_satuan
        self.jml_stok = jml_stok
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, no_sku, nama_barang, harga_satuan, jml_stok):
        new_node = Node(no_sku, nama_barang, harga_satuan, jml_stok)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
            if new_node.no_sku == temp.no_sku:
                return False
            if new_node.no_sku < temp.no_sku:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, no_sku):
        temp = self.root
        while temp is not None:
            if no_sku < temp.no_sku:
                temp = temp.left
            elif no_sku > temp.no_sku:
                temp = temp.right
            else:
                return temp
        return None
    
    def dfs_in_order(self):
        results = []
        def transverse(current_node):
            if current_node is None:
                return
            if current_node.left is not None:
                transverse(current_node.left)
            results.append([current_node.no_sku, current_node.nama_barang, current_node.harga_satuan, current_node.jml_stok])
            if current_node.right is not None:
                transverse(current_node.right)
        transverse(self.root)
        return results
    
bst = BinarySearchTree()

def restok(no_sku, stok_baru):
    temp = bst.root
    while temp is not None:
        if no_sku < temp.no_sku:
            temp = temp.left
        elif no_sku > temp.no_sku:
            temp = temp.right
        else:
            total_stok = temp.jml_stok + stok_baru
            temp.jml_stok = total_stok
            print("\nRestok Pada NO.SKU Barang Yang Diinputkan Berhasil Dilakukan")
            return total_stok
    return False

transaksi = []
def transaksi_baru(no_sku, jumlah_beli, nama_konsumen):
    node = bst.contains(no_sku)
    if node is not None:
        if jumlah_beli <= node.jml_stok:
            total_stok = node.jml_stok - jumlah_beli
            node.jml_stok = total_stok
            subtotal = node.harga_satuan * jumlah_beli
            transaksi.append([nama_konsumen, no_sku, jumlah_beli, subtotal])
            print("\nData Transaksi Konsumen Berhasil Diinputkan")
            return True
        else:
            print("\nJumlah Stok Barang Di NO.SKU Yang Anda Masukan Tidak Mencukupi")
            return 'stok_tidak_cukup'
    else:
        print("\nNO.SKU Barang Yang Diinputkan Belum Terdaftar")
        return False

def merge_sort(array):
    if len(array) > 1:
        left_array = array[:len(array)//2]
        right_array = array[len(array)//2:]

        merge_sort(left_array)
        merge_sort(right_array)

        i = 0 #left_array index
        j = 0 #right_array index
        m = 0 #merge array index

        while i < len(left_array) and j < len(right_array):
            if left_array[i][3] > right_array[j][3]: 
                array[m] = left_array [i]
                i += 1
            else:
                array[m] = right_array[j]
                j += 1
            m += 1

        while i < len(left_array):
            array[m] = left_array[i]
            i += 1
            m += 1

        while j < len(right_array):
            array[m] = right_array[j]
            j += 1
            m += 1

def menu_utama():
    while True:
        try:
            print("\n" + "="*5 + "SISTEM INFORMASI STOK DAN TRANSAKSI [SITORSI]" + "="*5)
            print("1. Kelola Stok Barang")
            print("2. Kelola Transaksi Konsumen")
            print("0. Keluar")
            pilihan = int(input("Masukan Pilihan Menu : "))
            if pilihan == 1:
                while True:
                    try:
                        print("\n" + "="*5 + "Kelola Stok Barang" + "="*5)
                        print("1. Input Data Stok Barang")
                        print("2. Restok Barang")
                        print("3. Lihat Data Barang")
                        print("0. Kembali Ke Menu Utama")
                        sub_pilihan = int(input("Masukan Pilihan Menu : "))
                        if sub_pilihan == 1:
                            menu_input()
                        elif sub_pilihan == 2:
                            menu_restok()
                        elif sub_pilihan == 3:
                            lihat_data_barang()
                        elif sub_pilihan == 0:
                            break
                        else:
                            print("Pilihan Tidak Tersedia, Silahkan Coba Lagi.")
                    except ValueError:
                        print("\nMasukan Inputan Dengan Benar!")
                        continue

            elif pilihan == 2:
                while True:
                    try:
                        print("\n"+"="*5 + "Kelola Transaksi Konsumen" + "="*5)
                        print("1. Input Transaksi Baru")
                        print("2. Lihat Data Seluruh Transaksi Konsumen")
                        print("3. Lihat Data Transaksi Berdasarkan Subtotal")
                        print("0. Kembali Ke Menu Utama")
                        sub_pilihan = int(input("Masukan Pilihan Menu : "))
                        if sub_pilihan == 1:
                            menu_transaksi_baru()
                        elif sub_pilihan == 2:
                            print("\n" + "-"*5 + "Lihat Data Seluruh Transaksi Konsumen" + "-"*5)
                            lihat_seluruh_transaksi(transaksi)
                        elif sub_pilihan == 3:
                            print("\n" + "-"*5 + "Lihat Data Transaksi Berdasarkan Subtotal" + "-"*5)
                            lihat_seluruh_transaksi_subtotal()
                        elif sub_pilihan == 0:
                            break
                        else:
                            print("\nPilihan Tidak Tersedia, Silahkan Coba Lagi.")
                    except ValueError:
                        print("\nMasukan Inputan Dengan Benar!")
                        continue

            elif pilihan == 0:
                print("\n" + "="*5 + "Terimakasih Telah Menggunakan Layanan SITORSI" + "="*5)
                return

            else:
                print("\nPilihan Tidak Tersedia, Silahkan Coba Lagi.")
                
        except ValueError:
            print("\nMasukan Inputan Dengan Benar!")
            continue


def menu_input():
    print("\n" + "-"*5 + "Input Data Stok Barang" + "-"*5)
    while True:
        try:
            no_sku = input("Masukan NO.SKU Barang (Maksimal 4 Digit) : ")
            if len(no_sku) != 4:
                print("\nNO.SKU Harus 4 Digit!\n")
                continue
            no_sku = int(no_sku)
            if bst.contains(no_sku):
                print("\nNo.SKU Sudah Ada Silahkan Masukan NO.SKU Lainnya!\n")
                continue
            nama_barang = str(input("Masukan Nama Barang : "))
            if len(nama_barang) == 0:
                print("\nNama Barang Tidak Boleh Kosong!\n")
                continue
            harga_satuan = int(input("Masukan Harga Satuan Barang : "))
            jml_stok = int(input("Masukan Jumlah Stok Barang : "))
            bst.insert(no_sku, nama_barang, harga_satuan, jml_stok)
            print("\nBarang Pada NO.SKU Yang Diinputkan Berhasil Ditambahkan")
        except ValueError:
            print("\nMasukan Inputan Dengan Benar!")
            continue
        
        pilih = str(input("Apakah Ingin Memasukan Barang Lain (Y/N)? ")).lower()
        if pilih == "y":
            print()
            continue 
        else:
            return  

def menu_restok():
    print("\n" + "-"*5 + "Restok Barang" + "-"*5)
    while True:
        try:
            no_sku = input("Masukan NO.SKU Barang Yang Akan Di Restok : ")
            if len(no_sku) != 4:
                print("\nNO.SKU Harus 4 Digit!\n")
                continue
            no_sku = int(no_sku)
            node = bst.contains(no_sku)
            if node is not None:
                stok_baru = int(input("Masukan Stok Barang Tambahan : "))
                total_stok = restok(no_sku, stok_baru)
                nama_barang = node.nama_barang
                harga_satuan = node.harga_satuan
            else:
                while True:
                    pilih = input("NO.SKU Barang Belum Terdaftar, Ingin Menginputkan Barang (Y/N)? ").lower()
                    if pilih == "y":
                        menu_input()
                        break
                    else:
                        return
        except ValueError:
            print("\nMasukan Inputan Dengan Benar!")
            continue
        break
        
def menu_transaksi_baru():
    print("\n" + "-"*5 + "Input Transaksi Baru" + "-"*5)
    nama_konsumen = str(input("Masukan Nama Konsumen: "))
    while True:
        try:
            no_sku = (input("Masukan NO.SKU Barang: "))
            if len(no_sku) != 4:
                print("\nNO.SKU Harus 4 Digit!\n")
                continue
            no_sku = int(no_sku)
            node = bst.contains(no_sku)
            if node is None:
                print("\nNO.SKU Barang Yang Diinputkan Belum Terdaftar")
                pilih = str(input("Apakah Ingin Melanjutkan Transaksi (Y/N)? ")).lower()
                if pilih == "y":
                    print()
                    continue
                else:
                    return 
                
            while True:
                jumlah_beli = int(input("Masukan Jumlah Barang Yang Akan Dibeli: "))
                transaksi_proses = transaksi_baru(no_sku, jumlah_beli, nama_konsumen)
                if transaksi_proses == True:
                    pilih = str(input("Apakah Ingin Menambahkan Data Pembelian Untuk Konsumen Ini (Y/N)? ")).lower()
                    if pilih == "y":
                        print()
                        break
                    else:
                        return
                    
                elif transaksi_proses == 'stok_tidak_cukup':
                    pilih = str(input("Apakah Ingin Melanjutkan Transaksi (Y/N)? ")).lower()
                    if pilih == "y":
                        print()
                        continue
                    else:
                        return
        except ValueError:
            print("\nMasukan Inputan Dengan Benar!")
            continue
            
def lihat_data_barang():
    print("\n" + "-"*5 + "Lihat Data Barang" + "-"*5)
    dfs = bst.dfs_in_order()
    if dfs:
        dfs_str = [[str(item[0]).zfill(4), item[1], item[2], item[3]] for item in dfs]
        header = ["NO.SKU", "Nama Barang", "Harga", "Jumlah Stok"]
        print(tabulate(dfs_str, headers=header, tablefmt="fancy_outline"))
    else:
        print("\nData Barang Kosong")

def lihat_seluruh_transaksi(transaksi):
    if transaksi:
        transaksi_str = [[item[0], str(item[1]).zfill(4), item[2], item[3]] for item in transaksi]
        header = ["Nama Konsumen", "NO.SKU", "Jumlah Beli", "Subtotal"]
        print(tabulate(transaksi_str, headers=header, tablefmt="fancy_outline"))
    else:
        print("\nData Transaksi Konsumen Kosong")
        
def lihat_seluruh_transaksi_subtotal():
    transaksi_sort = transaksi[:] 
    merge_sort(transaksi_sort)
    lihat_seluruh_transaksi(transaksi_sort)

menu_utama()
