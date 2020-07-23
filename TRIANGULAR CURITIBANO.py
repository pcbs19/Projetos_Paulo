from random import randint
from math import floor
print(' ')
print('___________________________________________')
print(' ')
print('##### TRIANGULAR CENTÊ #####')
print('___________________________________________')
a = 'Vila Trindade'
c = 'Acrópole'
p = 'Morumbi'
cpeso = 0.7
ppeso = 0.5
print(f'Os times participantes são:\n{a}, {c} e {p}!!!\n_______________________________________________')
aj1 = randint(0,4)
cj1 = floor(((randint(0,5))*cpeso))
pj1 = floor((randint(0,4))*ppeso)
aj2 = randint(0,4)
cj2 = floor(((randint(0,5))*cpeso))
pj2 = floor((randint(0,4))*ppeso)
aj3 = randint(0,4)
cj3 = floor(((randint(0,5))*cpeso))
pj3 = floor((randint(0,4))*ppeso)
aj4 = randint(0,4)
cj4 = floor(((randint(0,5))*cpeso))
pj4 = floor((randint(0,4))*ppeso)
aj5 = randint(0,4)
cj5 = randint(0,4)
pj5 = randint(0,4)

### PRIMEIRA RODADA
#ok = str(input("Digite OK para começar a PRIMEIRA rodada: "))
print(f'Primeira Rodada:\n   Jogo 1: {a} {aj1}x{cj1} {c}\n   Jogo 2: {a} {aj2}x{pj1} {p}\n   Jogo 3: {c} {cj2}x{pj2} {p}')
#jogo 1
if aj1 > cj1:
        ap = 3
        cp = 0
if aj1 == cj1:
        ap = 1
        cp = 1
if aj1 < cj1:
        ap = 0
        cp = 3 
#jogo 2
if aj2 > pj1:
        ap += 3
        pp = 0
if aj2 == pj1:
        ap += 1
        pp = 1
if aj2 < pj1:
        ap += 0
        pp = 3 
#jogo 3
if cj2 > pj2:
        cp += 3
        pp += 0
if cj2 == pj2:
        cp += 1
        pp += 1
if cj2 < pj2:
        cp += 0
        pp += 3    
print('___________________________________________')
print('CLASSIFICAÇÃO APÓS A 1ª RODADA:')
print(f'     {a}: {ap}  pontos')
print(f'     {c}: {cp}  pontos')
print(f'     {p}:   {pp}  pontos')
print('___________________________________________')

### SEGUNDA RODADA
#ok = str(input("Digite OK para começar a SEGUNDA rodada: "))
print(f'Segunda Rodada:\n   Jogo 4: {c} {cj3}x{aj3} {a}\n   Jogo 5: {p}   {pj3}x{aj4} {a}\n   Jogo 6: {p}   {pj4}x{cj4} {c}')
#jogo 4
if cj3 > aj3:
        ap += 0
        cp += 3
if cj3 == aj3:
        ap += 1
        cp += 1
if cj3 < aj3:
        ap += 3
        cp += 0 
#jogo 5
if pj3 > aj4:
        ap += 0
        pp += 3
if pj3 == aj4:
        ap += 1
        pp += 1
if pj3 < aj4:
        ap += 3
        pp += 0 
#jogo 6
if pj4 > cj4:
        cp += 0
        pp += 3
if pj4 == cj4:
        cp += 1
        pp += 1
if pj4 < cj4:
        cp += 3
        pp += 0    
print('___________________________________________')
print('CLASSIFICAÇÃO APÓS A 2ª RODADA:')
print(f'     {a}: {ap}  pontos')
print(f'     {c}: {cp}  pontos')
print(f'     {p}:   {pp}  pontos')
print('___________________________________________')
if ap > cp and ap > pp:
    print(f'### {a} Campeão!!! ###'.upper())
if cp > ap and cp > pp:
    print(f'### {c} Campeão!!! ###'.upper())
if pp > cp and pp > ap:
    print(f'### {p} Campeão!!! ###'.upper())
