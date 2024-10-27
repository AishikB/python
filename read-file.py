f = open("example.txt", "r")
print(f.read())
f.close()

# f = open("example.txt", "a")
# f.write("\nAppending one more line to the file")
# f.close()

# f = open("example.txt", "r")
# print(f.read())
# f.close()


# read file write lines

f=open("example.txt", "w")
f.writelines(["new lines added\n", "old lines removed\n"])
f.close()

f = open("example.txt", "r")
print(f.read())
f.close()

# import csv
# with open('test.csv', mode ='r')as file:
#   csvFile = csv.reader(file)
#   for lines in csvFile:
#         print(lines)


