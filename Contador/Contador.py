def count_words(palabra):
    result = {}
    for word in palabra.split(' '):
        lower_word = word.lower()
        if lower_word in result:
            result[lower_word] += 1
        else:
            result[lower_word] = 1
    return result


