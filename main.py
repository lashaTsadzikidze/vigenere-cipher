import string

# letter_to_index_lower = dict(zip(string.ascii_lowercase, range(26)))
# letter_to_index_upper = dict(zip(string.ascii_uppercase, range(26)))

# index_to_letter_lower = dict(zip(range(26), string.ascii_lowercase))
# index_to_letter_upper = dict(zip(range(26), string.ascii_uppercase))

def repeat_key(message, key):
    key_repeat = ''
    key_index = 0
    for char in message:
        if char in string.ascii_uppercase:
            key_repeat += key[key_index % len(key)].upper()
            key_index += 1
        elif char in string.ascii_lowercase:
            key_repeat += key[key_index % len(key)].lower()
            key_index += 1
        else:
            key_repeat += char
    
    return key_repeat

def encrypt(message, key):

    key_repeat = repeat_key(message, key)
    encrypted_message = ''

    for i in range(len(message)):
        if message[i] in string.ascii_uppercase:
            old_char_pos = ord(message[i]) - ord('A')
            key_char_pos = ord(key_repeat[i]) - ord('A')
            new_pos = (old_char_pos + key_char_pos) % 26
            encrypted_message += chr(new_pos + ord('A'))
        elif message[i] in string.ascii_lowercase:
            old_char_pos = ord(message[i]) - ord('a')
            key_char_pos = ord(key_repeat[i]) - ord('a')
            new_pos = (old_char_pos + key_char_pos) % 26
            encrypted_message += chr(new_pos + ord('a'))
        else:
            encrypted_message += message[i]
    
    return encrypted_message