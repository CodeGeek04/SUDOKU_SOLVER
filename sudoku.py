def solve(mat,i,j):
    if i>8:
        #"VALUE OF I"
        return True
    if j>8:
        j=0
        return solve(mat,i+1,j)
    if mat[i][j]!=0:
        return solve(mat,i,j+1)
    lst1=check(mat,i,j)
    ans=False
    if lst1.count(1)==0:
        return False
    for h in range(1,10):
        if lst1[h]==0:
            mat[i][j]=h
            ans=ans or solve(mat,i,j+1)
            if ans==True:
                break
            mat[i][j]=0
    return ans

def check(mat,i,j):
    lst1=[0,0,0,0,0,0,0,0,0,0]
    for k in range(0,9):
        if mat[k][j]!=0:
            lst1[mat[k][j]]=1
    for k in range(0,9):
        if mat[i][k]!=0:
            lst1[mat[i][k]]=1
    m=int(i/3)
    n=int(j/3)
    for  k in range(int(m*3),int(m*3+3)):
        for l in range(int(n*3),int(n*3+3)):
            if mat[k][l]!=0:
                lst1[mat[k][l]]=1
    return lst1

mat=[[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
for i in range(9):
    for j in range(9):
        str1="ENTER ELEMENT "+str(i+1)+" "+str(j+1)+":"
        mat[i][j]=int(input(str1))
solve(mat,0,0)
for i in range(9):
    for j in range(9):
        print(mat[i][j],end=" ")
    print("\n")

while True:
    pass
