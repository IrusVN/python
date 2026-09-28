tokens = ["cat", "dog", "bird"]

def create_vocab(tokens: list[str]) -> dict[str, int]:
    token_to_id = {
        token: index
        for index, token in enumerate(tokens)
    } 
    return token_to_id

result = create_vocab(tokens)
print(result)
