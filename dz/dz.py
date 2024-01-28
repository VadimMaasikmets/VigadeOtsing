#1
''' (for)
mitu=0
for k in range(1,16):
    n=float(input("Sisesta "+str(k)+". arv"))
    if int(n)== float(n):
        mitu+=1
print("Täisarvude kogus: ",mitu)
'''
''' (while true)
k=0
while True:
    k+=1
    n=float(input("Sisesta arv nr." +str(k)))
    if int(n)==float(n):
        mitu+=1
        if k==15: break
        '''
''' (while)
k=0
mitu=0
while k<15:
    k+=1
    n=float(input("Sisesta arv nr." +str(k)))
    if int(n)==float(n):
        mitu+=1
        '''
#16
'''(while)
n=9
i=1
while i<=n:
    j=1
    while j <=n:
        if i==j:
            print(i, end="")
        else:
            print(0, end="")
        j+=1
    print()
    i+=1
'''
'''(for)

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            print(i, end="")
        else:
            print(0, end="")
    print()
'''


''' (while true)
n=9
i=1
while True:
    j = 1
    while j <= n:
        if i == j:
            print(i, end="")
        else:
            print(0, end="")
        j += 1
    print()
    i += 1

    if i > n:
        break
 '''


#2
'''(while)
A = int(input("Введите число A: "))
sum = 0
i = 1

while i <= A:
    sum += i
    i += 1

print(f"Сумма всех натуральных чисел от 1 до {A}:{sum}")

'''
'''(while true)



A = int(input("Введите число A: "))
sum_while = 0
i = 1

while True:
    sum_while += i
    i += 1
    if i > A:
        break

print(f"Сумма всех натуральных чисел от 1 до {A}:{sum_while}")
'''



'''(for)

A = int(input("Введите число A: "))
sum_for = 0

for i in range(1, A + 1):
    sum_for += i

print(f"Сумма всех натуральных чисел от 1 до {A}:{sum_for}")
'''
#3
''' (while)
a = 1
b = 0

while b < 8:
    c = float(input("Введите число: "))
    if c > 0:
        a *= c
        b += 1

print(f"Произведение положительных чисел :{a}")


a_while = 1
b_while = 0
'''
''' (while true)

while True:
    c_while = float(input("Введите число: "))
    if c_while > 0:
        a_while *= c_while
        b_while += 1
    if b_while == 8:
        break

print(f"Произведение положительных чисел :{a_while}")

'''
'''(for)
a_for = 1

for i in range(8):
    c_for = float(input("Введите число: "))
    if c_for > 0:
        a_for *= c_for

print(f"Произведение положительных чисел :{a_for}")
'''


#4
''' (while)
num = 10

while num <= 20:
    square = num**2
    print(f"Квадрат числа {num}:{square}")
    num += 1


num_while = 10

'''
'''(while true)

while True:
    square_while = num_while**2
    print(f"Квадрат числа {num_while}:{square_while}")
    num_while += 1

    if num_while > 20:
        break

'''
'''(for)
for num_for in range(10, 21):
    square_for = num_for**2
    print(f"Квадрат числа {num_for}:{square_for}")

    '''

#5
'''(while)
n = int(input("Введите количество чисел N: "))

sum_negative = 0
i = 0
while i < n:
    number = float(input(f"Введите число {i + 1}: "))
    if number < 0:
        sum_negative += number
    i += 1

print(f"Сумма отрицательных чисел:{sum_negative}")

'''
''' (while true)
sum_negative = 0
i = 0
while True:
    number = float(input(f"Введите число {i + 1} (для завершения введите 0): "))
    if number == 0:
        break
    if number < 0:
        sum_negative += number
    i += 1

print(f"Сумма отрицательных чисел:{sum_negative}")
'''
'''(for)

sum_negative = 0
for i in range(N):
    number = float(input(f"Введите число {i + 1}: "))
    if number < 0:
        sum_negative += number

print(f"Сумма отрицательных чисел:{sum_negative}")
'''

#7
'''(while)
a= int(input("введите значение А: "))
b= int(input("введите значение B: "))
k= int(input("введите значение K: "))

i= a
while i<=b:
    if i%k==0:
        print(i)
    i+=1
    '''
'''(while true)
a= int(input("введите значение А: "))
b= int(input("введите значение B: "))
k= int(input("введите значение K: "))
i=a
while True:
    if i>b:
        break
    if i%k==0:
        print(i)
    i+=1
    '''
'''(for)
a= int(input("введите значение А: "))
b= int(input("введите значение B: "))
k= int(input("введите значение K: "))
for i in range(a, b + 1):
    if i%k==0:
        print(i)   
        '''

#13
'''(while)
a=100
b=0
c=0
while a<=1000:
    if a%7==0:
        print(a)
        b+=1
        c+=a
    a+=1
print(f"Количество: {b}")
print(f"Сумма: {c}")
'''
'''(while true)
a=100
b=0
c=0
while True:
    if a>1000:
        break
    if a%7==0:
        print(a)
        b +=1
        c+=a
    a+=1
print(f"Количество: {b}")
print(f"Сумма: {c}")    
       '''
'''(for)      
b=0
c=0
for a in range(100, 1000):
    if a%7==0:
        print(a)
        b+=1
        c+=a
print(f"Количество: {b}")
print(f"Сумма: {c}")  
'''
#14
'''(while)
import random
a = random.randint(1, 10)
b=1
c=1
while b<=a:
    c*=b
    b+=1
print(f"Произвенедние: {c}")
'''
'''(while true)
import random
a = random.randint(1, 10)
b=1
c=1
while True:
    if b>a:
        break
    c*=b
    b+=1
print(f"Произвенедние: {c}")
'''
'''(for)
import random
a = random.randint(1, 10)
c=1
for b in range(1, a+1):
    c*=b   
print(f"Произвенедние: {c}")
'''
#17
'''(while)
a=1
while a<=9:
    b=2*a
    print(f"2*{a}={b}")
    a+=1
 '''
'''(while true)
a=1
while True:
    b=2*a
    print(f"2*{a}={b}")
    a+=1
    if a>9:
        break   

        '''
'''(for)
for a in range(1, 10):
    b=2*a
    print(f"2*{a}={b}")
    '''  
