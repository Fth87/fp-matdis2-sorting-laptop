from fastapi import APIRouter, HTTPException, UploadFile, File, Query
from service.filtering_service import filter_laptops
from service.sorting_service import merge_sort
from service.scoring_service import calculate_score
import pandas as pd
import os
from controller.laptop_controller import get_filtered_and_sorted_laptops

router = APIRouter()

UPLOAD_FOLDER = "./uploaded_files"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/laptops/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".xlsx"):
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


@router.get("/laptops/filter")
def filter_laptops(
    min_price: float = Query(0, description="Harga minimum"),
    max_price: float = Query(float("inf"), description="Harga maksimum"),
):
    try:
        print(f"Filtering laptops with min_price={min_price}, max_price={max_price}")
        return get_filtered_and_sorted_laptops(min_price, max_price)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Kesalahan saat memproses data: {e}"
        )
