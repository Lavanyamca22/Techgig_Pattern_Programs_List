import string
def main(n):
    # Write code here 
    s = string.ascii_uppercase[0:n]
    count = 0
    for i in range(n-1,-1,-1):
        print('  '*count,end='')
        print(*[s[i] for j in range(0,i+1)])
        count = count+1 

n = int(input())
main(n)
