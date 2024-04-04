output = 0
with open("20230726121145.log") as f:
    for line in f:
        line = line.rstrip()
        if "total_tokens" in line:
            lol = line.split()
            if len(lol) > 2:
                continue
            output += int(lol[-1]) 
    print("total tokens used", output)