import random
count = 10000
check_count = 0

for i in range(count):
    a = random.randint(0,99)
    b = random.randint(0,99)
    if a>b: check_count +=1

print('Veroyatnost = ')
print(check_count/count)
