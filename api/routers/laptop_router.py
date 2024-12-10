from fastapi import APIRouter, HTTPException, UploadFile, File
from service.filtering_service import filter_laptops
from service.sorting_service import merge_sort
from service.scoring_service import calculate_score
import pandas as pd
import os

router = APIRouter()

UPLOAD_FOLDER = "./uploaded_files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.post("/laptops/upload")
async def upload_file(file: UploadFile = File(...)):
    """
    Endpoint untuk mengunggah file Excel dan membaca data laptop.
    """
    if not file.filename.endswith('.xlsx'):
        raise HTTPException(status_code=400, detail="File harus berformat .xlsx")
    
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    
    try:
        # Simpan file di server
        with open(file_path, "wb") as f:
            f.write(await file.read())
        
        # Baca file Excel
        df = pd.read_excel(file_path)
        return {"message": "File berhasil diunggah.", "columns": df.columns.tolist()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Gagal membaca file: {e}")

@router.post("/laptops/filter")
async def filter_uploaded_file(price_range: dict):
    """
    Endpoint untuk memfilter data dari file Excel yang diunggah.
    """
    try:
        # Ambil file terbaru
        files = os.listdir(UPLOAD_FOLDER)
        if not files:
            raise HTTPException(status_code=400, detail="Tidak ada file yang diunggah.")
        
        latest_file = max([os.path.join(UPLOAD_FOLDER, f) for f in files], key=os.path.getctime)
        
        # Baca data dari file terbaru
        df = pd.read_excel(latest_file)

        # Filter berdasarkan rentang harga
        min_price = price_range.get("min", 0)
        max_price = price_range.get("max", float("inf"))
        filtered = filter_laptops(df, (min_price, max_price))

        if filtered.empty:
            return []

        # Hitung skor dan urutkan
        filtered["Skor"] = filtered.apply(calculate_score, axis=1)
        laptops = filtered.to_dict(orient="records")
        merge_sort(laptops, 0, len(laptops) - 1)

        return laptops
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Kesalahan saat memproses file: {e}")
