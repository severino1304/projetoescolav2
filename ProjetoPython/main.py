"""
Projeto de Programação Python
Rodrigo Severino Nº28 12ºB"
"""

# Menu Principal
import jogo, calculo

while True:
    print("1 - Jogar")
    print("2 - Calcular")
    print("3 - Sair")
    opcao=input()
    if opcao == "1":
        jogo.jogar()
    elif opcao == "2":
          calculo.calcular()
    elif opcao == "3":
        break
