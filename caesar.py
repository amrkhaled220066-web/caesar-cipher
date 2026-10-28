# Caesar cipher: shifts every letter by 3 places (a -> d, b -> e, ..., x -> a)

SHIFT = 3


def caesar(text, shift):
    result = ""
    for ch in text:
        if "a" <= ch <= "z":
            result += chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
        elif "A" <= ch <= "Z":
            result += chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
        else:
            result += ch  # spaces, numbers and symbols stay the same
    return result


mode = input("Encrypt or decrypt? (e/d): ").lower()
message = input("Message: ")

if mode == "e":
    print("Result:", caesar(message, SHIFT))
elif mode == "d":
    print("Result:", caesar(message, -SHIFT))
else:
    print("Please type e or d.")
