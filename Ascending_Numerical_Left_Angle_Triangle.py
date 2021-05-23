def main(n):
    # Write code he
    count = n-1
    for i in range(1,n+1):
        print('  '*count,end='')
        print(*[j for j in range(1,i+1)])
        count = count-1

n = int(input())
main(n)
