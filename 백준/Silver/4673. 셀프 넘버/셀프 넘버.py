# 생성자
def d(n):
    n = n + sum(map(int, str(n)))
    return n

# 생성자를 위한 집합
dn_arr = set()

for i in range(1, 10001):
    dn_arr.add(d(i))

# 생성자가 없으면 셀프넘버
for self_number in range(1, 10001):
    if self_number not in dn_arr: 
        print(self_number)