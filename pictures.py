def pictures(input_str: str):
    input_list = input_str.split()
    print(f'Квадрат со стороной {len(input_list)}')
    for _ in range(len(input_list)):
        print(' '.join(input_list))
