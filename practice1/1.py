

def prepareMass2(mass):
    # итого: [x, y, uneff, b_counter, f, class]
    mass = [i.extend([0, 0, 0, 0]) for i in mass]

def countingSolutionsEffectivicy(mass):
    prepareMass2(mass)
    for i in range(len(mass)):
        if mass[i][2]==0:
            mass[i][2] = 1
            for j in range(len(mass)):
                if j!=i and mass[j][2] != 2:
                    if mass[j][0] - mass[i][0] <=0 and mass[j][1] - mass[i][1] <=0:
                        mass[j][2] = 2
                    if mass[j][0] - mass[i][0] >0 and mass[j][1] - mass[i][1] >0:
                        mass[i][3] +=1
        if mass[i][2]==2:
            for j in range(len(mass)):
                if j!=i:
                    if mass[j][0] - mass[i][0] >0 and mass[j][1] - mass[i][1] >0:
                        mass[i][3] +=1
    return mass

def countF(mass, count):
    for i in range(len(mass)):
        mass[i][4] = 1 / (1 + mass[i][3] / (count-1))



def defineClass(mass):
    C1 = 1
    C2 = 0.85
    C3 = 0.75
    for i in range(len(mass)):
        t = min([abs(mass[i][4] - C1), abs(mass[i][4] - C2), abs(mass[i][4] - C3)])

        if t == abs(mass[i][4] - C1):
            mass[i][5] = 1
        if t == abs(mass[i][4] - C2):
            mass[i][5] = 2
        if t == abs(mass[i][4] - C3):
            mass[i][5] = 3