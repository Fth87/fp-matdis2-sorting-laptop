import pandas as pd
import os


def load_data():
    # Read the latest file in the uploaded_files directory
    uploaded_files = os.listdir("./uploaded_files")
    if not uploaded_files:
        raise ValueError("No files uploaded")

    latest_file = max(
        uploaded_files,
        key=lambda f: os.path.getctime(os.path.join("./uploaded_files", f)),
    )
    df = pd.read_excel(f"./uploaded_files/{latest_file}")
    return df
