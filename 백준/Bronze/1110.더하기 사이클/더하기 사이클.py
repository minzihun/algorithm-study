N = int(input())

origin = N
cnt = 0

if N == 0:
    print(1)
    
else:
    
    if N < 10:
        N = (N*10) + N
        cnt += 1
            
    while True:
        temp = (N//10) + (N%10)
        N = ((N%10)*10) + (temp%10)
        cnt += 1
        
        if origin == N:
            print(cnt)
            break