# FINAL ATLÉTICO COXA    
if ap == cp and ap > pp and cp > pp:
    ok = str(input('Dê "ENTER" para começar a FINAL!!! '))
    print(f'RODADA FINAL:\n   FINAL: {a} {aj5}x{cj5} {c}')
    if aj5 > cj5:
        print(f'### {a} Campeão!!! ###'.upper())
    if aj5 < cj5:
        print(f'### {c} Campeão!!! ###'.upper())
    if aj5 == cj5:
        print(f'Iremos para a disputa de Penaltis!!!')
        apenaltis = randint(0,5)
        cpenaltis = randint(0,5)
        print(f' {a} {apenaltis} x {cpenaltis} {c}')
        if apenaltis > cpenaltis:
            print(f'{a} Campeão!!!'.upper())
        if apenaltis < cpenaltis:
            print(f'{c} Campeão!!!'.upper())
        if apenaltis == cpenaltis:
            apenaltis2 = randint(0,2)
            cpenaltis2 = randint(0,2)
            print(f' {a} {apenaltis2} x {cpenaltis2} {c}')
            if apenaltis2 > cpenaltis2:
                print(f'{a} Campeão!!!'.upper())
            if apenaltis2 < cpenaltis2:
                print(f'{c} Campeão!!!'.upper())
            else:
                print('vá se ferrar!')

# FINAL ATLÉTICO PARANA    
if ap == pp and ap > cp and pp > cp:
    ok = str(input('Dê "ENTER" para começar a FINAL!!! '))
    print(f'RODADA FINAL:\nFINAL: {a} {aj5}x{pj5} {p}')
    if aj5 > pj5:
        print(f'{a} Campeão!!!'.upper())
    if aj5 < pj5:
        print(f'{p} Campeão!!!'.upper())
    if aj5 == pj5:
        print(f'Iremos para a disputa de Penaltis!!!')
        apenaltis = randint(0,5)
        ppenaltis = randint(0,5)
        print(f' {a} {apenaltis} x {ppenaltis} {p}')
        if apenaltis > cpenaltis:
            print(f'{a} Campeão!!!'.upper())
        if apenaltis < ppenaltis:
            print(f'{p} Campeão!!!'.upper())
        if apenaltis == ppenaltis:
            apenaltis2 = randint(0,2)
            ppenaltis2 = randint(0,2)
            print(f' {a} {apenaltis2} x {ppenaltis2} {p}')
            if apenaltis2 > ppenaltis2:
                print(f'{a} Campeão!!!'.upper())
            if apenaltis2 < ppenaltis2:
                print(f'{p} Campeão!!!'.upper())
            else:
                print('Vá se ferrar!')

# FINAL COXA PARANA
if cp == pp and cp > ap and pp > ap:
    ok = str(input('Dê "ENTER" para começar a FINAL!!! '))
    print(f'RODADA FINAL:\nFINAL: {c} {cj5}x{pj5} {p}')
    if cj5 > pj5:
        print(f'{c} Campeão!!!'.upper())
    if cj5 < pj5:
        print(f'{p} Campeão!!!'.upper())
    if cj5 == pj5:
        print(f'Iremos para a disputa de Penaltis!!!')
        cpenaltis = randint(0,5)
        ppenaltis = randint(0,5)
        print(f' {c} {cpenaltis} x {ppenaltis} {p}')
        if cpenaltis > ppenaltis:
            print(f'{c} Campeão!!!'.upper())
        if cpenaltis < ppenaltis:
            print(f'{p} Campeão!!!'.upper())
        if cpenaltis == apenaltis:
            cpenaltis2 = randint(0,2)
            ppenaltis2 = randint(0,2)
            print(f' {c} {cpenaltis2} x {ppenaltis2} {p}')
            if cpenaltis2 > ppenaltis2:
                print(f'{c} Campeão!!!'.upper())
            if cpenaltis2 < ppenaltis2:
                print(f'{p} Campeão!!!'.upper())
            else:
                print('vá se ferrar!')
        