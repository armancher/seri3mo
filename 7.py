num_list=[]
for i in range(1,21):
    number=int(input("enter a number:"))
    num_list.append(number)

sum_num=sum(num_list)
# sum_numm=0
# for j in num_list:
#     sum_numm+=j
min_num=min(num_list)
# min_numm=num_list[0]
# for k in num_list:
#     if k<min_numm:
#         min_numm=k
max_num=max(num_list)
# max_numm=num_list[0]
# for h in num_list:
#     if h>max_numm:
#         max_numm=h
        
average=sum_num / len(num_list)
print(sum_num)
print(min_num)
print(max_num)
print(average)