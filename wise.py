import sys
def check(i, j, row1, col1):
    n, m = i, j
    for a in range(row1):
        for b in range(col1):
            if motif[a][b] != 0 and mosaic[i][j] != motif[a][b]:
                return False
            j = j + 1
        i = i + 1
        j = m
    return True

def print_output(ans):
    print(len(ans))
    for i in ans:
        print(*i)
    
    
motif = []
mosaic = []
row1, col1 = map(int, sys.argv[1:3]) 
for i in range(row1):
    motif.append(list(map(int, sys.argv[3 + i * col1: 3 + i * col1 + col1])))
row2, col2=map(int, sys.argv[3 + row1 * col1:5 + row1 * col1])
for i in range(row2):
    mosaic.append(list(map(int, sys.argv[5 + row1 * col1 + i * col2: 5 + row1 * col1 + i * col2 + col2])))

ans=[]

for i in range(row2 - row1 + 1):
    for j in range(col2 - col1 + 1):
        if mosaic[i][j] == motif[0][0] or motif[0][0] == 0:
            if(check(i, j, row1, col1)):
                ans.append([i + 1, j + 1])

print_output(ans)
