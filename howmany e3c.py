howmany = int(input(print("How many: ")))
startvalue = int(input(print("starting number: ")))
i = 0
if startvalue < 100:
    while i < howmany:
        print("E3N-00" + str(startvalue) + "-RRDC-C-___")
        startvalue += 1
        i += 1
elif startvalue >= 100:
    while i < howmany:
        print("E3N-0" + str(startvalue) + "-RRDC-C-___")
        startvalue += 1
        i += 1
elif startvalue >= 1000:
    while i < howmany:
        print("E3N-" + str(startvalue) + "-RRDC-C-___")
        startvalue += 1
        i += 1