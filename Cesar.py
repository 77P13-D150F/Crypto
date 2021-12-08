#!/usr/bin/env python3
"""
CESAR CIPHER
First historical cipher (substitution cipher) used by Julius Cesar.
Obtained by shifting all letters of plaintext by 3 positions on the right.
This algorithm let define the amplitude of the rotation.

Key space = 26

Usage:
to encrypt a plaintext with a numeric key: -e KEY "plaintext"
to decrypt through all possible letter rotations: -d "ciphertext"
"""


from sys import argv
import string
from collections import deque

az= [l for l in string.ascii_lowercase]
AZ= [L for L in string.ascii_uppercase]


def encrypt(rot, plaintext):
    shift= deque(az)                                                                    # Create a deque of the alphabet
    shift.rotate(rot)                                                                   # Shift the deque
    rotation_tab= plaintext.maketrans(string.ascii_lowercase, ''.join(shift))           # Bulid a translation table
    cipher= plaintext.translate(rotation_tab)                                           # Apply the alphabet shift
    SHIFT= deque(AZ)
    SHIFT.rotate(rot)
    rotation_tab= cipher.maketrans(string.ascii_uppercase, ''.join(SHIFT))
    print(cipher.translate(rotation_tab))

    
def decrypt(cipher):
    for rot in range(26):
        shift= deque(az)
        shift.rotate(rot)
        rotation_tab= cipher.maketrans(string.ascii_lowercase, ''.join(shift))
        cipher= cipher.translate(rotation_tab)
        
        SHIFT= deque(AZ)
        SHIFT.rotate(rot)
        rotation_tab= cipher.maketrans(string.ascii_uppercase, ''.join(SHIFT))
        print(rot, '\t', cipher.translate(rotation_tab))


def main():
    if argv[1] == '-e' and len(argv) > 2:
        text= ' '.join(argv[i] for i in range(2, len(argv)))                            # Merge multiple words with spaces into one string
        key= int(argv[2])
        encrypt(key, text)
    elif argv[1] == '-d':
        cipher= ' '.join(argv[i] for i in range(2, len(argv)))                          # Merge multiple words with spaces into one string
        decrypt(cipher)
    else:
        print('To encrypt a plaintext (example with rotation 13): Cesar.py -e 13 "plaintext and more plaintext"')
        print('To decrypt through all possible rotations: Cesar.py -d ciphertext')

main()
