def main(n):
    # Write code here 
    for i in range(n,0,-1):
        print(*list(map(int,[i for j in range(5,0,-1)])))

n = int(input())
main(n)
