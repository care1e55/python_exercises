import random

def create_password_generator(symbols: str):
    def func(num_symbols: int):
        result = []
        for _ in range(num_symbols):
            result.append(random.choice(symbols))
        return ''.join(result)
    return func

alpha_password = create_password_generator('abcdef')
symbol_password = create_password_generator('!@#$%')

print(alpha_password(5))
print(alpha_password(10))

print(symbol_password(5))
print(symbol_password(10))
