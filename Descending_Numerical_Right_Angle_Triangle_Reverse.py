def main(n):
    # Write code here 
    for i in range(n,0,-1):
        print(*[i for j in range(i)])

n = int(input())
main(n)
