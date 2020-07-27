from colorama import Fore, Back, Style, init
init()
import random
print(f'{Fore.BLACK}{Back.LIGHTYELLOW_EX}#####  TORNEIO ESPECIAL  #####\n Seguem os oito times participantes: {Style.DIM}{Style.RESET_ALL}')
a = 'Atlético-PR'
b = 'Coritiba'
c = 'Intern'
d = 'Grêmio'
e = 'Chapecoense'
f = 'Goiás'
g = 'Corinthians'
h = 'Flamengo'
print(f'  {Fore.RED}{Back.BLACK}{a}{Style.RESET_ALL}')
print(f'  {Fore.GREEN}{Back.WHITE}{b}{Style.RESET_ALL}')
print(f'  {Fore.WHITE}{Back.RED}{c}{Style.RESET_ALL}')
print(f'  {Fore.WHITE}{Back.BLUE}{d}{Style.RESET_ALL}')
print(f'  {Fore.BLACK}{Back.LIGHTGREEN_EX}{e}{Style.RESET_ALL}')
print(f'  {Fore.WHITE}{Back.GREEN}{f}{Style.RESET_ALL}')
print(f'  {Fore.WHITE}{Back.BLACK}{g}{Style.RESET_ALL}')
print(f'  {Fore.RED}{Back.BLACK}{h}{Style.RESET_ALL}')
placar = [0, 1, 2, 3, 4, 5]
for rodada in range(1,11):
    times = [a, b, c, d, e, f, g, h]
    random.shuffle(times)
    print(f'{rodada}ª RODADA:')
    print(f'   {times[0]} \t{random.choice(placar)}X{random.choice(placar)} {times[1]} ')
    print(f'   {times[2]} \t{random.choice(placar)}X{random.choice(placar)} {times[3]} ')
    print(f'   {times[4]} \t{random.choice(placar)}X{random.choice(placar)} {times[5]} ')
    print(f'   {times[6]} \t{random.choice(placar)}X{random.choice(placar)} {times[7]} ')
    print(' ')
    print('___________________________________________')
    
    
    print(f'CLASSIFICAÇÃO APÓS A {rodada}ª RODADA:')
    print(f'     {a}: {ap}  pontos')
    print(f'     {c}: {cp}  pontos')
    print(f'     {p}:   {pp}  pontos')
    print('___________________________________________')
    