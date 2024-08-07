numbers=list(map(int,input().split()))
n=int(input())
for i in range(n):
    numbers_range = list(map(int,input().split()))
    sum_of = 0 
    for j in range(len(numbers)):
        number = int(numbers[j])
        if number >= int(numbers_range[0]) and number <= int(numbers_range[1]):
            sum_of = sum_of + number 
    print(sum_of)
    