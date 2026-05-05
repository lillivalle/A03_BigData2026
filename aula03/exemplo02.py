#Verificando se a pessoa é maior de idade
# idade = int(input('Digite a idade: ')) 

# > (maior), < (menor), >= (maior ou igual), 
# <= (menor ou igual), == (igual), != (diferente)

# if idade >= 18: 
#     print('Você é adulto! ')
#     print()
# else:
#     print('Você é menor de idade. Não é adulto! ')    

# print('--------------//-------------')
# print()

#------------------------------------

#Classificação por pontos

pontos = int(input('Informe os pontos: '))

if pontos >= 100: #Se
    total = pontos + 10
    print(f'Excelente! =D Agora você tem {total}. ')
elif pontos >= 50: #Se não se (o elif só entra se o if não for verdadeiro)
    total = pontos + 5
    print(f'Bom desempenho! =] Você tem {total} pontos. ')
elif pontos >= 30: 
    total = pontos + 2
    print(f'Desempenho ok! =S Você tem {total} pontos. ')
else: #só sobrou você, se não
    print(f'Treine mais. =/ Pontuação: {pontos} pontos. ')

print('Fim!!!!!!!!')
