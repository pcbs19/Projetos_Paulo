from random import randint
from math import floor
print(' ')
print('___________________________________________')
print(' ')
print('##### CAMPEONATÃO CAJURÚ #####')
print('___________________________________________')
print('##### FASE 1 - CENTENARIÃO #####')
print('___________________________________________')
a = 'Vila Trindade'
c = 'Acrópole'
p = 'Morumbi'
cpeso = 0.8
ppeso = 0.7
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


##################################################################################################
                
print(' ')
print('___________________________________________')
print(' ')
print('##### CAMPEONATÃO CAJURÚ #####')
print('___________________________________________')
print('##### FASE 2 - CAJURUZÃO #####')
print('___________________________________________')
v = 'Vila Oficinas'
j = 'Jardim Santa Barbara'
g = 'Agrícola'
jpeso = 0.8
gpeso = 0.7
print(f'Os times participantes são:\n{v}, {j} e {g}!!!\n_______________________________________________')
vj1 = randint(0,4)
jj1 = floor(((randint(0,5))*cpeso))
gj1 = floor((randint(0,4))*ppeso)
vj2 = randint(0,4)
jj2 = floor(((randint(0,5))*cpeso))
gj2 = floor((randint(0,4))*ppeso)
vj3 = randint(0,4)
jj3 = floor(((randint(0,5))*cpeso))
gj3 = floor((randint(0,4))*ppeso)
vj4 = randint(0,4)
jj4 = floor(((randint(0,5))*cpeso))
gj4 = floor((randint(0,4))*ppeso)
vj5 = randint(0,4)
jj5 = randint(0,4)
gj5 = randint(0,4)
ff1 = randint(0,5)
ff2 = randint(0,5)

### PRIMEIRA RODADA
#ok = str(input("Digite OK para começar a PRIMEIRA rodada: "))
print(f'Primeira Rodada:\n   Jogo 1: {v} {vj1}x{jj1} {j}\n   Jogo 2: {v} {vj2}x{gj1} {g}\n   Jogo 3: {j} {jj2}x{gj2} {g}')
#jogo 1
if vj1 > jj1:
        vp = 3
        jp = 0
if vj1 == jj1:
        vp = 1
        jp = 1
if vj1 < jj1:
        vp = 0
        jp = 3 
#jogo 2
if vj2 > gj1:
        vp += 3
        gp = 0
if vj2 == gj1:
        vp += 1
        gp = 1
if vj2 < gj1:
        vp += 0
        gp = 3 
#jogo 3
if jj2 > gj2:
        jp += 3
        gp += 0
if jj2 == gj2:
        jp += 1
        gp += 1
if jj2 < gj2:
        jp += 0
        gp += 3    
print('___________________________________________')
print('CLASSIFICAÇÃO APÓS A 1ª RODADA:')
print(f'     {v}: {vp}  pontos')
print(f'     {j}: {jp}  pontos')
print(f'     {g}: {gp}  pontos')
print('___________________________________________')

### SEGUNDA RODADA
#ok = str(input("Digite OK para começar a SEGUNDA rodada: "))
print(f'Segunda Rodada:\n   Jogo 4: {j} {jj3}x{vj3} {v}\n   Jogo 5: {g}   {gj3}x{vj4} {v}\n   Jogo 6: {g}   {gj4}x{jj4} {j}')
#jogo 4
if jj3 > vj3:
        vp += 0
        jp += 3
if jj3 == vj3:
        vp += 1
        jp += 1
if jj3 < vj3:
        vp += 3
        jp += 0 
#jogo 5
if gj3 > vj4:
        vp += 0
        gp += 3
if gj3 == vj4:
        vp += 1
        gp += 1
if gj3 < vj4:
        vp += 3
        gp += 0 
#jogo 6
if gj4 > jj4:
        jp += 0
        gp += 3
if gj4 == jj4:
        jp += 1
        gp += 1
if gj4 < jj4:
        jp += 3
        gp += 0    
print('___________________________________________')
print('CLASSIFICAÇÃO APÓS A 2ª RODADA:')
print(f'     {v}: {vp}  pontos')
print(f'     {j}: {jp}  pontos')
print(f'     {g}: {gp}  pontos')
print('___________________________________________')
if vp > jp and vp > gp:
    print(f'### {v} Campeão!!! ###'.upper())
if jp > vp and jp > gp:
    print(f'### {j} Campeão!!! ###'.upper())
if gp > jp and gp > vp:
    print(f'### {g} Campeão!!! ###'.upper())
# FINAL ATLÉTICO COXA    
if vp == jp and vp > gp and jp > gp:
    ok = str(input('Dê "ENTER" para começar a FINAL!!! '))
    print(f'RODADA FINAL:\n   FINAL: {v} {vj5}x{jj5} {j}')
    if vj5 > jj5:
        vp += 3
        jp += 0
        print(f'### {v} Campeão!!! ###'.upper())
    if vj5 < jj5:
        vp += 0
        jp += 3
        print(f'### {j} Campeão!!! ###'.upper())

# FINAL ATLÉTICO PARANA    
if vp == gp and vp > jp and gp > jp:
    ok = str(input('Dê "ENTER" para começar a FINAL!!! '))
    print(f'RODADA FINAL:\nFINAL: {v} {vj5}x{gj5} {g}')
    if vj5 > gj5:
        vp += 0
        gp += 3
        print(f'{v} Campeão!!!'.upper())
    if vj5 < gj5:
        vp += 0
        gp += 3
        print(f'{g} Campeão!!!'.upper())
   
# FINAL COXA PARANA
if jp == gp and jp > vp and gp > vp:
    ok = str(input('Dê "ENTER" para começar a FINAL!!! '))
    print(f'RODADA FINAL:\nFINAL: {j} {jj5}x{gj5} {g}')
    if jj5 > gj5:
        jp += 0
        gp += 3
        print(f'{j} Campeão!!!'.upper())
    if jj5 < gj5:
        jp += 0
        gp += 3
        print(f'{g} Campeão!!!'.upper())
 
#FINAL GRANDE CAMPEONATO CAJURU
print(' ')
print('___________________________________________')
print(' ')
print('##### CAMPEONATÃO CAJURÚ #####')
print('___________________________________________')
print('############# GRANDE FINAL ################')
print('___________________________________________')       
#finalista 1
if ap > cp and ap > pp:
    f1 = a
if cp > ap and cp > pp:
    f1 = c
if pp > ap and pp > cp:
    f1 = p
print(f'Finalista 1: {f1}')
  
#finalista 2
if vp > jp and vp > gp:
    f2 = v
if jp > vp and jp > gp:
    f2 = j
if gp > vp and gp > jp:
    f2 = g      
print(f'Finalista 2: {f2}')
print('###############################################')
print('@@@@@@@@@@ GRANDE FINAL CAMPEONATÃO CAJURÚ @@@@@@@@@@@')
print('###############################################')
print(f'FINALZONA:\n       {f1} {ff1}x{ff2} {f2}')
if ff1 > ff2:
    print(f'################## {f1} Campeão!!! ######################'.upper())
if ff1 < ff2:
    print(f'################## {f2} Campeão!!! ######################'.upper())