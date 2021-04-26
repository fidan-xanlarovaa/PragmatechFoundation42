'''name, *line = input().split() <--- doubt

input()  # reads single line of input
# 'abc 23 34 45'

.split()  # splits it into a list of whitespace separated tokens
# ['abc', '23', '34', '45']

name, *line = ...  # name is assigned first token, line a list of the remaining tokens
name  # 'abc'
line  #  ['23', '34', '45']

scores = list(map(float, line))  # maps float function onto the list of strings
scores  # [23.0, 34.0, 45.0]'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()[:3]
        scores = list(map(float, line))
        student_marks[name] = scores
print(student_marks)
query_name = input()
sum=0
for i in student_marks[query_name]:
    sum=sum+i
print(sum/3)



