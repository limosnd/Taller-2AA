import time

# Algoritmo 1: Conversión Binaria Recursiva (CB)
def CB(X, b, e):
    if e < b:
        return []
    else:
        q = (b + e) // 2
        d = (X // (2 ** q)) % 2
        l = CB(X, b, q - 1)
        h = CB(X, q + 1, e)
        return h + [d] + l

# Ejemplo de uso para CB:
n = 13
b = 0
e = len(bin(n)) - 3  # Calcula la cantidad de bits necesarios menos el "0b"
print(CB(n, b, e))  # Salida esperada: [1, 1, 0, 1]

# Algoritmo 2: Conversión Iterativa a Binario (CBI)
def CBI(n):
    res = []
    while n > 0:
        r = n % 2
        res = [r] + res
        n = n // 2

    if res == []:
        return [0]

    return res

# Ejemplo de uso para CBI:
print(CBI(n))  # Salida: [1, 1, 0, 1]

# Función para medir el tiempo de ejecución de un algoritmo
def medir_tiempo(func, *args):
    inicio = time.time()
    func(*args)
    fin = time.time()
    return fin - inicio

# Comparación de tiempos de ejecución
max_n = 30000
tiempos_CB = []
tiempos_CBI = []

for n in range(1, max_n + 1):
    # Calculamos 'e' como la cantidad de bits necesarios menos el "0b"
    b = 0
    e = len(bin(n)) - 3

    # Medimos el tiempo de ejecución de CB
    tiempo_CB = medir_tiempo(CB, n, b, e)
    tiempos_CB.append(tiempo_CB)

    # Medimos el tiempo de ejecución de CBI
    tiempo_CBI = medir_tiempo(CBI, n)
    tiempos_CBI.append(tiempo_CBI)

# Imprimimos los resultados
print(f"Tiempo promedio para CB: {sum(tiempos_CB)/len(tiempos_CB):.10f} segundos")
print(f"Tiempo promedio para CBI: {sum(tiempos_CBI)/len(tiempos_CBI):.10f} segundos")

print(f"Tiempo total para CB: {sum(tiempos_CB):.10f} segundos")
print(f"Tiempo total para CBI: {sum(tiempos_CBI):.10f} segundos")
