def main(n):
    # Write code here
    for i in range(n,0,-1):
        print(*[j for j in range(1,i+1)]) 

n = int(input())
main(n)
