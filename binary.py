list1 = range(0,17)

with open("binary", "bw") as bin_file:
    print(bytes(list1))
    bin_file.write(bytes(list1))

with open("binary", "br") as binFile:
    for i in binFile:
        print (list1)