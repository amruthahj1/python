def seperate(text):
    words=text.split(",")
    for word in words:
        spwords=word.split("=")
        words[words.index(word)]=(spwords[0],spwords[1])
    return words
