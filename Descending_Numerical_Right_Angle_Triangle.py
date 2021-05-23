def main(n):
    # Write code here 
    for i in range(1,n+1):
        print(*[j for j in range(n,i-1,-1)])

n = int(input())
main(n)
