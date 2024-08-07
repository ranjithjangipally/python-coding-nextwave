a=int(input())
actual_list = []
for i in range(a):
    num_list = list(map(int,input().split(",")))
    actual_list.append(num_list)
  
group_with_highest_score = actual_list[0]
for each_group in actual_list:
    if sum(each_group) > sum(group_with_highest_score):
        group_with_highest_score = each_group 

final_string = ""
for i in group_with_highest_score:
    final_string += str(i) + " "
print(final_string)
        