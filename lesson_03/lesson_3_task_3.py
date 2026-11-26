from address import Address
from mailing import Mailing

to_addr = Address("101000", "Москва", "Тверская", "12", "34")
from_addr = Address("190000", "Санкт-Петербург", "Невский проспект", "45", "6")

mailing = Mailing(to_addr, from_addr, 500, "TRACK123456789")

print(
    f"Отправление {mailing.track} из {mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} "
    f"в {mailing.to_address.index}, {mailing.to_address.city}, {mailing.to_address.street}, "
    f"{mailing.to_address.house} -{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)
