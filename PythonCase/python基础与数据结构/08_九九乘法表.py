for r in range(1, 10):
    for c in range(1, r + 1):
        print("{}x{}={}".format(c, r, c * r), end="\t")
    print()

print("--------------------------------------------------" * 2)
r = 1
while r <= 9:
    for c in range(1, r + 1):
        print("{}x{}={}".format(c, r, c * r), end="\t")
    r += 1
    print()

print("--------------------------------------------------" * 2)
r = 1
while r <= 9:
    c = 1
    while c <= r:
        print("{}x{}={}".format(c, r, c * r), end="\t")
        c += 1
    r += 1
    print()

