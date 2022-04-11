cost = int(input("cost(Baht): "))
profit = int(input("profit(%): "))
sell = (100*cost)/(100 - profit)
print("cost = %.2f \nprofit = %.2f \nsell = %.2f" % (cost, profit, sell))