from time import sleep
import colorama
from colorama import Fore, Back, Style, init
init()
print('_'*50)
print('!                  TABUADAS                      !')
print('-'*50)
print(' ')
print('Bem vindo ao aplicativo TABUADAS')
print(' ')
sleep(1)
for x in range (1,1000):
    print(" \nDigite um número para ver a sua TABUADA\nou digite 0 para sair a qualquer momento.")
    t = int(input('  --> Digite sua opção: '))
    print(f' \n{Fore.BLACK}{Back.LIGHTWHITE_EX} Tabuada do {t}: {Style.NORMAL}{Style.RESET_ALL}')    
    if t == 0:
        print(' \nObrigado por usar nosso aplicativo!')
        break    
    for n in range(1,11):
        print(f' {t} x {n} = {t*n}')
    x += 1

