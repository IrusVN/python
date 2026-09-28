def tensor_size(shape: list[int]) -> int:
    return 1 if not shape else shape[0] * tensor_size(shape[1:])

tensor_size([2, 3])       # 6
tensor_size([2, 3, 4])    # 24
tensor_size([2, 3, 4, 5]) # 120
