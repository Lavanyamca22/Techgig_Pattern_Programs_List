def main(n):
    for i in range(0,n):
        print(*[i for i in range(1,n+1)])

n = int(input())
main(n)
