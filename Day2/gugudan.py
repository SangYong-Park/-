for dan in range(1,10):
    print(dan, " 단", end="           ")
print()
for hang in range(2,10):
    # print(dan, " 단")
    for dan in range(1,10):
        # print(dan, "*", hang, "=", (dan*hang))
        # print("%d * %d = %d" % (dan, hang, (dan*hang)))
        print("%d * %d = %2d" % (dan, hang,(dan*hang)), end="\t")
    print()