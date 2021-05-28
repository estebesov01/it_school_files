# Простые делители числа 13195 - это 5, 7, 13 и 29.

# Каков самый большой делитель числа 600851475143, являющийся простым числом?
import math,time
def issimple(a):
    r=math.ceil(math.sqrt(a))
    lst=[]
    for i in range(3,r):
        if i % 2 != 0:
            if a%i==0:
                if issimple(i)==[]:
                    lst.append(i)
    return lst
start = time.perf_counter()
r=issimple(600851475143)
print(r)
end = time.perf_counter()
print(end - start)