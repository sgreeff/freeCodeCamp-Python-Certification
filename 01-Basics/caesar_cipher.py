"""freecodecamp.org worshop - Build a Caesar Cipher """

#implement alphabet shifting logic using list slicing
alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = 5
shifted_alphabet = alphabet[shift:] + alphabet[0:shift]