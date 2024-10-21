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
            total_stock = temp.jml_stok + stok_baru
            temp.jml_stok = total_stock
            return total_stock
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
            print("Data Transaksi Konsumen Berhasil Diinputkan")
            return True
        else:
            print("Jumlah Stok NO.SKU yang Anda beli tidak mencukupi")
            return 'stok_tidak_cukup'
    else:
        print("NO.SKU Yang Diinputkan Belum Terdaftar")
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
            if left_array[i][3] > right_array[j][3]: #[3] merujuk indeks subtotal di append list transaksi_baru
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
    print("="*5 + "SITORSI" + "="*5)
    while True:
        print("1. Kelola Stok Barang")
        print("2. Kelola Transaksi Konsumen")
        print("0. Keluar")
        pilihan = int(input("Masukan Pilihan Menu : "))
        if pilihan == 1:
            while True:
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

        elif pilihan == 2:
            while True:
                print("1. Input Transaksi Baru")
                print("2. Lihat Data Seluruh Transaksi Konsumen")
                print("3. Lihat Data Transaksi Berdasarkan Subtotal")
                print("0. Kembali Ke Menu Utama")
                sub_pilihan = int(input("Masukan Pilihan Menu : "))
                if sub_pilihan == 1:
                    menu_transaksi_baru()
                elif sub_pilihan == 2:
                    lihat_seluruh_transaksi(transaksi)
                elif sub_pilihan == 3:
                    lihat_seluruh_transaksi_subtotal()
                elif sub_pilihan == 0:
                    break
                else:
                    print("Pilihan Tidak Tersedia, Silahkan Coba Lagi.")

        elif pilihan == 0:
            print("Terimakasih Telah Menggunakan Layanan SITORSI")
            return

        else:
            print("Pilihan Tidak Tersedia, Silahkan Coba Lagi.")

def menu_input():
    while True:
        try:
            no_sku = input("Masukan NO.SKU (maksimal 4 digit) : ")
            if len(no_sku) != 4:
                print("NO.SKU maksimal 4 digit")
                continue
            no_sku = int(no_sku)
            if bst.contains(no_sku):
                print("No SKU Sudah ada silahkan masukan NO.SKU lainya !")
                continue
            nama_barang = str(input("Masukan Nama Barang : "))
            if len(nama_barang) == 0:
                print("Nama Barang Tidak Boleh Kosong!")
                continue
            harga_satuan = int(input("Masukan Harga Satuan Barang : "))
            jml_stok = int(input("Masukan Jumlah Stok Barang : "))
            bst.insert(no_sku, nama_barang, harga_satuan, jml_stok)
        except ValueError:
            print("Masukan Inputan Dengan Benar!")
            continue

        while True:
            pilih = str(input("Apakah ingin memasukan produk lain (Y/N)? ")).lower()
            if pilih == "y":
                break
            elif pilih =="n" :
                return
            else:
                print("Pilihan Tidak Tersedia!")
                continue
            
def menu_restok():
    while True:
        try:
            no_sku = input("Masukan NO.SKU yang akan di restok : ")
            if len(no_sku) != 4:
                print("NO.SKU maksimal 4 digit")
                continue
            no_sku = int(no_sku)
            node = bst.contains(no_sku)
            if node is not None:
                stok_baru = int(input("Masukan Stok Tambahan : "))
                total_stok = restok(no_sku, stok_baru)
                nama_barang = node.nama_barang
                harga_satuan = node.harga_satuan
            else:
                while True:
                    pilih = input("NO. SKU belum terdaftar, ingin menginputkan produk (Y/N)? ").lower()
                    if pilih == "y":
                        menu_input()
                        break
                    elif pilih == "n":
                        return
                    else:
                        print("Pilihan Tidak Tersedia!")
                        continue
                    
        except ValueError:
            print("Masukan Inputan Dengan Benar!")
            continue
        break
        
def menu_transaksi_baru():
    nama_konsumen = str(input("Masukan nama konsumen: "))
    while True:
        try:
            no_sku = (input("Masukan NO.SKU Produk: "))
            if len(no_sku) != 4:
                print("NO.SKU maksimal 4 digit")
                continue
            no_sku = int(no_sku)
            node = bst.contains(no_sku)
            if node is None:
                print("NO.SKU Yang Diinputkan Belum Terdaftar")
                while True:
                    pilih = str(input("Apakah ingin melanjutkan transaksi (Y/N)? ")).lower()
                    if pilih == "y":
                        break
                    elif pilih == "n":
                        return
                    else:
                        print("Pilihan Tidak Tersedia!")
                        continue
                continue

            while True:
                jumlah_beli = int(input("Masukan jumlah produk yang akan dibeli: "))
                transaksi_proses = transaksi_baru(no_sku, jumlah_beli, nama_konsumen)
                if transaksi_proses == True:
                    keluar_loop = False
                    while True:
                        pilih = str(input("Apakah ingin menambahkan data pembelian untuk konsumen ini (Y/N)? ")).lower()
                        if pilih == "y":
                            keluar_loop = True
                            break
                        elif pilih == "n":
                            return
                        else:
                            print("Pilihan Tidak Tersedia!")
                            continue
                    if keluar_loop:
                        break
                
                elif transaksi_proses == 'stok_tidak_cukup':
                    while True:
                        pilih = str(input("Apakah ingin melanjutkan transaksi (Y/N)? ")).lower()
                        if pilih == "y":
                            break
                        elif pilih == "n":
                            return
                        else:
                            print("Pilihan Tidak Tersedia!")
                            continue
                            
        except ValueError:
            print("Masukan Inputan Dengan Benar! ")
            continue
            
def lihat_data_barang():
    try:
        dfs = bst.dfs_in_order()
        dfs_str = [[str(item[0]).zfill(4), item[1], item[2], item[3]] for item in dfs]
        header = ["NO.SKU", "Nama Barang", "Harga", "Jumlah Stok"]
        print(tabulate(dfs_str, headers=header, tablefmt="fancy_outline"))
    except ValueError:
        print("Data Kosong") 

def lihat_seluruh_transaksi(transaksi):
    if transaksi:
        transaksi_str = [[item[0], str(item[1]).zfill(4), item[2], item[3]] for item in transaksi]
        header = ["Nama Konsumen", "NO.SKU", "Jumlah Beli", "Subtotal"]
        print(tabulate(transaksi_str, headers=header, tablefmt="fancy_grid"))
    else:
        print("Data Transaksi Konsumen Kosong")
        
def lihat_seluruh_transaksi_subtotal():
    transaksi_sort = transaksi[:] #menyalin array transaksi
    merge_sort(transaksi_sort)
    lihat_seluruh_transaksi(transaksi_sort)

menu_utama()
