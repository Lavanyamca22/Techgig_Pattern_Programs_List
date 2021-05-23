import string
def main(n):
    # Write code here 
    s = string.ascii_uppercase[0:n]
    for i in range(n,-1,-1):
        print(*[s[j] for j in range(0,i)])
n = int(input())
main(n)
