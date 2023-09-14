morse_code_letters = {"A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
              "F": "..-.", "G": "--.", "H": "....", "I": "..", "K": "-.-",
              "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.",
              "Q": "--.-", "R": ".-.", "S": "...", "T": "-", "U": "..-",
              "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..",
              "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....",
              "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----", }

word_to_convert = input("Please enter a word to convert:")

converted_word = []

def convert_word(word):
    word = word.upper()
    for letter in word:
        if letter in morse_code_letters:
            converted_word.append(morse_code_letters[letter])

    print(" ".join(converted_word))

convert_word(word_to_convert)
