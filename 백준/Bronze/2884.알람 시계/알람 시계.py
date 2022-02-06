H, M = map(int, input().split())
diff = M - 45

if diff < 0 :
    H -= 1
    M = 60 + diff
else: M = diff

if H < 0 :
    H = 24 + H
elif H > 23 :
    H = H - 24

print(H, M)