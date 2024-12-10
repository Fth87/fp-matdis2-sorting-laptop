def display_laptops(laptops, price_range):
    if laptops:
        print(
            f"\nLaptop dalam kategori harga Rp{price_range[0]:,} - Rp{price_range[1]:,}:"
        )
        for laptop in laptops:
            print(
                f"Nama: {laptop['Merek']} {laptop['Model']}, Harga: Rp{laptop['Harga']:,}, "
                f"CPU: {laptop['CPU']}, RAM: {laptop['RAM']}, Penyimpanan: {laptop['Penyimpanan']}"
            )
    else:
        print("Tidak ada laptop dalam kategori ini.")
