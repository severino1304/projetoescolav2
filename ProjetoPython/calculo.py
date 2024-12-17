def calcular():
    import matplotlib.pyplot as plt
    """
    Importa o módulo "matplotlib" para poder desenhar gráficos.
    Deu-se o nome "plt" ao modulo para que seja mais fácil de utilizar para o código.
    """
    def calculodistancia(tempos, velocidades): # Esta função serve para calcular a área sob a curva (distância) usando a regra do trapézio
        distancia = 0
        for i in range(1, len(tempos)): # "Len" serve para devolver o número total de elementos na lista tempos
        # Usamos o "range" para percorrer cada par de pontos consecutivos de forma a calcular a área de cada trapézio
            distancia += (velocidades[i-1] + velocidades[i]) / 2 * (tempos[i] - tempos[i-1])
        # Calculou-se a área de cada trapézio entre dois pontos consecutivos de tempo e velocidade.
        # A área do trapézio representa a distância percorrida nesse intervalo de tempo.
        return distancia # O resultado final da distância total percorrida é entregue com o "return" para que possa ser usado fora da função

    while True:
        print("Este programa calcula a velocidade média e desenha o gráfico velocidade-tempo")
        pontos = int(input("Quantos pontos deseja inserir no gráfico velocidade-tempo? "))
        tempos = [] # Cria uma lista para guardar os valores de tempo
        velocidades = [] # Cria uma lista para guardar os valores de velocidade

        for i in range(pontos): # Até o número de pontos desejado pedir ao utilizador os valores de tempo e velocidade
            t = float(input("Insira o tempo t" + str(i+1) + " (em segundos): "))
            v = float(input("Insira a velocidade v" + str(i+1) + " (em m/s): "))
            tempos.append(t)
            velocidades.append(v)

        distanciatotal = calculodistancia(tempos, velocidades) # Calcula a distância percorrida e a velocidade média
        tempototal = tempos[-1] - tempos[0] # O tempo total é a diferença entre o último e o primeiro tempo

        if tempototal != 0:
            vm = distanciatotal / tempototal # A velocidade média é calculada através da diferença da distância total pelo tempo total
            print(" A velocidade média é:", vm, "(m/s)")
        else:
            print("Erro: o tempo total é zero! Certifique-se de que o primeiro e o último tempo são diferentes")

        # Para esboçar o gráfico velocidade-tempo
        plt.plot(tempos, velocidades, marker="o", color="b", linestyle="-", label="Velocidade (m/s)")
        plt.xlabel("Tempo (s)")
        plt.ylabel("Velocidade (m/s)")
        plt.title("Gráfico Velocidade-Tempo")
        plt.legend()
        plt.grid(True)
        plt.show()

        repetir = input("Quer repetir? (sim/nao): ").strip().lower()
        if repetir == "nao":
            break

        
if __name__=="__main__":
    calcular()
















