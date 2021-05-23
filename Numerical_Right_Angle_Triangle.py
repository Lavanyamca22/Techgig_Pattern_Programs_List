def main(n):
    # Write code here 
    for i in range(1,n+1):
        print(*[i for j in range(i)])

n = int(input())
main(n)
