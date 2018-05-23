# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 16:38:38 2018

@author: T3
"""

import math
itext = input("Enter text: ")
iinstruction = input("Encrypt/Decrypt (e/d): ")
ikey = input("Key:")
inumlet = input("Number of letters in alphabet:")
inumlet = int(inumlet)

alphabet = []
for letter in range(97,123):
    alphabet.append(chr(letter)) #get the alphabet in an array
alphabet_enum = enumerate(alphabet)
#print(alphabet)

def caesar(text,instruction,key):
    text = text.lower()
    text_characters = list(text)
    text_numbers_first = []
    text_numbers_second = []
    text_numbers_third = []
    key = int(key)
    #enumerate the text
    for letter in text_characters:
        letter_number = ord(letter) - 96
        text_numbers_first.append(letter_number)
    for number in text_numbers_first:
        if instruction == 'e':
            number += key
            number = number%inumlet
        elif instruction == 'd':
            number -= key
            number = number%inumlet
        text_numbers_second.append(number)
    for number in text_numbers_second:
        number_letter = chr(number + 96)
        text_numbers_third.append(number_letter)
    text_characters_fourth = ''.join(text_numbers_third)
    return text_characters_fourth

print("\n")
output = caesar(itext,iinstruction,ikey)

print(output)