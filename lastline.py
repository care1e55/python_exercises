
fakefile_path = "fakefile.txt"
accumulator = 0

def to_int(word):
    try:
        return int(word)
    except:
        return 0

with open(fakefile_path, 'r') as file:
    for line in file:
        current_line = line.strip()
        accumulator += sum(
            [to_int(word) for word in current_line.split()]
        )

print(f'The sum is {accumulator} and the last line is {current_line}')
