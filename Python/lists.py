if __name__ == '__main__':
    N = int(input())
method_parametrs={}
list1=[]
for i in range (N):
    method, *line = input().split()
    parametrs = list(map(int, line))
    method_parametrs[method] = parametrs
    if method=="insert":
        list1.insert(parametrs[0],parametrs[1])
    if method=="append":
        list1.append(parametrs[0])
    if method=="print":
        print(list1)
    if method=="sort":
        list1.sort()
    if method=="pop":
        list1.pop()
    if method=="reverse":
        list1.reverse()
    if method=="remove":
        list1.remove()
        
   