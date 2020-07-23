from colorama import Fore, Back, Style, init
init()
import random
print(f'{Fore.BLACK}{Back.LIGHTYELLOW_EX}#####  TORNEIO ESPECIAL  #####\n Seguem os oito times participantes: {Style.DIM}{Style.RESET_ALL}')
a = 'Atlético-PR'
b = 'Coritiba'
c = 'Internacional'
d = 'Grêmio'
e = 'Chapecoense'
f = 'Goiás'
g = 'Corinthians'
h = 'Flamengo'
lista = [a, b, c, d, e, f, g, h]
print(f'  {Fore.RED}{Back.BLACK}{a}{Style.RESET_ALL}')
print(f'  {Fore.GREEN}{Back.WHITE}{b}{Style.RESET_ALL}')
print(f'  {Fore.WHITE}{Back.RED}{c}{Style.RESET_ALL}')
print(f'  {Fore.WHITE}{Back.BLUE}{d}{Style.RESET_ALL}')
print(f'  {Fore.BLACK}{Back.LIGHTGREEN_EX}{e}{Style.RESET_ALL}')
print(f'  {Fore.WHITE}{Back.GREEN}{f}{Style.RESET_ALL}')
print(f'  {Fore.WHITE}{Back.BLACK}{g}{Style.RESET_ALL}')
print(f'  {Fore.RED}{Back.BLACK}{h}{Style.RESET_ALL}')
listaresult = [0, 1, 2, 3, 4, 5]


rodada = 1
while rodada <= 10:
    print(f'{rodada}ª RODADA:')
    j = 1
    while j <= 4:
        print(f' Jogo {j}: {random.choice(lista)} {random.choice(listaresult)}X{random.choice(listaresult)} {random.choice(lista)} ')
        j += 1
    rodada += 1