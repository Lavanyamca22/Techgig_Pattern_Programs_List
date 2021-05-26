def print_rangoli(size):
    alpha_str = "abcdefghijklmnopqrstuvwxyz"
    char = alpha_str[size-1]
    count = 0
    list1 = []
    string = ""
    for i in range(0,len(alpha_str)):
        if alpha_str[i] != char:
            string+=alpha_str[i]
            count+=1
        else:
            string+=char
            count+=1
            break
    string1 = string[ : :-1]
    string1+=string[1:len(string)]
    string = string[ : :-1]
    for i in range(0,len(string)):
        for j in range(i+1,len(string1)-i):
            print("-",end ="")
        for k in range(0,i+1):
            if i==0:
                print(string[k],end="")
            else:
                print(string[k],end = "-")
        for j in range(i,0,-1):
            if j-1 == 0:
                print(string[j-1],end = "")
            else:
                print(string[j-1],end="-")
        for k in range(i+1,len(string1)-i):
            print("-",end="")  
        print()
    for i in range(len(string)-1,0,-1):
        for j in range(len(string1)-i,i-1,-1):
            print("-",end="")
        for k in range(0,i):
            print(string[k],end="-")
        for j in range(i-1,0,-1):
            print(string[j-1],end="-")
        for k in range(i,len(string1)-i):
            print("-",end="")
        print()


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
