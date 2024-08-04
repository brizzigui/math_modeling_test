# Solução da questão 2

import io 
# Parte da stdlib, importei apenas para colocar as dicas de tipo (type hints) do arquivo texto

import matplotlib.pyplot as plt

import time
import datetime
# Lidam com a conversão das datas em horas de maneira precisa e genérica

import numpy as np

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
            print(f"{value}", end=" ")

        elif index == 1:
            print(f"{value}x", end=" ") if value != 1 else print(f"x", end=" ")

        else:
            print(f"{value}x^{index}", end=" ") if value != 1 else print(f"x^{index}", end=" ")

def get_applied_polynomial(p: list, value: float) -> float:
    acc = 0
    for i in range(len(p)):
        acc = acc + (p[i]*value**i)

    return acc

def apply_list(p: list, values: list) -> list:
    applied = []
    for value in values:
        applied.append(get_applied_polynomial(p, value))

    return applied

def divide_polynomial_by_value(polynomial: list, value: float) -> list:
    return [polynomial[i]/value for i in range(len(polynomial))]

def convert_timestamps(stamps: list) -> list:
    # Retorna o tempo em horas decorrido desde o início do experimento.

    converted = [0]
    first = True

    for stamp in stamps:
        date, moment = stamp.split()
        year, month, day = map(int, date.split("-"))
        hours, minutes, seconds = map(int, moment.split(":"))

        unix_stamp = datetime.datetime(year, month, day, hours, minutes, seconds).timestamp()

        if first:
            start = unix_stamp
            first = False
            continue

        hours_elapsed = (unix_stamp - start) / (60 * 60)
        converted.append(hours_elapsed)
        
    return converted

def plot_interpolated_function(polynomial:list, discrete_x:list, discrete_y:list) -> None:
    plt.scatter(discrete_x, discrete_y)

    x_vals = np.linspace(min(discrete_x), max(discrete_x), 1000)
    y_vals = apply_list(polynomial, x_vals)

    plt.plot(x_vals, y_vals)
    plt.show()


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
        
        print("\n-------------------")
        print("Solução do item (a)")

        print(f"Valor mínimo: {minimum}")
        print(f"Valor máximo: {maximum}")
        print(f"Valor médio: {average}")

        print("\n-------------------")
        print("Solução do item (b)")
        print("FECHE A JANELA PARA CONTINUAR AO ITEM C")
        plot_wvht(dates, wvht)

        print("\n-------------------")
        print("Solução do item (c)")

        times_elapsed = convert_timestamps(dates)
        result = interpolate_data_points(times_elapsed, wvht)

        print("A interpolação polinomial mais próxima é: \n")
        polynomial_printing(result)
        print("\n\n(usando a interpolação de Lagrange)")

        print("\nPlotando gráfico. FECHE A JANELA PARA ENCERRAR PROGRAMA.")

        plot_interpolated_function(result, times_elapsed, wvht)


# Para evitar confusão com escopo de variáveis
if __name__ == "__main__":
    main()