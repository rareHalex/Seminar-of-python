#4

"""
Есть головоломка каждая буква заменяется на цифру одним способом чтобы результатом операции была истина
нет 2 буквы соотвествовать 1 цифре и нет начала с нуля
"""

# SEND + MORE = MONEY
#  лоб решение
for S in range(1,10):
    for E in range(10):
        for N in range(10):
            for D in range(10):
                for M in range(1, 10):
                    for R in range(10):
                        for O in range(10):
                            for Y in range(10):
                                send = S*1000 + E*100+N*10+D
                                more = M*1000+O*100+R*10+E
                                money = M*10000+O*1000*N*100+E*10+Y
                                letters = [S,E,N,D,M,R,Y]
                                if send+more == money and len(set(letters)) == len(letters):
                                    print(send, more, sep='\n')
                                    break


# permutations(что перебираем,по сколько берем различных групп)
from intertools import permutations
for perm in permutations(range(3)):
    print(perm)  # кортежи

a = 'SEND'
b = 'MORE'
c = 'MONEY'
#это был частный случай напишем теперь общий решатель этой задачи

def convert(a:str,d:dict)->int:
    A = ''
    for ch in a:
        A += str(d[ch])
    return int(A)

chars = list(set(a+b+c)) # сколько букв
leading_chars = list(set(a[0]+b[0]+c[0]))
for perm in permutations(range(10), len(chars)):
    ch_dict = {chars[i]: p for i, p in enumerate}  # дает индекс и значение
    flag = 0
    for ch in leading_chars:
        if ch_dict[ch] ==0:
            flag = 1
    if flag:
        continue
    A, B, C = map(lambda x: convert(x, ch_dict), [a, b, c])
    if A+B == C:
        print(A, B, C)
# лучшеее
for perm in permutations(range(10), len(chars)):
    ch_dict = {chars[i]: p for i, p in enumerate}  # дает индекс и значение
    flag = 0
    if all(ch_dict[x] for x in leading_chars): # all когда все true то он true
        continue
    A, B, C = map(lambda x: convert(x, ch_dict), [a, b, c])
    if A+B == C:
        print(A, B, C)




