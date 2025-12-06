# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
# text = input("Type your message:\n").lower()
# # shift = int(input("Type the shift number:\n"))

# fruits = ["apple", "pear", "orange"]


def encrypt(original_text, shift_number):
    new_word = []

    for char in original_text:
        if char.isalpha():
            new_char = ord(char) + shift_number

            if new_char > 122: 
                new_char -= 26
            
            new_word.append(chr(new_char))
        else: 
            new_word.append(char)

    return ''.join(new_word)

def decrypt(original_text, shift_number):

    new_word = []

    for char in original_text:
        if char.isalpha():
            new_char = ord(char) - shift_number

            if new_char < 97: 
                new_char += 26
            
            new_word.append(chr(new_char))
        else: 
            new_word.append(char)

    return ''.join(new_word)

# encrypted = []
# for word in fruits:
#     encrypted.append(encrypt(word, 9))

# for word in encrypted:
#     print(decrypt(word, 9))

while True:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        print(f'Here\'s the encoded result: {encrypt(text, shift)}')
    elif direction == "decode":
        print(f'Here\'s the decoded result: {decrypt(text, shift)}')
    else: 
        print(f"Unknown command. Please try again")
        continue
    
    decision = input("Type 'yes' if you want to go again. Otherwise type no").lower()

    if decision == "no":
        break