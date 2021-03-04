from fredonia import calculate_tax

if __name__=="__main__":
    print(f"The taxes are {calculate_tax(500, 'Harpo', 12)}")
    print(f"The taxes are {calculate_tax(500, 'Harpo', -1)}")
    print(f"The taxes are {calculate_tax(500, 'Harpo', 111)}")
