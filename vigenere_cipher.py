def vigenere_cipher():
    message = 'i am psychopath'
    key = 'student'
    direction = 1
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_message = ''
    key_index = 0 
    for char in message:
        if char == " ":
            encrypted_message += char
        else:
            key_char = key[key_index %len(key)]
            key_index += 1
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            encrypted_message += alphabet[new_index]
    print('Real_message: ', message)
    print('Encrypted_message: ', encrypted_message)

    return encrypted_message      

vigenere_cipher() 
