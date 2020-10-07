def userinput(name,matrix):
    k=1
    print("Enter the element of matrix"+name+".")
    for i in range(row):
        for j in range(col):
            print('Enter the ',k,'value : ',end='')
            matrix[i][j] = int(input())
            k += 1
        print()

def printtt(name,matrix):
    print("Matrix"+name+" is : ")
    for i in range(row):
        for j in range(col):
            print(matrix[i][j],"  ",end='')
        print()
    print()

def tranpose(name,matrix):
    print("Transpose of Matrix"+name+" is : ")
    for i in range(col):
        for j in range(row):
            print(matrix[j][i],'  ',end='')
        print()
    print()

while True:
    while True:
        row = int(input("Enter the number of Row of matrix : "))
        col = int(input("Enter the column of matrix : "))
        a = [[0 for i in range(col)]for j in range(row)]
        b = [[0 for i in range(col)]for j in range(row)]
        answer = [[0 for i in range(col)]for j in range(row)]
        userinput('A',a)
        printtt('A',a)
        userinput('B',b)
        printtt('B',b)
        cont = input("Do you want to reEnter the element (Y/N) : ")
        if cont == 'y' or cont == 'Y':
            continue
        else:
            break

    while True:
        print("1.Find Addition of two matrix.")
        print("2.Find Subtration of two matrix.")
        print("3.Find Transpose of two matrix.")
        choice = int(input('Enter the Choice : '))
        if choice == 1:    
            printtt('A',a)
            printtt('B',b)
            print('Addition on MatrixA and MatrixB is : ')
            for i in range(row):
                for j in range(col):
                    answer[i][j] = a[i][j]+b[i][j]
                    print(answer[i][j],"  ",end='')
                print()
        elif choice == 2:
            printtt('A',a)
            printtt('B',b)
            print("Subtraction of MatrixA and MatrixB is : ")
            for i in range(row):
                for j in range(col):
                    answer[i][j] = a[i][j]-b[i][j]
                    print(answer[i][j],'  ',end='')
                print()
        elif choice == 3:
            printtt('A',a)
            tranpose('A',a)
            printtt('B',b)
            tranpose('B',b)
        else:
            print("Invalid Choice.")
        cont = input('Do you want to continue for check rest of option (Y/N) : ')
        if cont=='y' or cont=='Y':
            continue
        else:
            break
    cont = input("Do you want to rerun all-over program (Y/N) : ")
    if cont=='y' or cont=='Y':
        continue
    else:
        break