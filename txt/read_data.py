def read(filename):
    with open(f"{filename}.txt", "r") as f:
        content = f.read()
        print(content)
        
read("data")