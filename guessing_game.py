import random

def guessing_game() -> int:
    return random.randint(1,101)

if __name__ == "__main__":
    true_number = guessing_game()
    while True:
        prompt = int(input("Please enter your guess: "))
        if not prompt:
            print("You entered empty guess")
            continue
        if prompt == true_number:
            print("Just right")
            break
        elif prompt > true_number:
            print("Too high")
            continue
        elif prompt < true_number:
            print("Too low")
            continue
