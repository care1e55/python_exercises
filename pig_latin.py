vowels = "aeiou"

def translate_piglatin(english_word: str) -> str:
    if english_word[0] in vowels:
        english_word = english_word + "way"
    else:
        english_word = english_word[1:] + english_word[0] + 'ay'
    return english_word

def translate_piglatin2(english_word: str) -> str:
    if english_word[0] in vowels:
        return english_word + "way"
    return english_word[1:] + english_word[0] + 'ay'

def translate_piglatin3(english_word: str) -> str:
    if english_word[0] in vowels:
        return f'{english_word}way'
    return f'{english_word[1:]}{english_word[0]}ay'

if __name__=='__main__':
    example = input()
    print(translate_piglatin(example))
    print(translate_piglatin2(example))
    print(translate_piglatin3(example))
