stoi = {}
itos = {}

def encode(val):
    if not stoi:
        raise RuntimeError("Encoder uninitialized")
    return_list = []
    for each_char in val:
        return_list.append(stoi[each_char])
    return return_list

def decode(val):
    if not itos:
        raise RuntimeError("Decoder uninitialized")
    return_string = ""
    for each_val in val:
        return_string += itos[each_val]
    return return_string

def load_characters():
    characters = []
    with open(r"input.txt", "r") as f:
        data = f.read()
        for each_character in data:
            if each_character not in characters:
                characters.append(each_character)
    return characters

def build_encoder_decoder_dict(characters):
    for index, character in enumerate(characters):
        stoi[character] = index
        itos[index] = character

def main():
    characters = load_characters()
    build_encoder_decoder_dict(characters)

    encoded_val = encode("Hello World")
    print(f"Encoded Value: {encoded_val}")
    decodeed_val = decode(encoded_val)
    print(f"Decoded Value: {decodeed_val}")

if __name__ == "__main__":
    main()