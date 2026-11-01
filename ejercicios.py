from lista_python import ListaPasajerosPython
from pasajero import Pasajero


def ejercicio_t1():
    print("T1 - CRUD de pasajeros con clase Pasajero + list")
    lista = ListaPasajerosPython()
    lista.añadir(Pasajero("Diana", "0923456789", 22))
    lista.añadir(Pasajero("Ana", "0912345678", 28))
    lista.añadir(Pasajero("Luis", "0987654321", 35))
    lista.listar()
    pos = lista.buscar("0912345678")
    print(f"Buscar Ana: posicion {pos}")
    lista.modificar("0912345678", "Anita", 29)
    lista.eliminar_por_valor("0987654321")
    lista.pasajeros.sort(key=lambda p: p.nombre)
    print("Lista final ordenada por nombre:")
    lista.listar()


def ejercicio_t2():
    print("T2 - Estadisticas de una lista de notas")
    nombres = ["Ana", "Luis", "Diana", "Beto", "Elena"]
    notas = [8, 6, 10, 7, 5]

    suma = 0
    max_nota = notas[0]
    min_nota = notas[0]
    idx_max = 0
    aprobados_m = 0
    for i in range(len(notas)):
        suma += notas[i]
        if notas[i] > max_nota:
            max_nota = notas[i]
            idx_max = i
        if notas[i] < min_nota:
            min_nota = notas[i]
        if notas[i] >= 7:
            aprobados_m += 1
    prom_m = suma / len(notas)
    print(f"[Manual] Promedio {prom_m:.2f} | Max {max_nota} ({nombres[idx_max]}) | Min {min_nota} | Aprobados {aprobados_m} de {len(notas)}")

    prom_p = sum(notas) / len(notas)
    max_p = max(notas)
    min_p = min(notas)
    nom_max = nombres[notas.index(max_p)]
    aprobados_p = len([n for n in notas if n >= 7])
    print(f"[Python] Promedio {prom_p:.2f} | Max {max_p} ({nom_max}) | Min {min_p} | Aprobados {aprobados_p} de {len(notas)}")


def ejercicio_t3():
    print("T3 - Ordenar una lista (bubble sort)")
    datos = [5, 2, 8, 1, 9, 3, 7]
    copia = datos[:]
    n = len(copia)
    for i in range(n - 1):
        hubo_swap = False
        for j in range(n - 1 - i):
            if copia[j] > copia[j + 1]:
                copia[j], copia[j + 1] = copia[j + 1], copia[j]
                hubo_swap = True
        if not hubo_swap:
            break
    print(f"[Manual] {copia}")
    print(f"[Python] {sorted(datos)}")


def ejercicio_p1():
    print("P1 - Contar apariciones de un valor")
    lista = [1, 3, 2, 3, 4, 3, 5]
    v = 3
    c = 0
    for x in lista:
        if x == v:
            c += 1
    print(f"[Manual] {v} aparece {c} veces")
    print(f"[Python] {v} aparece {lista.count(v)} veces")


def ejercicio_p2():
    print("P2 - Invertir una lista")
    lista = [1, 2, 3, 4, 5]
    inv_m = []
    for i in range(len(lista) - 1, -1, -1):
        inv_m.append(lista[i])
    print(f"[Manual] {inv_m}")
    print(f"[Python] {lista[::-1]}")


def ejercicio_p3():
    print("P3 - Numeros unicos")
    nums = [1, 3, 2, 3, 4, 1, 5, 2]
    unicos = []
    for x in nums:
        if x not in unicos:
            unicos.append(x)
    print(f"[Manual] {unicos}")
    print(f"[Python] {list(dict.fromkeys(nums))}")


def ejercicio_p4():
    print("P4 - Segundo mayor")
    nums = [5, 2, 9, 7, 9, 3, 8]
    mayor = float("-inf")
    segundo = float("-inf")
    for x in nums:
        if x > mayor:
            segundo = mayor
            mayor = x
        elif x > segundo and x < mayor:
            segundo = x
    print(f"[Manual] Mayor {mayor} | Segundo {segundo}")
    segundo_py = sorted(set(nums))[-2]
    print(f"[Python] Mayor {max(nums)} | Segundo {segundo_py}")


def ejercicio_p5():
    print("P5 - Fusionar dos listas ordenadas")
    a = [1, 3, 5, 7]
    b = [2, 4, 6, 8, 10]
    res = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
        else:
            res.append(b[j])
            j += 1
    while i < len(a):
        res.append(a[i])
        i += 1
    while j < len(b):
        res.append(b[j])
        j += 1
    print(f"[Manual] {res}")
    print(f"[Python] {sorted(a + b)}")


EJERCICIOS = [
    ("T1", "CRUD de pasajeros con clase Pasajero + list", "taller", ejercicio_t1),
    ("T2", "Estadisticas de una lista de notas", "taller", ejercicio_t2),
    ("T3", "Ordenar una lista (bubble sort)", "taller", ejercicio_t3),
    ("P1", "Contar apariciones de un valor", "propuesto", ejercicio_p1),
    ("P2", "Invertir una lista", "propuesto", ejercicio_p2),
    ("P3", "Numeros unicos", "propuesto", ejercicio_p3),
    ("P4", "Segundo mayor", "propuesto", ejercicio_p4),
    ("P5", "Fusionar dos listas ordenadas", "propuesto", ejercicio_p5),
]


def menu_ejercicios():
    while True:
        taller = [e for e in EJERCICIOS if e[2] == "taller"]
        propuestos = [e for e in EJERCICIOS if e[2] == "propuesto"]
        print("\n--- DESARROLLADOS (taller) ---")
        for e in taller:
            print(f"  {e[0]}. {e[1]}")
        print("--- PROPUESTOS ---")
        for e in propuestos:
            print(f"  {e[0]}. {e[1]}")
        print("  0. Volver")

        codigo = input("Codigo: ").strip().upper()
        if codigo == "0":
            break
        encontrados = [e for e in EJERCICIOS if e[0] == codigo]
        if encontrados:
            print()
            encontrados[0][3]()
        else:
            print("Codigo no valido")