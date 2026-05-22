from funcionalidades import *

tv=Televisor('SONY', 'SAMSUNG')

controle= ControleRemoto(tv)

#Escola de canais

canais_disponiveis=[2,4,5,7,9,11,13]

for canal in canais_disponiveis:
    controle.sintonizaCanal(canal)

#Menu visual para o usuario
while True:
    print("\n---MENU DA TELEVISÃO---")
    print(f"Canais dispooníveis: {tv.lista_de_canais}")
    print(f"Canal atual: {tv.canal_atual}")
    print(f"Volume atual: {tv.volume}")
    print("--------------------------")
    print("Opções de Volume: [+] Aumentar | [-] Diminuir")

# Recebe a escolha do usuario

    opcao = input(
        "Digite o número do canal que deseja,"
        "'+' para volume, '-' para volume" 
        "(ou 'sair' para desligar): "
        ).strip()

# Condição para encerrar

    if opcao.lower() == 'sair':
        print("Deligando a TV... Tchau!!!")
        break

#Opções de volume
    elif opcao =='+':
        controle.aumentaVolume()
        print("Volume aumentado!")
    elif opcao =='-':
        controle.diminuiVolume()
        print("Volume diminuído!")

# Muda o canal
if opcao.isdigit():

    canal_escolhido =int(opcao)

    #Verefica o canal
    if canal_escolhido in tv.lista_de_canais:
        controle.trocaCanal(canal_escolhido)
        print(f"Sintonizando canal {canal_escolhido} com sucesso")
    else:
        print("Este canal não está dísponínel")
else:
        print("Digite uma opção válida")
