def main(n):
    list1 = [i for i in range(1,n+n) if(i%2!=0)]
    count = 0
    for i in range(len(list1)-1,-1,-1):
        print('  '*count,end='')
        print(*list(map(int,[list1[i] for j in range(list1[i])])))
        count = count+1

main(10)


