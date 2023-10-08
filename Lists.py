# cats = []
# print("Enter the cat name to save it inside a list or leave it blank to exit the program")

# while True:
    
#     catName = input()
#     if catName == '':
#         break
#     cats = cats + [catName]

# print(cats)

list2d = []

for i in range(5):
    columns = []
    for j in range(5):
        columns.append(str(i)+"_"+str(j))
    list2d.append(columns)

print(list2d)

for row in list2d:
    for item in row:
        print(item,end=" ,")
    print()

for x in range(len(list2d)):
    for y in range(len(list2d[0])):
        print(list2d[x][y],end=' ,')
    print()