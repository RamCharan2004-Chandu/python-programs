with open("data.txt", "w") as f:
    f.write("Line 1\nLine 2")
with open("data.txt", "r") as f:
    print(f.read())