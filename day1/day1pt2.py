from heapq import heappush, nlargest

def main(inventory):
    currElf = 0
    heap = []
    for line in inventory:
        currElf = 0
        for i in line:
            currElf += int(i)
        heappush(heap,currElf)
    return sum(nlargest(3,heap))
    
with open('inputData.txt','r') as file:
    data = file.read().splitlines()
    lists = []
    current_list = []
    for line in data:
        if line == "":
            if current_list:
                lists.append(current_list)
                current_list = []
        else:
            current_list.append(int(line))
    if current_list:
        lists.append(current_list)


print(main(lists))