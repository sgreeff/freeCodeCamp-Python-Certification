"""freecodecamp.org worshop - Build a Caesar Cipher """

#implement alphabet shifting logic using list slicing
alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = 5
shifted_alphabet = alphabet[shift:] + alphabet[0:shift]
translation_table = str.maketrans(alphabet, shifted_alphabet)
print(translation_table)

"""
TEACHER NOTES:
The str.maketrans() method takes two strings of equal length and returns a 
translation table that maps each character of the first string with the corresponding 
character of the second string. Each character in the translation table is stored 
as a Unicode ordinal, a number that uniquely identifies the character.


Efficiency: str.maketrans() creates a dictionary of Unicode ordinals (the numbers like 97 for 'a'). 
This is a O(1) constant-time lookup, which is mathematically the most efficient way to handle translation.

Abstraction: It abstracts away the "how" of the search, allowing the programmer to focus on the "what" 
(the mapping of the alphabet).

Unicode Awareness: Because it uses ordinals, it handles the underlying way computers represent text, 
showing a deeper understanding of Computer Science foundations.
"""