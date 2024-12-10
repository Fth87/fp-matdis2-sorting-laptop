def display_price_levels():
    print("Pilihan level harga:")
    for i in range(1, 10):
        if i < 9:
            print(f"{i}. Rp{(i-1)*2500000:,} - Rp{i*2500000:,}")
        else:
            print("9. Rp20,000,000 ke atas")

def get_user_choice():
    return input("Masukkan pilihan (1-9): ")
