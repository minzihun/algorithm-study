N = int(input())
star = '*'
blank = ' '

for i in range(N):
    print((blank*(N-i-1)) + (star * (i+1)))