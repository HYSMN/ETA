import csv
import numpy as np
import io
from numpy import unicode

filename1 = 'routeall3.txt'
filename2 = 'map.txt'
i = 0
with open(filename1) as f1:
    reader1 = csv.reader(f1)
    for row1 in reader1:
        arr = []
        with open(filename2) as f2:
            reader2 = csv.reader(f2)
            for row2 in reader2:
                if row1[1] == row2[0]:
                    node1 = row2[1]
                    arr.append(node1)
                if row1[2] == row2[0]:
                    node2 = row2[1]
                    arr.append(node2)
                if row1[4] == row2[0]:
                    node3 = row2[1]
                    arr.append(node3)
                if row1[6] == row2[0]:
                    node4 = row2[1]
                    arr.append(node4)
                if row1[9] == row2[0]:
                    node5 = row2[1]
                    arr.append(node5)
                if row1[13] == row2[0]:
                    node6 = row2[1]
                    arr.append(node6)
                if row1[14] == row2[0]:
                    node7 = row2[1]
                    arr.append(node7)
                if row1[15] == row2[0]:
                    node8 = row2[1]
                    arr.append(node8)
                if row1[16] == row2[0]:
                    node9 = row2[1]
                    arr.append(node9)
                if row1[18] == row2[0]:
                    node10 = row2[1]
                    arr.append(node10)

            with io.open('nodenum3.txt', mode="a", encoding='utf-8') as data:  
                data.write(unicode(arr))
                data.write('\n')
                data.close()
            f2.close()
    f1.close()
