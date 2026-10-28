# Caesar Cipher (Python)

A small command-line tool that encrypts and decrypts text with the Caesar cipher, using a fixed shift of 3.

## How it works
Every letter moves 3 places forward in the alphabet: `a -> d`, `b -> e`, `x -> a`.
The alphabet wraps around, so `x, y, z` become `a, b, c`. Upper and lower case are kept.
Spaces, numbers and symbols are not changed. Decryption shifts by -3.

## Run it
```
python3 caesar.py
```

## Example
```
Encrypt or decrypt? (e/d): e
Message: Hello, World xyz!
Result: Khoor, Zruog abc!
```

## Tech
Python 3, no external libraries.

## Limits (why this is not real security)
There are only 25 possible shifts, so an attacker can try all of them in seconds (brute force).
Frequency analysis also breaks it. Modern systems use AES or similar algorithms instead.
