from model.data_loader import load_data
from view.user_input_view import display_price_levels, get_user_choice
from view.display_view import display_laptops
from service.scoring_service import calculate_score
from service.filtering_service import get_price_range, filter_laptops
from service.sorting_service import merge_sort

def main():
    df = load_data()
    if df is None:
        return

    display_price_levels()
    choice = get_user_choice()
    price_range = get_price_range(choice)
    if not price_range:
        print("Pilihan tidak valid. Silakan coba lagi.")
        return

    filtered = filter_laptops(df, price_range)
    if filtered.empty:
        display_laptops([], price_range)
        return

    filtered['Skor'] = filtered.apply(calculate_score, axis=1)
    laptops = filtered.to_dict('records')
    merge_sort(laptops, 0, len(laptops)-1)
    display_laptops(laptops, price_range)
