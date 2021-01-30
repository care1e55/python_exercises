vowels = 'aeiou'
prefix = 'ub'

def ubbi_dubbi(word: str) -> str:
    '''
    Transaltes wordf to Ubbi-Dubbi

    Parameters:
    ----------
    word: str
        word for translation

    Returns
    -------
    str
        result translation

    Examples
    --------
    >>> ubbi_dubbi("octopus")

    uboctubopubus
    
    '''
    result = []
    for letter in word:
        if letter in vowels:
            result.append(prefix)
        result.append(letter)
    return "".join(result)

if __name__ == '__main__':
    word = input()
    print(ubbi_dubbi(word))