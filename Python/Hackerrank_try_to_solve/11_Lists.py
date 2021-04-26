'''if __name__ == '__main__':
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
        list1.remove()'''

if __name__ == '__main__':
    N = int(input())
print_list=[]
list1=[]
for i in range (N):
    inputt=input()
    method=inputt.split()
    if method[0]=="insert":
        a=method[1]
        b=method[2]
        list1.insert(int(a),int(b))
    elif method[0]=="append":
        b=method[1]
        list1.append(int(b))
    elif method[0]=="print":
        a=list1
        print_list.append(a)
    elif method[0]=="sort":
        list1.sort()
    elif method[0]=="pop":
        list1.pop()
    elif method[0]=="reverse":
        list1.reverse()
    elif method[0]=="remove":
        list1.remove()
print(print_list)
        
   
'''
        
   3 2 0

   10
insert 0 3
insert 1 2
append 0
print
sort 
print
reverse
print
pop
print'''