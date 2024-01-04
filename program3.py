# Write a program to arrange list in decending order without using function
list = [7, 2, 10, 5, 3, 8, 1]

n = len(list)
print(n)
for i in range(n):
    for j in range(0, n-i-1):
        if list[j] < list[j+1]:
            list[j], list[j+1] = list[j+1], list[j]
print("The sorted list in descending order is:",list)