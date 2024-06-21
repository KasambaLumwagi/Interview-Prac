def swap(d):
    return {value:key for key ,value in d.items()}
    

d ={'a': 1, 'b': 2}
swapped_dict = swap(d)
print("Original dictionary:", d)
print("Swapped dictionary:", swapped_dict)
print(d.items())