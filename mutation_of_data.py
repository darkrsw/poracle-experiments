file1 = open('dataset100.txt', 'r')
Lines = file1.readlines()
import random
count = 0
# Strips the newline character
for line in Lines:
    #print(line)
    sample = line.split(';')
    for i in range(0, (len(sample)-1)):

        if i >= 5:
            if random.randint(0, 1) == 0:
                data = float(sample[i])+ (float(sample[i])*.01)
                f = open("newdata101.csv", "a")
                f.write(str(data))
                f.write(',')
                f.close()
            else:
                data = float(sample[i]) - (float(sample[i]) * .01)
                f = open("newdata101.csv", "a")
                f.write(str(data))
                f.write(',')
                f.close()
        else:
            f = open("newdata101.csv", "a")
            f.write(sample[i])
            f.write(',')
            f.close()
    f = open("newdata101.csv", "a")
    f.write('False')
    f.write('\n')
    f.close()

