import wikipedia

while 1:
    inp = input("Q: ")
    print(wikipedia.summary(inp,sentences=2))