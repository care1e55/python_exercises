from pig_latin import vowels, translate_piglatin3

def pig_latin_sentence(sentence: str) -> str:
    """
    Translates sentence to Pig Latin

    Parameters:
    ----------
    sentence: str
        english sentence

    Returns
    ------
    pl_sentence: str
        translated sentence
    """
    
    result = []
    for word in sentence.split():
        result.append(translate_piglatin3(word))
    return " ".join(result)
    

if __name__ == '__main__':
    sentence = input()
    print(pig_latin_sentence(sentence))
