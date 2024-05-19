A = [
    [6, 7, 8, 10],
    [4, 5, 6, 13],
    [10, 6, 5, 11],
    [8, 9, 7, 9],
    [1, 2, 1, 2],
    [2, 1, 2, 4],
    [3, 3, 2, 2],
    [4, 1, 3, 3] 
]



mn = [6, 4, 5, 7, 1, 1, 2, 1]
mx = [10, 13, 11, 9, 2, 4, 3, 4]

alpha = 0.6

for i in range(0, 8):

    print(mn[i]*alpha + mx[i]*(1-alpha), mn[i]*alpha, mx[i]*(1-alpha))

# for i in range(8):
#     print(0.25* sum(A[i]))


# p = [0.1, 0.4, 0.4, 0.1]


# for i in range(8):
#     summ = 0
#     for j in range(4):
#         s = p[j]* A[i][j]
#         summ += s

#     print(summ)
