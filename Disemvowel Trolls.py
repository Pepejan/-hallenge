def disemvowel(string_):
    letters = {'a', 'e', 'i', 'o', 'u'}

    text_list = list(string_)

    i = 0
    while i < len(text_list):
        if text_list[i].lower() in letters:
            text_list.pop(i)
        else:
            i += 1

    text = "".join(text_list)
    return text