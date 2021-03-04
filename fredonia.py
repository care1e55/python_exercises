
PROVINCES = ['harpo', 'chico', 'groucho', 'zeppo']

province_tax_rates = {
    'harpo': 0.5, 
    'chico': 0.5, 
    'groucho': 0.7, 
    'zeppo': 0.4
}

def time_percentage(hour):
    return hour / 24.0


def calculate_tax(amount: int, province: str, purchase_time: int) -> int:
    return amount * province_tax_rates[province.lower()] * time_percentage(purchase_time)
