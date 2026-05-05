#Atividade 01

#Se o cliente realizar uma compra acima de R$250,00 o sistema deve aplicar um desconto de 16%. Caso contrário o valor da compra deve permanecer o mesmo.

gasto = float(input('Insira o valor gasto na compra com decimais: '))

if gasto > 250.00:
    desco = gasto *0.16 #aplicou o desconto
    gastodesc = round(gasto - desco,2)
    print(f'Você tem um desconto de 16% e o valor a ser pago é {gastodesc}. ')
    print()

else:
    print(f'O total a ser pago não tem desconto, pois deu {gasto}. Para adicionar o desconto gaste mais {250.00-gasto}.')