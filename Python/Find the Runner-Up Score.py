__name__ = '__main__'
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split()[:n])
list1=list(arr)

list1.sort()
a=list1.pop(-1)
list1[:] = (value for value in list1 if value != a)
print(max(list1))
