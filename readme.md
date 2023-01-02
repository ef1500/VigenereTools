# Vigenère Cipher Tools

This program implements the Vigenère cipher, a method of encrypting and decrypting texts using a repeating key.

## Requirements

This program requires Python 3.

## Usage

To run the program, use the following command:

`python vigenere.py [operation] [options]`


### Options

- `operation`: The operation to perform. Must be one of `encode`, `decode`, or `reversekey`.
- `--alphabet`, `-a`: The alphabet to use. Required for all operations.
- `--key`, `-k`: The key for the cipher. Required for `encode` and `decode` operations.
- `--plaintext`, `-p`: The plaintext. Required for `encode` and `reversekey` operations.
- `--ciphertext`, `-c`: The ciphertext for the cipher. Required for `decode` and `reversekey` operations.

### Examples

To encode a message using the Vigenère cipher:

`python cipher_tools.py encode -a ABCDEFGHIJKLMNOPQRSTUVWXYZ -k HELLO -p HELLO`


To decode a message using the Vigenère cipher:

`python cipher_tools.py decode -a ABCDEFGHIJKLMNOPQRSTUVWXYZ -k HELLO -c IFMMP`


To find the key for a Vigenère cipher using the plaintext and ciphertext:

`python cipher_tools.py reversekey -a ABCDEFGHIJKLMNOPQRSTUVWXYZ -p HELLO -c IFMMP`


## Table Generator

This repository also includes a tool for generating a lookup table for ciphers. To use the tool, run the following command:

`python3 table_generator.py [ALPHABET] [IMAGE]`


### Options

- `ALPHABET`: The alphabet to generate a table for.
- `IMAGE`: A boolean value indicating whether or not to generate an image. Optional.

### Examples

To generate a lookup table for the alphabet "ABCDEFGHIJKLMNOPQRSTUVWXYZ":

`python3 table_generator.py ABCDEFGHIJKLMNOPQRSTUVWXYZ`


To generate a lookup table for the alphabet "ABCDEFGHIJKLMNOPQRSTUVWXYZ" and an image:

`python3 table_generator.py ABCDEFGHIJKLMNOPQRSTUVWXYZ True`
