import numpy as np

def one_hot_encode(category, all_categories):
    encoded = np.zeros(len(all_categories))
    encoded[all_categories.index(category)] = 1
    return encoded

def encode_list(category_list, all_categories):
    return np.concatenate([one_hot_encode(category, all_categories) for category in category_list])

# Example list
category_list = ['cat', 'dog', 'bird']

# All possible categories
all_categories = ['cat', 'dog', 'bird']

# Encode the list
encoded_list = encode_list(category_list, all_categories)

print(encoded_list)