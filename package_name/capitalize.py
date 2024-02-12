def capitalize(text):
    """capitalize text
    >>> capitalize('hexlet')
    'Hexlet'
    """
    if text == '':
        return ''
    first_char = text[0].upper()
    rest_substring = text[1:]
    return f'{first_char}{rest_substring}'

if __name__ == "__main__":
    import doctest
    doctest.testmod()
