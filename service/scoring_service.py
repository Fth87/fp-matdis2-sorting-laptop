def calculate_score(laptop):
    try:
        cpu_scores = {"i7": 3, "i9": 3, "Ryzen 7": 3, "i5": 2, "Ryzen 5": 2}
        ram = int(laptop["RAM"].replace("GB", "").strip())
        storage_scores = {"1TB": 3, "512GB": 2, "256GB": 1}

        score = 1
        for cpu in cpu_scores:
            if cpu in laptop["CPU"]:
                score = cpu_scores[cpu]
                break

        if ram >= 16:
            score += 3
        elif ram >= 8:
            score += 2
        else:
            score += 1

        for storage in storage_scores:
            if storage in laptop["Penyimpanan"]:
                score += storage_scores[storage]
                break
        return score
    except Exception as e:
        print(f"Error saat menghitung skor: {e}")
        return 0
