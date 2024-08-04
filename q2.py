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


def plot_interpolated_function(p:list) -> None:
    pass

def interpolate_data_points() -> None:
    pass

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

        result = polynomial_multiplication([-12, 1, 3], [4, 0, 1])
        polynomial_printing(result)


# Para evitar confusão com escopo de variáveis
if __name__ == "__main__":
    main()