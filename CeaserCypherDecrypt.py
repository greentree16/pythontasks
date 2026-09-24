key = int(input("What number did you input as your key?"))
encryptedWord = input("Enter the encrypted word")
separateChars = list(encryptedWord)

unencryptedWord = []

for char in separateChars:
    encryptedAsciiCode = ord(char)
    unencryptedAsciiCode = encryptedAsciiCode - key
    if unencryptedAsciiCode < 97:
        difference = 97 - unencryptedAsciiCode
        newAsciiCode = 123 - difference
        unencryptedAsciiCode = newAsciiCode
    unencryptedChar = chr(unencryptedAsciiCode)
    unencryptedWord.append(unencryptedChar)

print("Your original word is", unencryptedWord)