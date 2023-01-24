def main(rounds):
    points = 0
    moveDic = {'X':1, 'Y':2,'Z':3}
    outcomesDic = {'AX':3,'AY':6,'AZ':0,'BX':0,'BY':3,'BZ':6,'CX':6,'CY':0,'CZ':3}
    for round in rounds:
        points += moveDic[round[1]] + outcomesDic[round[0]+round[1]]
    return points

with open('inputData.txt','r') as file:
    data = file.readlines()
    data = [i.strip().split() for i in data]

print(main(data))