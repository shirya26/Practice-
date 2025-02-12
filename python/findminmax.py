l = [22,11,55,44,27,99]
small = l[0]
big = l[0]

for i in l:
    if i < small :
        small = i
    else:
        if i > big :
            big = i
print(f"small : {small}\nbig:{big}")

        