def rem(l, word):
    n = []
    for item in l:
        if item != word:
            n.append(item.strip())
    return n


l = ["mina", "an", "reno"]
print(rem(l, "an"))