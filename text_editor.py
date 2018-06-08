text = open("ochyai.txt","r").read().split()

import string

for line in text:
    for word in line:
        if word in string.ascii_letters or word in string.digits:
            if line in text:
                text.remove(line)

f = open('new_ochyai.txt', 'w')
for x in text:
    f.write(str(x) + "\n")
f.close()

