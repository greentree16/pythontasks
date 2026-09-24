key = int(input("Enter a number between 1-25 to be the key."))
word = input("Enter the word which you want to encrypt.")
separateChars = list(word)
encryptedWord = []

for char in separateChars:
    asciiCode = ord(char)
    encryptedAsciiCode = asciiCode + key
    if encryptedAsciiCode > 122:
        difference = encryptedAsciiCode - 122
        encryptedAsciiCode = 96 + difference
    encryptedCharacter = chr(encryptedAsciiCode)
    encryptedWord.append(encryptedCharacter)

newWord = ''.join(encryptedWord)
print("The new word is",newWord)