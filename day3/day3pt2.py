def main(data):
    prioritySum = 0
    for elfIndex in range(0,len(data),3):
        firstElf = data[elfIndex]
        secondElf = data[elfIndex+1]
        thirdElf = data[elfIndex+2]
        commonItem = set(firstElf) & set(secondElf) & set(thirdElf)
        if not commonItem:
            continue
        commonItem = commonItem.pop()
        if commonItem.islower():
            prioritySum += ord(commonItem) - ord('a') + 1
        else:
            prioritySum += ord(commonItem) - ord('A') + 27
    
    return prioritySum


with open('inputData.txt','r') as file:
    data = file.readlines()
    data = [i.strip() for i in data]

print(main(data))