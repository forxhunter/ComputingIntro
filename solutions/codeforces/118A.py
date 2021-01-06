'''
Trivial string task
Petya started to attend programming lessons. On the first lesson his task was to write a simple program. The program was supposed to do the following: in the given string, consisting if uppercase and lowercase Latin letters, it:

    deletes all the vowels,
    inserts a character "." before each consonant,
    replaces all uppercase consonants with corresponding lowercase ones.

Vowels are letters "A", "O", "Y", "E", "U", "I", and the rest are consonants.
input: a string
output: a string modified
'''
vowels = ["a", "o", "y", "e", "u", "i"]
string = input()


output = string.lower()
new_output = ''
for letter in output:
    if letter in vowels:
        continue
    new_output += '.' + letter
print(new_output)

