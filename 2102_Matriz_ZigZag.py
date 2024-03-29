# https://jv.umsa.bo/oj/problem.php?id=2102
#  Matriz ZigZag
#  Enviar
#  Estado
#  Descripción
#    La matriz Zig Zag es una matriz cuadrada ($N * N$) que suele ser algo dificil de implementar. Es una matriz que va llenando sus casillas con los números entre $1$ y $N * N$ siguiendo la forma Zig Zag, de la siguiente forma(Lineas rojas):
#    La matriz Zig Zag es una matriz cuadrada ($N * N$) que suele ser algo dificil de implementar. Es una matriz que va llenando sus casillas con los números entre $1$ y $N * N$ siguiendo la forma Zig Zag, de la siguiente forma(Lineas rojas):
#    La matriz Zig Zag es una matriz cuadrada ($N * N$) que suele ser algo dificil de implementar. Es una matriz que va llenando sus casillas con los números entre $1$ y $N * N$ siguiendo la forma Zig Zag, de la siguiente forma(Lineas rojas):
#    Lineas rojas
#    Ahora debemos generar una matriz Zig Zag, con los números de $1$ a $N * N$, la matriz para $N = 5$ quedaría así:
#    Ahora debemos generar una matriz Zig Zag, con los números de $1$ a $N * N$, la matriz para $N = 5$ quedaría así:
#    Ahora debemos generar una matriz Zig Zag, con los números de $1$ a $N * N$, la matriz para $N = 5$ quedaría así:
#   Entrada
#    La entrada consiste en un único número entero $N$ ($1 \leq N \leq 100$).
#    La entrada consiste en un único número entero $N$ ($1 \leq N \leq 100$).
#    La entrada consiste en un único número entero $N$ ($1 \leq N \leq 100$).
#   Salida
#    Imprimir la matriz Zig Zag de tamaño $N * N$, con los números de $1$ a $N * N$
#    Imprimir la matriz Zig Zag de tamaño $N * N$, con los números de $1$ a $N * N$
#    Imprimir la matriz Zig Zag de tamaño $N * N$, con los números de $1$ a $N * N$
#   Ejemplo Entrada
#    5
#   Ejemplo Salida
#    1 3 4 10 112 5 9 12 196 8 13 18 207 14 17 21 2415 16 22 23 25
#   Ayuda

# Se lee el tamaño de la matriz cuadrada
n = int(input())

# Se inicializa una matriz de n x n con valores 0
matriz = [[0] * n for _ in range(n)]

# Se inicia en la esquina superior izquierda de la matriz
fila, columna = 0, 0

# Se comienza a llenar la matriz con los números del 1 al n^2
# La variable direccion indica si se está avanzando hacia arriba o hacia abajo
direccion = "abajo"

for i in range(1, n * n + 1):
    # Se coloca el número en la posición actual de la matriz
    matriz[fila][columna] = i
    
    # Dependiendo de la dirección actual, se mueve hacia la siguiente posición
    if direccion == "arriba":
        # Si se está avanzando hacia arriba, se verifica si se ha llegado al borde superior o derecho de la matriz
        if fila == 0 or columna == n - 1:
            # Si se ha llegado al borde superior o derecho, se cambia la dirección hacia abajo
            direccion = "abajo"
            # Se verifica si se ha llegado al borde derecho de la matriz
            if columna == n - 1:
                # Si se ha llegado al borde derecho, se mueve una posición hacia abajo
                fila += 1
            else:
                # Si no se ha llegado al borde derecho, se mueve una posición hacia la derecha
                columna += 1
        else:
            # Si no se ha llegado a ningún borde, se mueve una posición hacia arriba y hacia la derecha
            fila -= 1
            columna += 1
    else:
        # Si se está avanzando hacia abajo, se verifica si se ha llegado al borde inferior o izquierdo de la matriz
        if columna == 0 or fila == n - 1:
            # Si se ha llegado al borde inferior o izquierdo, se cambia la dirección hacia arriba
            direccion = "arriba"
            # Se verifica si se ha llegado al borde inferior de la matriz
            if fila == n - 1:
                # Si se ha llegado al borde inferior, se mueve una posición hacia la derecha
                columna += 1
            else:
                # Si no se ha llegado al borde inferior, se mueve una posición hacia abajo
                fila += 1
        else:
            # Si no se ha llegado a ningún borde, se mueve una posición hacia abajo y hacia la izquierda
            fila += 1
            columna -= 1

# Se imprime la matriz en forma de tabla
for fila in matriz:
    print(" ".join(str(x) for x in fila))