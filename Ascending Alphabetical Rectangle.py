import string
def main(n):
    s = string.ascii_uppercase[0:n]
    for i in range(0,n):
        print(*[j for j in s])

n = int(input())
main(n)
