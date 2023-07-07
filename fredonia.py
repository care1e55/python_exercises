PROVINCES = ['harpo', 'chico', 'groucho', 'zeppo']

province_tax_rates = {
    'harpo': 0.5,
    'chico': 0.5,
    'groucho': 0.7,
    'zeppo': 0.4
}


class HourTooLowError(Exception):
    pass


class HourTooHighError(Exception):
    pass


def time_percentage(hour):
    return hour / 24.0


def calculate_tax(amount: int, province: str, purchase_time: int) -> int:
    if purchase_time < 0:
        raise HourTooLowError(f'Hour of {purchase_time} is < 0')
    if purchase_time >= 24:
        raise HourTooHighError(f'Hour of {purchase_time} is >= 24')
    return amount * province_tax_rates[province.lower()] * time_percentage(purchase_time)
