# Hash-Generator
A simple Python script that generates a SHA-256 hash from user input text.

## How It Works

The program asks the user to enter some text, then uses Python's built-in `hashlib` library to generate and print the SHA-256 hash of that text.

## How to Run

1. Make sure you have Python installed.
2. Run the script:
3. 3. Enter any text when prompted.
4. The SHA-256 hash of your text will be printed.


## What Is SHA-256?

SHA-256 is a cryptographic hash function that takes an input and produces a fixed-length (256-bit) string of characters. It's commonly used to verify data integrity, since even a tiny change in the input produces a completely different hash.

## Note

Hashing is one-way — you can't reverse a hash back into the original text. This makes it useful for things like storing password hashes (instead of plaintext passwords) or verifying file integrity.

## Possible Improvements

- Let the user choose the hashing algorithm (e.g. MD5, SHA-1, SHA-512)
- Add an option to hash the contents of a file instead of just text input
- Add a comparison feature to check if two hashes match

- Let the user choose the hashing algorithm (e.g. MD5, SHA-1, SHA-512)
- Add an option to hash the contents of a file instead of just text input
- Add a comparison feature to check if two hashes match
