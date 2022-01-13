secret = input("Enter a secret: ")
shift_pattern = int(input("Enter a shift pattern: "))

def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result = result + chr((ord(char) + s - 65) % 26 + 65)
        else:
            result = result + chr((ord(char) + s - 97) % 26 + 97)
    return result

print("Caesar ciphered: " + encrypt(secret,shift_pattern))