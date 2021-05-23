import string 
def main(n):
    S = string.ascii_uppercase[0:n]
    for i in S:
        print(*list(map(str, [i for j in range(5)])))


n = int(input())
main(n)
