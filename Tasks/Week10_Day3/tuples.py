if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split()[:n])
print (hash(integer_list))

#hash() __Return the hash value of the object (if it has one). Hash values are integers. 
# They are used to quickly compare dictionary keys during a dictionary lookup. Numeric values that compare equal have the same hash value
#  (even if they are of different types, as is the case for 1 and 1.0).