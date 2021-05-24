import string
def main(n):
    # Write code here 
    s = string.ascii_uppercase[0:n]
    list1 = [i for i in range(1,n+n+1) if(i%2!=0)]
    count = ((n+n)//2)-1
    for i in range(0,n):
        print("  "*count,end='')
        print(*[s[i] for j in range(list1[i])])
        count = count-1

n = int(input())
main(n)
