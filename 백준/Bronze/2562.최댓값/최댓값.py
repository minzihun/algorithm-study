num_list =[]

for i in range(9):
    temp = int(input())
    num_list.append(temp)

print(max(num_list))
print(num_list.index(max(num_list))+1)