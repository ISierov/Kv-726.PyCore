def filter_words(st):
    res = ""
    flag = False

    for letter in st:
        if flag and letter == " ":
            continue
        elif not flag and letter == " ":
            flag = True
        elif letter != " ":
            flag = False
        res += letter

    return res.strip().capitalize()
