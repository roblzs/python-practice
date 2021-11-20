def calculate_seconds(d):
    seconds = d * 24 * 3600

    return f"{seconds} sekundes"

print(calculate_seconds(int(input("Ievadiet dienu skaitu: "))))