# Name: Jamar Hill
# Date: 11/17/20
# Description Assignment 8.a

"""Counts letters in string"""
def count_letters(string):
    let = dict()
    if string == "":#Returns count of empthy string
        return let
    for letter in string:
        if ord("a")<=ord(letter)<=ord("z") or ord("A")<=ord(letter)<=ord("Z"):
            if ord("a")<=ord(letter)<=ord("z"):
                letter = chr(ord(letter)-32)
            if letter not in let:
                let[letter] = 0
            let[letter] += 1
    return let

print(count_letters("AaBb"))