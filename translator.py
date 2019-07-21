def translate(phrase):
    translateWord = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translateWord += "g"
        else:
            translateWord += letter
    return translateWord

print(translate(input("Enter the phrase: ")))

