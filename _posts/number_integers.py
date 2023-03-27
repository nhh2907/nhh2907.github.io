# https://school.programmers.co.kr/learn/courses/30/lessons/12912
def solution(a, b):
   if a>b:
       temp = a
       a = b
       b = temp
        
   return sum([i for i in range(a, b+1)])

def solution(a, b):
    if a>b:
        a, b = b, a
        
    return sum(range(a, b+1))  # iterable을 sum함수 인자로