#Ceaser cipher1
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def encrypt(t, s):
    code = ""
    for letter in t:
        position = alphabet.index(letter)
        new_position = position + s
        if (new_position > 25):
            new = new_position - 25
            code += alphabet[new - 1]
        else:
            code += alphabet[new_position]
    print(f"encoded text is {code}")


def decrypt(t, s):
    de_cipher = ""
    for letter in t:
        position = alphabet.index(letter)
        new_position = position - s
        de_cipher += alphabet[new_position]
    print("The decoded text is " + de_cipher)

    
if (direction == 'encode'):
    encrypt(t=text, s=shift)
elif (direction == 'decode'):
    decrypt(t=text, s=shift)
else:
    print("!!!Invalid input!!!")
