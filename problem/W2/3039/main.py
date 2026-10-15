"""n sort"""

num_count = int(input())
num_list = []

for i in range(num_count):
    num_list.append(int(input()))
    num_list.sort()
i = num_list[0]
print(i)
