tokens = ["Hello", "world", "hello", "AI", "world", "hello"]
count_frequency = {}
# cách 1
# for token in tokens:
#     if token in count_frequency:
#         count_frequency[token] += 1
#     else:
#         count_frequency[token] = 1

# cách 2
for token in tokens:
    count_frequency[token] = count_frequency.get(token, 0) + 1

print (count_frequency)