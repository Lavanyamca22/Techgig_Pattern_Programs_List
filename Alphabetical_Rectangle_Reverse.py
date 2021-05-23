import string
def main(n):
    # Write code here 
    s = string.ascii_uppercase[0:n]
    for i in range(n-1,-1,-1):
        print(*[s[i] for j in range(5)])


n = int(input())
main(n)

