from random import randint
from emoji import emojize
from time import sleep
print("======================================================")
print('################ PEDRA PAPEL ou TESOURA ##############\nVamos disputar uma melhor de 10 com o COMPUTADOR!')
contador = 0
pontosjog = 0
pontoscomp = 0
for contador in range(0,10):
    # ESCOLHA DO JOGADOR:
    opcao = int(input(emojize('''Digite a sua opção:
      [ 1 ] PEDRA 
      [ 2 ] PAPEL :scroll:
      [ 3 ] TESOURA :scissors:
        --> Digite a sua opção: ''')))
    sleep(1)
    opcomp = randint(1,3)
    if opcao == 1:
        print(' Você escolheu PEDRA')
    if opcao == 2:
        print(' Você escolheu PAPEL')
    if opcao == 3:
        print(' Você escolheu TESOURA')
    # ESCOLHA DO COMPUTADOR:
    if opcomp == 1:
        print(' O COMPUTADOR escolheu PEDRA')
    if opcomp == 2:
        print(' O COMPUTADOR escolheu PAPEL')
    if opcomp == 3:
        print(' O COMPUTADOR escolheu TESOURA')  
        # RESULTADO:
    if opcao == 1 and opcomp == 1:
        print("   EMPATE!!!")
    elif opcao == 1 and opcomp == 2:
        print('   O COMPUTADOR GANHOU')
        pontoscomp += 1
    elif opcao == 1 and opcomp == 3:
        print('   VOCÊ GANHOU DO COMPUTADOR')
        pontosjog += 1        
    elif opcao == 2 and opcomp == 1:
        print('   VOCÊ GANHOU DO COMPUTADOR')
        pontosjog += 1        
    elif opcao == 2 and opcomp == 2:
        print("   EMPATE!!!")
    elif opcao == 2 and opcomp == 3:
        print('   O COMPUTADOR GANHOU')
        pontoscomp += 1
    elif opcao == 3 and opcomp == 1:
        print('   O COMPUTADOR GANHOU')
        pontoscomp += 1
    elif opcao == 3 and opcomp == 2:
        print('   VOCÊ GANHOU DO COMPUTADOR')
        pontosjog += 1        
    elif opcao == 3 and opcomp == 3:
        print("   EMPATE!!!")
    else:
        print('Opção Inválida. Tente novamente.')
    sleep(1)
    print(f'''PLACAR:
           JOGADOR:    {pontosjog} pontos
           COMPUTADOR: {pontoscomp} pontos''')