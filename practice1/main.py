import funcs0 as funcs
from graphic_plotter import plotter

COUNT_OF_SOLUTIONS = 20
N_LIMITER = 1


#l = funcs.createListOfSolutions(COUNT_OF_SOLUTIONS, N_LIMITER)
#l, COUNT_OF_SOLUTIONS, N_LIMITER  = funcs.getDefaultSolution()
#l, COUNT_OF_SOLUTIONS, N_LIMITER  = funcs.getMySolution()
l, COUNT_OF_SOLUTIONS, N_LIMITER = funcs.getSolution2()

print("Hello")

funcs.setSolutionsEffectivicy(l)

print(*funcs.getEffectiveSolutions(l), sep="\n")

funcs.countF(l)
funcs.defineCluster(l)

dots_x = [i[0] for i in l]
dots_y = [i[1] for i in l]
clusters = [i[-1] for i in l]
print("-------------------------------------")
print(*l, sep ="\n")

plotter(N_LIMITER, dots_x, dots_y, clusters)



