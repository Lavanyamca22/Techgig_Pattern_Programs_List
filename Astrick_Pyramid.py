def main(n):
    # Write code here 
    list1 = [i for i in range(1,n+n+1) if(i%2!=0)]
    count = ((n+n)//2)-1
    for i in range(0,n):
        print('  '*count,end='')
        print(*['*' for i in range(0,list1[i])])
        count = count-1
n = int(input())
main(n)
