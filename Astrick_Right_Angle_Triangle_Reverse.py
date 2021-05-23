
def main(n):
    # Write code here
    for i in range(n,-1,-1):
        print(*['*' for j in range(0,i)]) 

n = int(input())
main(n)
