with open("./data.txt", "r") as f:
    data = f.read()



with open("./test.txt", "w") as w:
    w.write(data)
