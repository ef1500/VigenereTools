import argparse

def find_vigenere_key(alpha1, alpha2, plaintext, ciphertext):
    """Find the vigenere key for the text given the plaintext, ciphertext
    and two alphabets."""
    # Check that the alphabets are the same size
    if len(alpha1) != len(alpha2):
        raise ValueError("Alphabets must be the same size")
    n = len(alpha1)
    
    # Check that the plaintext and ciphertext are the same length
    if len(plaintext) != len(ciphertext):
        raise ValueError("Plaintext and ciphertext must be the same length")
    
    # Initialize the key to an empty string
    key = ""
    
    # Iterate through the plaintext and ciphertext, finding the key for each character
    for i in range(len(plaintext)):
        # Find the index of the plaintext character in alpha1
        p = alpha1.index(plaintext[i])
        # Find the index of the ciphertext character in alpha2
        c = alpha2.index(ciphertext[i])
        # The key for this character is the character in alpha1 at the index (c - p) % n
        key += alpha1[(c - p) % n]
    
    return key

def encode_vigenere(alpha1, alpha2, plaintext, key):
    """Encode Data Using the vigenere cipher"""
    # Check that the alphabets are the same size
    if len(alpha1) != len(alpha2):
        raise ValueError("Alphabets must be the same size")
    n = len(alpha1)
    
    # Check that the key is the same length as the plaintext
    if len(plaintext) != len(key):
        raise ValueError("Key must be the same length as the plaintext")
    
    # Initialize the ciphertext to an empty string
    ciphertext = ""
    
    # Iterate through the plaintext and key, encoding each character
    for i in range(len(plaintext)):
        # Find the index of the plaintext character in alpha1
        p = alpha1.index(plaintext[i])
        # Find the index of the key character in alpha2
        k = alpha2.index(key[i])
        # The ciphertext character is the character in alpha2 at the index (p + k) % n
        ciphertext += alpha2[(p + k) % n]
    
    return ciphertext

def decode_vigenere(alpha1, alpha2, plaintext, key):
    """Decode data with the Vigenere chipher"""
    # Check that the alphabets are the same size
    if len(alpha1) != len(alpha2):
        raise ValueError("Alphabets must be the same size")
    n = len(alpha1)
    
    # Check that the plaintext and key are the same length
    if len(plaintext) != len(key):
        raise ValueError("Plaintext and key must be the same length")
    
    # Initialize the decoded text to an empty string
    decoded = ""
    
    # Iterate through the plaintext and key, decoding each character
    for i in range(len(plaintext)):
        # Find the index of the plaintext character in alpha1
        p = alpha1.index(plaintext[i])
        # Find the index of the key character in alpha1
        k = alpha1.index(key[i])
        # The decoded character is the character in alpha2 at the index (p - k) % n
        decoded += alpha2[(p - k) % n]
    
    return decoded

parser = argparse.ArgumentParser(description="Perform Vigenère cipher operations")
parser.add_argument("operation", choices=["encode", "decode", "reversekey"], help="The operation to perform (encode, decode, or reversekey)")
parser.add_argument("--alphabet", "-a", required=True, help="The alphabet to use")
parser.add_argument("--key", "-k", help="The key for the cipher")
parser.add_argument("--plaintext", "-p", help="The plaintext")
parser.add_argument("--ciphertext", "-c", help="The ciphertext for the cipher")
args = parser.parse_args()

# Clean the inputs before doing any operations
if args.alphabet.islower():
    if args.ciphertext:
        args.ciphertext = args.ciphertext.lower()
    if args.plaintext:
        args.plaintext = args.plaintext.lower()
if args.alphabet.isupper():
    if args.ciphertext:
        args.ciphertext = args.ciphertext.upper()
    if args.plaintext:
        args.plaintext = args.plaintext.upper()

if args.ciphertext:
    args.ciphertext = ''.join(c for c in args.ciphertext if c in args.alphabet)
if args.plaintext:
    args.plaintext = ''.join(c for c in args.plaintext if c in args.alphabet)

# Perform the specified operation
if args.operation == "encode":
    # Check that the key and plaintext were provided
    if args.key is None or args.plaintext is None:
        raise ValueError("The key and plaintext must be provided for encoding")
    # Encode the plaintext using the Vigenère cipher
    encoded = encode_vigenere(args.alphabet, args.alphabet, args.plaintext, args.key)
    print(encoded)
elif args.operation == "decode":
    # Check that the key and ciphertext were provided
    if args.key is None or args.ciphertext is None:
        raise ValueError("The key and ciphertext must be provided for decoding")
    # Decode the ciphertext using the Vigenère cipher
    decoded = decode_vigenere(args.alphabet, args.alphabet, args.ciphertext, args.key)
    print(decoded)
elif args.operation == "reversekey":
    # Check that the plaintext and ciphertext were provided
    if args.plaintext is None or args.ciphertext is None:
        raise ValueError("The plaintext and ciphertext must be provided for reversing the key")
    # Find the key for the Vigenère cipher using the plaintext and ciphertext
    key = find_vigenere_key(args.alphabet, args.alphabet, args.plaintext, args.ciphertext)
    print(key)