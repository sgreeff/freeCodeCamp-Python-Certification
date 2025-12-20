"""freecodecamp.org worshop - Build a Caesar Cipher """

def caesar(text, shift):
    if not isinstance(shift, int):
        #validation for shift to be an integer
        return 'Shift must be an integer value.'
    elif shift < 1:
        #validation for shift to be postive
        return 'Shift must be a positive integer.'
    else:
        #alphabet shifting logic using list slicing
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        shifted_alphabet = alphabet[shift:] + alphabet[0:shift]

        #character mapping using str.maketrans for optimised translation
        translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())

        #using the translate () funtion to return a copy of the original string 
        #where the characters have been replaced based on the translation table
        return text.translate(translation_table)

#caesar function call
print(caesar('hello world',5))