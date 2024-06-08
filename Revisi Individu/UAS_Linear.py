from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


class SortingProduct:
    def __init__(self, name, image_path, price):
        self.name = name
        self.image_path = image_path
        self.price = price

class PriceSort(tk.Tk):
    def __init__(self, products):
        super().__init__()
        self.title("Price Counting Sort")  # Judul aplikasi
        self.geometry("1280x832")  # Ukuran gui aplikasi
        self.products = products  # Daftar produk yang ada di bawah

        # Membuat canvas dengan scrollbar
        self.canvas = tk.Canvas(self, borderwidth=0, background="#F1EBC9")  # Membuat objek canvas
        self.product_frame = tk.Frame(self.canvas, background="#F1EBC9")  # Membuat frame untuk produk
        self.scrollbar = tk.Scrollbar(self, orient="vertical", command=self.canvas.yview)  # Membuat scrollbar vertikal

        self.canvas.configure(yscrollcommand=self.scrollbar.set)  # Mengkonfigurasi scrollbar canvas
        self.scrollbar.pack(side="right", fill="y")  # Menampilkan scrollbar di sisi kanan
        self.canvas.pack(side="left", fill="both", expand=True)  # Menampilkan canvas di sisi kiri dengan mengisi seluruh ruang yang tersedia
        self.canvas.create_window((4, 4), window=self.product_frame, anchor="nw")  # Menambahkan frame produk ke dalam canvas

        self.product_frame.bind("<Configure>", self.on_frame_configure)  # Mengikat tindakan saat ukuran frame berubah
        self.canvas.bind("<Configure>", self.on_canvas_configure)  # Mengikat tindakan saat ukuran canvas berubah

        # Menambahkan produk ke dalam frame
        self.products = products
        self.add_products()

        # Tombol untuk mengurutkan produk berdasarkan harga
        self.sort_button1 = tk.Button(self, text="High To Low", command=self.sort_high_to_low)  # Tombol untuk mengurutkan dari harga tertinggi ke terendah
        self.sort_button2 = tk.Button(self, text="Low To High", command=self.sort_low_to_high)  # Tombol untuk mengurutkan dari harga terendah ke tertinggi
        self.sort_button1.pack(side="left")  # Menampilkan tombol "High To Low" di sebelah kiri
        self.sort_button2.pack(side="right")  # Menampilkan tombol "Low To High" di sebelah kanan


    def add_products(self):
        num_columns = 5  #jumlah kolom
        col = 0
        row = 0

        for product in self.products:
            # memuat gambar produk
            image = Image.open(product.image_path)
            image = image.resize((100, 100), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)

            # membuat label produk
            product_label = tk.Label(
                self.product_frame,
                text=product.name,
                image=photo,
                compound="top",
                font=("Helvetica", 9),
                bg="#ffffff",
                fg="black",
            )
            product_label.photo = photo
            product_label.grid(row=row, column=col, padx=10, pady=10)

            # membuat label 
            price_label = tk.Label(
                self.product_frame,
                text=f"Price: {product.price}",
                font=("Helvetica", 10),
                bg="#ffffff",
                fg="black",
            )
            price_label.grid(row=row + 1, column=col, padx=10, pady=5)

            # mengikat tindakan klik pada label produk
            product_label.bind("<Button-1>", lambda event, p=product: self.on_product_click(p))

            col += 1
            if col >= num_columns:
                col = 0
                row += 2

    def on_frame_configure(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def on_canvas_configure(self, event):
        self.canvas.itemconfigure(self.product_frame, width=event.width)
    #visualisasi sirt descending
    def sort_high_to_low(self):
        self.counting_sort(reverse=True)
        self.product_frame.destroy()
        self.product_frame = tk.Frame(self.canvas, background="#ffffff")
        self.canvas.create_window((4, 4), window=self.product_frame, anchor="nw")
        self.add_products()
    #visualisasi sort ascending
    def sort_low_to_high(self):
        self.counting_sort(reverse=False)
        self.product_frame.destroy()
        self.product_frame = tk.Frame(self.canvas, background="#ffffff")
        self.canvas.create_window((4, 4), window=self.product_frame, anchor="nw")
        self.add_products()

    def counting_sort(self, reverse):
        # Step 1: Menghitung nilai maksimum dan minimum dari harga produk
        max_price = max(self.products, key=lambda p: p.price).price
        min_price = min(self.products, key=lambda p: p.price).price

        # Step 2: Menghitung rentang harga
        price_range = max_price - min_price + 1

        # Step 3: Membuat array count untuk menghitung frekuensi kemunculan setiap harga produk
        count = [0] * price_range

        for product in self.products:
            count[product.price - min_price] += 1

        # Step 4: Jika reverse=True, pengurutan dilakukan dari harga tertinggi ke terendah
        if reverse:
            sorted_products = []
            for i in range(price_range - 1, -1, -1):
                while count[i] > 0:
                    # Step 5a: Mencari harga produk yang sesuai dengan i + min_price
                    price = i + min_price
                    for product in self.products:
                        if product.price == price:
                            # Step 5b: Menambahkan produk ke dalam sorted_products dan mengurangi count[i] sebanyak 1
                            sorted_products.append(product)
                            count[i] -= 1
                            break  # Melanjutkan ke iterasi selanjutnya setelah menemukan produk yang sesuai

        # Step 6: Jika reverse=False, pengurutan dilakukan dari harga terendah ke tertinggi
        else:
            sorted_products = []
            for i in range(price_range):
                while count[i] > 0:
                    # Step 7a: Mencari harga produk yang sesuai dengan i + min_price
                    price = i + min_price
                    for product in self.products:
                        if product.price == price:
                            # Step 7b: Menambahkan produk ke dalam sorted_products dan mengurangi count[i] sebanyak 1
                            sorted_products.append(product)
                            count[i] -= 1
                            break  # Melanjutkan ke iterasi selanjutnya setelah menemukan produk yang sesuai

        # Step 8: Mengganti self.products dengan sorted_products setelah pengurutan selesai
        self.products = sorted_products




products =  [
        SortingProduct('Mi 37W Dual-Port Car Charger', 'Mi 37W Dual-Port Car Charger.png', 109000),
        SortingProduct('Mi 360 Camera (1080p)', 'Mi 360Camera (1080p).png', 449000),
        SortingProduct('Mi Curved Gaming Monitior 34', 'Mi Curved Gaming Monitor 34_.png', 5599000),
        SortingProduct('Mi Desktop Monitor 27”', 'Mi Desktop Monitor 27.png', 1699000),
        SortingProduct('Mi LCD Writing Tablet 13.5"', 'Mi LCD Writing Tablet 13.5&quot.png', 2699000),
        SortingProduct('Mi Robot Vacuum-Mop 2 Lite', 'Mi Robot Vacuum-Mop 2 Lite.png', 2799000),
        SortingProduct('Mi Router 4C', 'Mi Router 4C.png', 199000),
        SortingProduct('Mi Smart Air Fryer (3.5L)', 'Mi Smart Air Fryer (3.5L).png', 1199000),
        SortingProduct('Mi TV 4 43', 'Mi TV 4 43.png', 3599000),
        SortingProduct('Mi TV 4 55', 'Mi TV 4 55.png', 5999000),
        SortingProduct('Mi TV Stick', 'Mi TV Stick.png', 599000),
        SortingProduct('Mi Vacuum Cleaner Light', 'Mi Vacuum Cleaner Light.png', 1499000),
        SortingProduct('Mi Vacuum Cleaner Mini.jpg', 'Mi Vacuum Cleaner Mini.jpg.png', 649000),
        SortingProduct('Mi Watch Charging Dock', 'Mi Watch Charging Dock.png', 69000),
        SortingProduct('Mi WiFi Range Extender AC1200', 'Mi WiFi Range Extender AC1200.png', 249000),
        SortingProduct('Mi Wireless Switch', 'Mi Wireless Switch.png', 99000),
        SortingProduct('POCO F4 GT', 'POCO F4 GT.png', 7999000),
        SortingProduct('POCO F4', 'POCO F4.png', 5199000),
        SortingProduct('poco M4 pro', 'poco M4 pro.png', 3399000),
        SortingProduct('POCO M5', 'POCO M5.png', 2299000),
        SortingProduct('POCO M5s', 'POCO M5s.png', 2599000),
        SortingProduct('POCO X5 5G', 'POCO X5 5G.png', 3499000),
        SortingProduct('Redmi 10 2022', 'Redmi 10 2022.png', 2299000),
        SortingProduct('Redmi Buds 3 Pro', 'Redmi Buds 3 Pro.png', 699000),
        SortingProduct('Redmi buds 4 Pro', 'Redmi buds 4 Pro.png', 949000),
        SortingProduct('Redmi buds 4', 'Redmi buds 4.png', 549000),
        SortingProduct('Redmi Note 11 Pro 5G', 'Redmi Note 11 Pro 5G.png', 4099000),
        SortingProduct('Redmi Note 11 Pro', 'Redmi Note 11 Pro.png', 3699000),
        SortingProduct('Redmi Note 11', 'Redmi Note 11.png', 2699000),
        SortingProduct('Redmi Note 12 Pro 5G', 'Redmi Note 12 Pro 5G.png', 4599000),
        SortingProduct('Redmi Note 12', 'Redmi Note 12.png', 2999000),
        SortingProduct('Redmi Pad', 'Redmi Pad.png', 3499000),
        SortingProduct('Redmi Watch 3', 'Redmi Watch 3.png', 1199000),
        SortingProduct('RedmiBook 15', 'RedmiBook 15.png', 7499000),
        SortingProduct('Xiaomi 6A Type-A to Type-C Cable', 'Xiaomi 6A Type-A to Type-C Cable.png', 79000),
        SortingProduct('xiaomi 10t Pro', 'xiaomi 10t.png', 6999000),
        SortingProduct('xiaomi 11 T pro', 'xiaomi 11 T pro.png', 6199000),
        SortingProduct('xiaomi 11 T', 'xiaomi 11 T.png', 4999000),
        SortingProduct('Xiaomi 22.5W Power Bank 10000mAh', 'Xiaomi 22.5W Power Bank 10000mAh.png', 4599000),
        SortingProduct('Xiaomi 67W Charging Combo (Type-A) EU', 'Xiaomi 67W Charging Combo (Type-A) EU.png', 299000),
        SortingProduct('Xiaomi Air Purifier 4 Pro', 'Xiaomi Air Purifier 4 Pro.png', 3499000),
        SortingProduct('Xiaomi Portable Electronic Air Compressor 1S', 'Xiaomi Portable Electronic Air Compressor 1S.png', 549000),
        SortingProduct('Xiaomi Robot Vacuum E10', 'Xiaomi Robot Vacuum E10.png', 2499000),
        SortingProduct('Xiaomi Smart Air Purifier 4 Lite', 'Xiaomi Smart Air Purifier 4 Lite.png', 1799000),
        SortingProduct('Xiaomi smart band 7', 'Xiaomi smart band 7.png', 699000),
        SortingProduct('Xiaomi Smart Camera C300', 'Xiaomi Smart Camera C300.png', 599000),
        SortingProduct('Xiaomi TV Stick 4K', 'Xiaomi TV Stick 4K.png', 699000),
        SortingProduct('Xiaomi Watch S1 Active', 'Xiaomi Watch S1 Active.png', 1999000),
        SortingProduct('Xiaomi12', 'Xiaomi12.png', 6999000),
        SortingProduct('xiaomi12lite5G', 'xiaomi12lite5G.png', 4799000),
        SortingProduct('xiaomi12pro', 'xiaomi12pro.png', 12199000),
        SortingProduct('Mi 360 Home Security Camera 2K', 'Mi 360 Home Security Camera 2K.png', 599000),
        SortingProduct('XIAOMI TV A2 55_', 'XIAOMI TV A2 55.jpg', 5899000),
        SortingProduct('XIAOMI TV P1E 65_', 'XIAOMI TV P1E 65.jpg', 9399000),]


# Create the app
app = PriceSort(products)
app.mainloop()

