def caesar_cipher():
    message ='my name is psychopath'
    offset = 1
    direction = 2
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_message = ''

    for char in message:
        if char == ' ':
            encrypted_message += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)
            encrypted_message += alphabet[new_index]
    
    print('Real_message: ', message)
    print('Encrypted_message: ', encrypted_message)

caesar_cipher()  
