s='zztqooauhujtmxnsbzpykwlvpfyqijvdhuhiroodmuxiobyvwwxupqwydkpeebxmfvxhgicuzdealkgxlfmjiucasokrdznmtlwh'
lst = []
for item in s:
    if lst and lst[-1] == item: #Empty strings are "falsy" which means they are considered false in a Boolean context. If lst means if truthy or "if list is not empty, do this"
        lst.pop()
    else:
        lst.append(item)

print("Empty String") if not lst else print(''.join(lst)) #Empty strings are "falsy" which means they are considered false in a Boolean context. If not lst means, "if not truthy" or, if list is empty.
