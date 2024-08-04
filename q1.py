# Solução da questão 1

import matplotlib.pyplot as plt

def fibonacci_sequence(n: int) -> list:
    # Retorna lista com a sequência até o n termo
    
    sequence = [0, 1]

    for i in range(n-2):
        sequence.append(sequence[i]+sequence[i+1])

    return sequence

def plot_graph(values: list) -> None:
    # Recebe lista de valores ordenados da sequência de fibonacci
    # e constroi gráfico usando matplotlib

    plt.scatter([i for i in range(len(values))], values)
    plt.show()

def main() -> None:
    sequence = fibonacci_sequence(31)
    print(f"A sequência é {sequence}")

    plot_graph(sequence)

# Para evitar confusão com escopo de variáveis
if __name__ == "__main__":
    main()