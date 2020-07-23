from random import randint
print('#'*100)
print('SUGESTÕES DE NÚMEROS PARA LOTERIA!')
loteria = int(input('Digite 1 para MEGASENA ou 2 para QUINA: '))
#MEGASENA
m1 = randint(1,60)
m2 = randint(1,60)
m3 = randint(1,60)
m4 = randint(1,60)
m5 = randint(1,60)
m6 = randint(1,60)
lm = [m1,m2,m3,m4,m5,m6]
lmo = sorted(lm)
#QUINA
q1 = randint(1,80)
q2 = randint(1,80)
q3 = randint(1,80)
q4 = randint(1,80)
q5 = randint(1,80)
lq = [q1,q2,q3,q4,q5]
lqo = sorted(lq)
if loteria == 1:
    print(f'NÚMEROS PARA MEGASENA: {lmo[0],lmo[1],lmo[2],lmo[3],lmo[4],lmo[5]}')
if loteria == 2:
    print(f'NÚMEROS PARA QUINA: {lqo[0],lqo[1],lqo[2],lqo[3],lqo[4]}')

