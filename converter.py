with open('rate.txt') as f:
    lines = f.readlines()

curDict = {}

for line in lines:
    part = line.split('\t')
    curDict[part[0]] = part[1]

# print(curDict)

amount = int(input('Enter the amount : '))
print('Currency Available are : ')
for item in curDict:
    print(item)
curr = input('Enter the currency : ')

print(amount*float(curDict[curr]))
