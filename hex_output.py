def hex_output(hex_input) -> int:
    decimal = 0
    for pos, value in enumerate(reversed(hex_input)):
        if value == "x":
            break
        decimal += int(value)*(16**pos)
    return decimal

def hex_output2(hex_input) -> int:
    decimal = 0
    for pos, value in enumerate(hex_input[:1:-1]):
        decimal += int(value)*(16**pos)
    return decimal

print(hex_output2(input()))
