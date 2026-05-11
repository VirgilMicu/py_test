def linear_search (vect, key):
    if not isinstance(key, int):
        return -1
    if not isinstance(vect, list):
        return -1
    if len(vect) != 5:
        return -1
    for i in range (0,5):
        if not isinstance(vect[i], int):
            return -1
    for i in range (0,5):
        if vect[i] == key:
            return i
    return -1
