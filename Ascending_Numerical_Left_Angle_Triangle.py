def main(n):
    # Write code here 
    count = n-1
    for i in range(1,n+1):
        print('  '*count,end='')
        print(*[i for j in range(0,i)])
        count = count-1

n = int(input())
main(n)
