import math

def get_sqrt(x):
    a = math.sqrt(x)
    return a

num = [2,4,8, 19, 200, 160, 47, 73]

for i in num:
    a = get_sqrt(i)
    print(f"sqrt of {i} equals {a}")