import csv

def load_csv(file_path):
    data = []
    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            new_row = {}
            for key, value in row.items():
                # Try to convert to int
                try:
                    new_row[key] = int(value)
                    continue
                except ValueError:
                    pass
                # Try to convert to float
                try:
                    new_row[key] = float(value)
                    continue
                except ValueError:
                    pass
                # Keep as string
                new_row[key] = value
            data.append(new_row)
    return data