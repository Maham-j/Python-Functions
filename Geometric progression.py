def geometric_progression(a1,r,n):
    
    for n in range(1,n):
        an = a1 * (r ** (n-1))
        print(f'a{n}: {an}')
    
a1 = 1
r = -3
n = 6

geometric_progression(a1,r,n)
