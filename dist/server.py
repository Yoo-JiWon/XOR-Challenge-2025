def get_flag():
    try:
        with open("flag.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "ERROR: Flag file not found!"

XOR_KEY = ???  # What is this? Can you guess the key?

SECRET_PHRASE = "XOR"

encoded_phrase = ''.join(chr(ord(c) ^ XOR_KEY) for c in SECRET_PHRASE)

def check_input(user_input):
    decoded_input = ''.join(chr(ord(c) ^ XOR_KEY) for c in user_input)
    
    if decoded_input == SECRET_PHRASE:
        return f"Flag: {get_flag()}"
    else:
        return "Wrong input!"

print("Can you find the key and decode the phrase?")

