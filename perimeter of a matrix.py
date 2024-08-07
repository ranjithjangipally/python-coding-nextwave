rows,columns = list(map(int,input().split()))

total = 0
for i in range(rows):
    row_list = list(map(int,input().split()))
    if i==0 or i==rows-1:
        for j in row_list:
            total += j 
    else:
        total += row_list[0] + row_list[columns-1] 
print(total)
