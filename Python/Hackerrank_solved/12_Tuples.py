if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split()[:n])
integer_list1=tuple(integer_list)
print (hash(integer_list1))
