# Solução da questão 2

import io 
# Parte da stdlib, importei apenas para colocar as dicas de tipo (type hints) do arquivo texto

import matplotlib.pyplot as plt

def print_database(file: io.TextIOWrapper) -> None:
    print("Imprimindo tabela:")
    for line in file:
        print(line, end="")

def extract_columns(file: io.TextIOWrapper) -> tuple[list, list]:
    dates = []
    wvht = []
    first = True    # Ignora a primeira linha

    for line in file:
        if not first:
            dates.append(line.split(",")[0])
            wvht.append(float(line.split(",")[1]))

        first = False

    return dates, wvht

def plot_wvht(dates: list, wvht: list) -> None:
    plt.scatter(dates, wvht)
    plt.xticks(rotation=90)
    plt.subplots_adjust(bottom=0.4)
    # see better date plotting to fix overlap of x axis label
    plt.show()


def polynomial_multiplication(pA:list, pB:list) -> list:
    result = [0]*(len(pA)+len(pB))

    for i in range(len(pA)):
        for j in range(len(pB)):
            result[i+j] += pA[i] * pB[j]

    return result


def polynomial_addition(pA:list, pB:list) -> list:
    result = []
    for i in range(max(len(pA), len(pB))):
        try:
            a = pA[i]

        except IndexError:
            a = 0

        try:
            b = pB[i]

        except IndexError:
            b = 0

        result.append(a + b)

    return result

def polynomial_printing(p:list) -> None:
    for index, value in enumerate(p):
        if value == 0:
            continue

        if value > 0:
            print("+", end="")

        if index == 0:
            print(value, end=" ")

        elif index == 1:
            print(f"{value}x", end=" ") if value != 1 else print(f"x", end=" ")

        else:
            print(f"{value}x^{index}", end=" ") if value != 1 else print(f"x^{index}", end=" ")

def get_applied_polynomial(p: list, value: float) -> float:
    acc = 0
    for i in range(len(p)):
        acc = acc + (p[i]*value**i)

    return acc

def divide_polynomial_by_value(polynomial: list, value: float) -> list:
    return [polynomial[i]/value for i in range(len(polynomial))]

def convert_timestamp(stamp: str) -> float:
    # Retorna o tempo em horas decorrido desde o início do experimento.
    pass

def plot_interpolated_function(p:list) -> None:
    # plotar função polinomial com matplot e pontos discretos. x sendo as horas, y os valores
    pass

def interpolate_data_points(x_points: list, y_points: list) -> None:
    # Usando o algoritmo de lagrange de interpolação polinomial

    size = len(x_points)
    polynomial = [0] * size
    
    for j in range(size):
        first = True
        for i in range(size):
            if i == j:
                continue

            if first:
                first = False
                aux = [-x_points[i], 1]
                aux = divide_polynomial_by_value(aux, x_points[j] - x_points[i])
           
            aux = polynomial_multiplication(aux, [-x_points[i], 1])
            aux = divide_polynomial_by_value(aux, x_points[j] - x_points[i])

        aux = polynomial_multiplication([y_points[j]], aux)
        polynomial = polynomial_addition(polynomial, aux)

    return polynomial
        

def main() -> None:
    with open("./dados_ic.csv", "r", encoding="utf8") as file:
        dates, wvht = extract_columns(file)

        minimum = min(wvht)
        maximum = max(wvht)
        average = sum(wvht)/len(wvht)

        print(f"Valor mínimo: {minimum}")
        print(f"Valor máximo: {maximum}")
        print(f"Valor médio: {average}")

        # plot_wvht(dates, wvht)

        result = interpolate_data_points([0, 1, 2, 3, 5], [4.13, 3.01, 2.79, 3.94, 2.7])
        polynomial_printing(result)
        print(get_applied_polynomial(result, 3))


# Para evitar confusão com escopo de variáveis
if __name__ == "__main__":
    main()