import random

MINMAX = 100
print("Hello")


def getDefaultSolution():
    return  ([
        [7, 1],
        [22, 7],
        [46, 30],
        [32, 19],
        [4, 39],
        [13, 47],
        [19, 41],
        [39, 14],
        [2, 40],
        [38, 4]
    ], 10, 26)

def getMySolution():
    return ([
        [9, 19],
        [12, 22],
        [12, 18],
        [13, 20],
        [13, 15],
        [14, 17],
        [15, 22],
        [16, 15],
        [16, 17],
        [16, 19],
        [17, 11],
        [18, 21],
        [19, 12],
        [19, 14],
        [19, 17],
        [20, 9],
        [20, 19],
        [22, 7],
        [22, 11],
        [22, 14]
    ], 20, 13)


def getSolution2(): 
  return  ( 
        [[0.8195965237694169, 1.7121793839419364], 
        [0.8388280482567345, 1.3850564896108808], 
        [0.9074821176162207, 1.1920438023467428], 
        [1.0694548336753318, 1.6776885013786824], 
        [1.1093434615891407, 1.8913170986963213], 
        [1.143486711427233, 1.0352032320439797], 
        [1.4207186419675, 1.402191089809756], 
        [1.4369871012615443, 0.6208539592694295], 
        [1.4771733644351248, 0.9102458744613684], 
        [1.5511280143764128, 0.7443107962989859], 
        [1.5686086667752397, 0.865479367530364], 
        [1.652078627325182, 1.250306352001895],  
        [1.6717644046934876, 1.4820565583541945], 
        [1.6886368474519409, 1.5199934720396047], 
        [1.7136071722964163, 0.9589758602318477], 
        [1.816788225379784, 1.3318821704915607], 
        [1.8548082733025217, 0.9144498549300883], 
        [1.871318742949979, 0.7564592003854065], 
        [1.8831148557521438, 1.1222983742177894], 
        [1.9021913015178193, 1.315120880031584] 
    ], 20, 1)

def createListOfSolutions(elements, n):
    l = []
    while len(l) < elements:
        f1 = random.uniform(0, MINMAX)
        f2 = random.uniform(0, MINMAX)
        if ((f1-n)**2 + (f2-n)**2 <= n**2) and (-f1 + f2 <= n) and (f1 + f2 >= 2*n):
            l.append([f1, f2])
            
    return l



def prepareMass(mass):
    # итого: [x, y, effectivicy, b_counter, f, class]
    mass = [i.extend([0, 0, 0, 0]) for i in mass]

def setSolutionsEffectivicy(mass):
    prepareMass(mass)
    for i in range(len(mass)):
        if mass[i][2]==0:
            mass[i][2] = 1
            for j in range(len(mass)):
                if j!=i and mass[j][2] != 2:
                    if mass[j][0] - mass[i][0] <=0 and mass[j][1] - mass[i][1] <=0:
                        mass[j][2] = 2
                    if mass[j][0] - mass[i][0] >=0 and mass[j][1] - mass[i][1] >=0:
                        mass[i][3] +=1
        if mass[i][2]==2:
            for j in range(len(mass)):
                if j!=i:
                    if mass[j][0] - mass[i][0] >=0 and mass[j][1] - mass[i][1] >=0:
                        mass[i][3] +=1

def getEffectiveSolutions(mass):
    l = []
    for i in range(len(mass)):
        if mass[i][2] == 1:
            t = [mass[i][0], mass[i][1]]
            l.append(t)
    return l


def countF(mass):
    count = len(mass)
    for i in range(len(mass)):
        mass[i][4] = 1 / (1 + mass[i][3] / (count-1))



def defineCluster(mass):
    C1 = 1
    C2 = 0.85
    C3 = 0.75
    for i in range(len(mass)):
        t = min([abs(mass[i][4] - C1), abs(mass[i][4] - C2), abs(mass[i][4] - C3)])

        if t == abs(mass[i][4] - C1):
            mass[i][5] = 0
        if t == abs(mass[i][4] - C2):
            mass[i][5] = 1
        if t == abs(mass[i][4] - C3):
            mass[i][5] = 2








