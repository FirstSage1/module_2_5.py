# module_2_5 Функция с параметром.
# ==========================================
def get_matrix(n, m, value):   # Cоздаем функцию матрицы
    matrix = []                # пустой список
    for i in range(n):         # цикл аргумента строк
        a=[]
        matrix.append(a)
        for j in range(m):      # цикл аргумента столбцов
            a.append(value)
    return matrix

result_1 = get_matrix(2,2,10)
result_2 = get_matrix(3,5,42)
result_3 = get_matrix(4,2 ,13)

print(result_1)
print(result_2)
print(result_3)
