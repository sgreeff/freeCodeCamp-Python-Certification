"""freecodecamp.org worshop - Build a Caesar Cipher """

def caesar(text, shift, encrypt = True):
    if not isinstance(shift, int):
        #validation for shift to be an integer
        return 'Shift must be an integer value.'
    elif shift < 1 or shift > 25:
        #validation for shift to be postive or must be less than the 25 alphabet characters condition
        return 'Shift must be an integer between 1 and 25.'
    else:
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        if encrypt != True:
            #determine if the function should encrypt the text passed to it (default behavior, encrypt=True), or if it should decrypt an encrypted message.
            shift = - shift   

        #alphabet shifting logic using list slicing    
        shifted_alphabet = alphabet[shift:] + alphabet[0:shift]

        #character mapping using str.maketrans for optimised translation
        translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())

        #using the translate () funtion to return a copy of the original string 
        #where the characters have been replaced based on the translation table
        return text.translate(translation_table)

#encrypt and decrypt wrapper functions
def encrypt(text, shift):
    return caesar(text, shift)

def decrypt(text, shift):
    return caesar(text, shift, False)

#encrypt function call
print(encrypt('hello world',5)) #Output: mjqqt btwqi

#decrypt function call
encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'
decrypted_text = decrypt(encrypted_text, 13)
print(decrypted_text) #Output: Courage is found in unlikely places.

"""
A tiny "Teacher Note" on the Decrypt Logic
I noticed the logic for negative shifts: alphabet[shift:] + alphabet[0:shift]

When shift becomes -13 (for decryption), Python handles this beautifully. alphabet[-13:] 
grabs the last 13 letters, and alphabet[0:-13] grabs everything but the last 13. It is a 
very elegant way to reverse the cipher without needing extra if statements!
"""