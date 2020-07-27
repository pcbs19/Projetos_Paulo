print('='*80)
print('########  CALCULADORA DE ÍNDICE DE MASSA CORPÓREA   #########')
alt = float(input('Digite a sua Altura: '))
peso = float(input('Digite o seu Peso atual: '))
print(f'Sua altura é de {alt:.2f}m e seu peso é de {peso:.1f}Kg.')
imc = peso / alt**2
if imc < 18.5:
    print(f'Seu IMC é de {imc:.1f} e você está ABAIXO DO PESO ideal.')
elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC é de {imc:.1f} e você está no PESO IDEAL!')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC é de {imc:.1f}. Cuidado! Você está com SOBREPESO!')
elif imc >= 30 and imc < 35:
    print(f'Seu IMC é de {imc:.1f}. Você é OBESO e deve iniciar uma dieta imediatamente!')
else:
    print(f'Seu IMC é de {imc:.1f} e você é OBESO MÓRBIDO! Procure ajuda médica...')
peso_ideal = 24.9999999999999*(alt**2)
print(f'Para atingir o PESO IDEAL, seu peso deve ser de {peso_ideal:.1f}Kg')