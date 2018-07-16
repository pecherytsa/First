file = open("INPUT.txt")
line = file.readline()
file.close()
print(line)

a = ""
strin = [a]

for c in line:
    if c == '1':
        a = a + '1'
    else:
        strin.append(a)
        a = ""

strin.append(a)

b = max(strin)
print(len(b))

file = open("OUTPUT.txt", "w")
file.write(str(len(b)))
file.close()



