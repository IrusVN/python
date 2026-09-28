tokens = ["cat", "dog", "bird"]

def create_vocab(tokens):
    token_to_id = {
        token: index
        for index, token in enumerate(tokens)
    } 
    return token_to_id

result = create_vocab(tokens)
print(result)
