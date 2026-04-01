def clean_data(grants):
    return [g for g in grants if g["funding"] > 0]