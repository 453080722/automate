#! python3

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

cloWiths = []
max = 0

for i in range(len(tableData)):
    for k in range(len(tableData[i])-1):
        if len(tableData[i][k]) <= len(tableData[i][k+1]):
            max = len(tableData[i][k+1])
        cloWiths.append(max)

for k in range(len(tableData[0])):
    for i in range(len(tableData)):
        print(tableData[i][k].rjust(cloWiths[i]), end='')
    print()