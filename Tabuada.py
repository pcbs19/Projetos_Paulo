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
x = 0
while x <=1000:
    n = 1
    print("Digite qual TABUADA você quer, \nou digite 0 para sair a qualquer momento.")
    t = int(input('  --> Digite sua opção: '))
    print(' ')
    sleep(2)
    if t != 0:
        print(f'{Fore.BLACK}{Back.LIGHTWHITE_EX} Tabuada do {t}: {Style.NORMAL}{Style.RESET_ALL}')
        while n <= 10:
            print(f' {t} x {n} = {t*n}')
            n += 1
        print(' ')
    elif t == 0:
        print(' \nObrigado por usar nosso aplicativo!')
        break
    x += 1