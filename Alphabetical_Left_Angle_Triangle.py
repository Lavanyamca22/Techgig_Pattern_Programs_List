import string
def main(n):
    # Write code here 
    s = string.ascii_uppercase[0:n]
    count = n-1
    for i in range(0,n):
        print('  '*count,end='')
        print(*[s[i] for j in range(0,i+1)])
        count = count-1

n = int(input())
main(n)
