from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 15", "+79991112233"),
    Smartphone("Samsung", "Galaxy S24", "+79992223344"),
    Smartphone("Xiaomi", "Redmi Note 13", "+79993334455"),
    Smartphone("Google", "Pixel 8", "+79994445566"),
    Smartphone("Honor", "Magic 6", "+79995556677")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")
