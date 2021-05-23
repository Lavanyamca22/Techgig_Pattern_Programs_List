def main(n):
    # Write code here 
    count = 0
    for i in range(n,-1,-1):
        print('  '*count,end='')
        print(*['*' for j in range(0,i)])
        count = count+1 

n = int(input())
main(n)
