import string
def main(n):
    # Write code here 
    s = string.ascii_uppercase[0:n]
    for i in range(0,n):
        print(*[s[i] for j in range(i+1)])

n = int(input())
main(n)
