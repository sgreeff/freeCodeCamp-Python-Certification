"""freecodecamp.org worshop - Build a Caesar Cipher """

def caesar():
    #alphabet shifting logic using list slicing
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shift = 5
    shifted_alphabet = alphabet[shift:] + alphabet[0:shift]

    #character mapping using str.maketrans for optimised translation
    translation_table = str.maketrans(alphabet, shifted_alphabet)

    #text to encrypt
    text = "hello world"

    #using the translate () funtion to return a copy of the original string 
    #where the characters have been replaced based on the translation table
    encrypted_text = text.translate(translation_table)
    print(encrypted_text)