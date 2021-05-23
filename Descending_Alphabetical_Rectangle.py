import string
def main(n):
    s = string.ascii_uppercase[0:n]
    for i in range(0,n):
        print(*[s[j] for j in range(n-1,-1,-1)])

n = int(input())
main(n)
