file = open("employees.txt", "a")

print(file.readable())

#if file.readable():
    #print(file.read())
    #print(file.readline())
    #print(file.readline())
    #print(file.readlines())

    #for line in file.readlines():
    #    print(line)

file.write("\nGray is 25 years old")


file.close()

file1 = open("index.html", "w")
file1.write("<html><head>This is page header</head></html>")
file1.close()