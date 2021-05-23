def main(n):
    for i in range(1,n+1):
        print(*['*' for i in range(5)])

n = int(input())
main(n)
