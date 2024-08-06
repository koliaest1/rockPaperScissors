#  write your code here 

file = open('/Users/nikolaikalinin/Downloads/hyperskill-dataset-101459050.txt', 'r')
count = 0
for line in file:
    if line == "summer\n":
        count = count + 1
print(count)
file.close()
