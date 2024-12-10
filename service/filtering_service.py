def get_price_range(choice):
    ranges = {
        "1": (0, 2500000),
        "2": (2500000, 5000000),
        "3": (5000000, 7500000),
        "4": (7500000, 10000000),
        "5": (10000000, 12500000),
        "6": (12500000, 15000000),
        "7": (15000000, 17500000),
        "8": (17500000, 20000000),
        "9": (20000000, float('inf'))
    }
    return ranges.get(choice, None)

def filter_laptops(df, price_range):
    return df[(df['Harga'] >= price_range[0]) & (df['Harga'] < price_range[1])].copy()
