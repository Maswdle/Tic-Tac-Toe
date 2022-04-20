import sys
pan = [[0,0,0],[0,0,0],[0,0,0]]
def win_if(n1,n2,n3,n4,n5,n6):
    if pan[n1][n2] != 0 and pan[n1][n2] == pan[n3][n4] and  pan[n1][n2] == pan[n5][n6]:
        return 1
    else:
        return 0
def win(z):
    for i in range(3):
        if (win_if(i,0,i,1,i,2)):
            printer()
            print(str(z) + "win")
            input('')
            sys.exit()
    for j in range(3):
        if (win_if(0,j,1,j,2,j)):
            printer()
            print(str(z) + "win")
            input('')
            sys.exit()
    
    if (win_if(0,0,1,1,2,2)):
        printer()
        print(str(z) + "win")
        input('')
        sys.exit()
    
    if (win_if(0,2,1,1,2,0)):
        printer()
        print(str(z) + "win")
        input('')
        sys.exit()
def insd(x,y,z):
    if pan[x][y]  == 0:
        pan[x][y] = z
        win(z)
    else:
        ftor(z)
def printer():
    for i in pan:
        print(*i)
def ftor(z):
    print("Position is occupied")
    x = int(input("in x>>>"))
    y = int(input("in y>>>"))
    insd(x,y,z)
    

for i in range(9):
    printer()
    x = int(input("in x>>>"))
    y = int(input("in y>>>"))
    if (i % 2 == 0):
        insd(x,y,1)
    else:
        insd(x,y,2)
    
print("Tie")
input('')