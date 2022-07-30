letters = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....",
           "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-",
           "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."}


def morse_converter(test_word):
    morse_string = ""
    for letter in test_word:
        if letter in letters.keys():
            morse_letter = letters[letter]
            morse_string = morse_string + morse_letter + " "
        else:
            morse_string = morse_string + " / "

    print(morse_string)


morse_converter("abc def")
