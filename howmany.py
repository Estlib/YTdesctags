howmany = int(input(print("How many: ")))
startvalue = int(input(print("starting number: ")))
i = 0
if startvalue < 99:
    while i < howmany:
        print("E2N-00" + str(startvalue) + "-STRO-___")
        startvalue += 1
        i += 1
elif startvalue >= 100:
    while i < howmany:
        print("E2N-0" + str(startvalue) + "-STRO-___")
        startvalue += 1
        i += 1
elif startvalue >= 1000:
    while i < howmany:
        print("E2N-" + str(startvalue) + "-STRO-___")
        startvalue += 1
        i += 1