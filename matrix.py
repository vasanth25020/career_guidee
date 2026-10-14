a = [[1,2,3],
[4,5,6,],
[7,8,9]]

b =[[9,8,7],
[6,5,4],
[3,2,1]]

result =[[0,0,0],
[0,0,0],
[0,0,0]]

for i in range(len(a)):
    for j in range (len(b[0])):
        print(i)
        print(j)
        if i == j:
            result[i][j]= a[i][j] + b[i][j]
for r in result:
    print(r)



x= [[1,2,3],
    [4,5,6],
    [7,8,9],
    [1,2,3]]

c= [[9,8,7,6],
    [6,5,4,5],
    [3,2,1,4]]

result =[[0,0,0,0]
        ,[0,0,0,0]
        ,[0,0,0,0]
        ,[0,0,0,0]]
        
for i in range(len(x)): # find 
    for d in range (len(c)): #length of 
        for j in range(len(c[0])): # array of indes 0th c
                result[i][j] += x[i][d]*c[d][j]
for r in result:
    print(r)

