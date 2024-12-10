import pandas as pd

FILE_PATH = './datalaptop.xlsx'

def load_data():
    try:
        return pd.read_excel(FILE_PATH)
    except FileNotFoundError:
        print("File tidak ditemukan.")
        return None
    except Exception as e:
        print(f"Error saat memuat data: {e}")
        return None
