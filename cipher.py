#This script is a Caesar Cipher based encode
from six.moves import input
def encrypt(string,s):
    result = ""
    for i in range(len(string)):
        char = string[i]
        #BIG LETTERS
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)
        else:
        #small letters
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result
while True:
    string = input("Input the string: ")
    s = 3
    print ("String Encoded: " + encrypt(string,s))
