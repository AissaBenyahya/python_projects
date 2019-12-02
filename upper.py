#!/usr/bin/python3
def _to_upper(phrase):
    test = {}
    i = 97; j = 65
    while i < 123 and j < 91:
        test[i] = j
        i = i + 1; j = j + 1

    for i in range(len(phrase)):
        for (key, value) in test.items():
            if phrase[i] == chr(key):
                phrase = phrase.replace(phrase[i], chr(value))
    print(phrase)


letter1 = input("write a letter: ")
_to_upper(letter1)
