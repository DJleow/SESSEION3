#topic: Calculating a Running Total
total = 0 #assigned total to zero
for num in range(1,6): #loop through numbers 1 to 5
    total += num
    print(f'Current total:{total}')
