import time

s = time.time()
for i in 1,2,3,4,5,6,7,8:
    j = i
    while j > 0:
        j = j / 2
e = time.time()

print(e)
print(s)
print(e-s)
