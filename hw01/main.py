for i in range(1,10):
    print(' '*(i-1)*8,end='')
    for j in range(i,10):
        formula='{0:1}x{1:1}={2:<4}'.format(i,j,i*j)
        print(formula,end='')
    print()

