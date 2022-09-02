#1. Cálculo de Bônus
#Crie um programa que calcule e dê um print no bônus que os funcionários devem receber segundo a regra:
#   A meta é 1000 vendas.
#   Se o valor de vendas for maior ou igual a meta, o valor do bônus do funcionário é 10% do valor de vendas.
#   Caso contrário o valor de bônus do funcionário é 0.
#Print o bônus dos 3 funcionários

# print('-----PROGRAMA BÔNUS FUNCIONÁRIOS-----')
# meta = 1000
# vendas_1 = int(input('Insira o numero de vendas do funcionário 1: '))
# vendas_2 = int(input('Insira o numero de vendas do funcionário 2: '))
# vendas_3 = int(input('Insira o numero de vendas do funcionário 3: '))

# def bonus (vendas):
#     if vendas >= meta:
#         return vendas * 0.1
#     else:
#         return 0
# print ('''No modelo 1 de bonificação. O bônus dos funcionários ficaria:
# Funcionário 1: {}
# Funcionário 2: {} 
# Funcionário 3: {}
# '''.format(bonus(vendas_1),bonus(vendas_2),bonus(vendas_3)))


# 2. Cálculo de bônus com uma nova regra
# Agora, crie um novo código que calcule e dê um print no bônus dos funcionários novamente. Porém há uma nova regra nesse 2º caso:
#       A meta é 1000 vendas
# Agora, os funcionários que venderem muito acima da meta ganham mais bônus do que os outros. Então o bônus é definido da seguinte forma:
#       Se vendas funcionário for maior ou igual a 2000, então o bônus é de 15% sobre o valor de vendas
#       Se vendas funcionário for menor do que 2000 e maior ou igual a 1000, então o bônus é de 10% sobre o valor de vendas
#       Se vendas funcionário for menos do que 1000 então o bônus do funcionário é de 0.
# Use as mesmas variáveis de vendas_funcionários


# def bonus (vendas):
#     if vendas >= 2*meta:
#         return vendas * 0.15
#     elif vendas >=meta:
#         return vendas * 0.1
#     else:
#         return 0

# print ('''No modelo 2 de bonificação. O bônus dos funcionários ficaria:
# Funcionário 1: {}
# Funcionário 2: {} 
# Funcionário 3: {}
# '''.format(bonus(vendas_1),bonus(vendas_2),bonus(vendas_3)))



# 3. Criando um mini sistema de controle de estoque
# Crie um sistema para ser usado pelo time de controle de estoque de um centro de distribuição.
# Imagine que ao fim de todo dia, o time conta quantas unidades de produto existem no estoque. 
# Se tivermos um estoque abaixo do estoque permitido para aquela categoria do produto, 
# o time deve ser avisado (print) para fazer um novo pedido daquele produto.
# Cada categoria de produto tem um estoque mínimo diferente, segundo a regra abaixo:
#   alimentos -> Estoque mínimo: 50
#   bebidas -> Estoque mínimo: 75
#   limpeza -> Estoque mínimo: 30

# Para isso vamos criar um programa que pede 3 inputs do usuário: 
#   nome do produto, categoria e quantidade atual em estoque.

# Se o produto tiver abaixo do estoque mínimo da categoria dele, o programa deve printar a mensagem "Solicitar {produto} à equipe de compras, temos apenas {unidades} em estoque"
# Exemplo: Se o usuário preenche os inputs com: bebidas, dolly, 90, o programa não deve exibir nenhuma mensagem.
# Agora, se o usuário preenche os inputs com: bebidas, guaraná, 60, o programa deve exibir a mensagem "Solicitar guaraná à equipe de compras, temos apenas 60 unidades em estoque.

# Obs: lembre de usar o int() para transformar o número inserido pelo usuário no input de string para int.
# Obs2: Caso o usuário não preencha alguma das 3 informações, o programa deve exibir uma mensagem para avisá-lo de preencher corretamente.


print('-----PROGRAMA CHECAGEM DE ESTOQUE-----')
em_ali = 50
em_bebibas = 75
em_limpeza = 30

produto = input('Insira o nome do produto: ')
cat = input('Insira a categoria (1 - Ali, 2 - Bebida, 3 - Limpeza): ')
unidades = input('Insira o estoque do produto: ')

if produto and (cat and unidades):  #checa se todas as variaveis foram preenchidas
    if int(cat) == 1 and int(unidades) < em_ali:
        print (f"Solicitar {produto} à equipe de compras, temos apenas {unidades} em estoque")
    elif int(cat) == 2 and int(unidades) < em_bebibas:
        print (f"Solicitar {produto} à equipe de compras, temos apenas {unidades} em estoque")
    elif int(cat) == 3 and int(unidades) < em_limpeza:
        print (f"Solicitar {produto} à equipe de compras, temos apenas {unidades} em estoque")
else:
    print ('Preencha todos os dados')

    
