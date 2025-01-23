#палидром
def polidrom(word):
    return word.lower() ==word[::1].lower()
polidrom("adda")
