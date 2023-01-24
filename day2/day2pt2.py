#A,X = Rock
#B,Y = Paper
#C,Z = Scissor

def main(rounds):
    points = 0
    moveDic = {'X':1, 'Y':2,'Z':3}
    outcomesDic = {'AX':3,'AY':6,'AZ':0,'BX':0,'BY':3,'BZ':6,'CX':6,'CY':0,'CZ':3}
    pt2Dic = {'AX':'Z','AY':'X','AZ':'Y','BX':'X','BY':'Y','BZ':'Z','CX':'Y','CY':'Z','CZ':'X'}
    for round in rounds:
        points += moveDic[pt2Dic[round[0]+round[1]]] + outcomesDic[round[0]+pt2Dic[round[0]+round[1]]]
    return points

with open('inputData.txt','r') as file:
    data = file.readlines()
    data = [i.strip().split() for i in data]

print(main(data))