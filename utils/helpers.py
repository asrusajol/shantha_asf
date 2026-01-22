def clean_number(value):
    if value is None:
        return 0
    return float(value.replace(",", "").strip())