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
    with open(r"input.txt", "r", encoding="utf-8") as f:
        data = f.read()
        return sorted(set(data))

def build_encoder_decoder_dict(characters):
    for index, character in enumerate(characters):
        stoi[character] = index
        itos[index] = character

def test():
    assert decode(encode("text")) == "text"

def get_batch(encoded_data):
    n = int(len(encoded_data) * 0.8)
    return encoded_data[:n], encoded_data[n:]
    

def main():
    characters = load_characters()
    build_encoder_decoder_dict(characters)
    encoded_data = None
    with open(r"input.txt", "r", encoding="utf-8") as f:
        data = f.read()
        encoded_data = encode(data)
    train_set, test_set = get_batch(encoded_data)

if __name__ == "__main__":
    main()