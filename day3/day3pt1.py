def main(rucksacks):
    prioritySum = 0
    for rucksack in rucksacks:
        firstCompartment = rucksack[:len(rucksack)//2]
        secondCompartment = rucksack[len(rucksack)//2:]
        commonItem = set(firstCompartment) & set(secondCompartment)
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