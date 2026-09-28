def tensor_size(shape: list[int]) -> int:
    result = 1
    for dim in shape:
        result *= dim
    return result

tensor_size([2, 3])       # 6
tensor_size([2, 3, 4])    # 24
tensor_size([2, 3, 4, 5]) # 120
