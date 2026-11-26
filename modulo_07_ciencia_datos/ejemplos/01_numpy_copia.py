"""Módulo 7 - Ejemplo 1: NumPy.

Ejecuta el fichero entero o, mejor, selecciona trozos y envíalos al
intérprete con Mayús + Intro.
"""

import time

import numpy as np

# --- Crear arrays -----------------------------------------------------------
precios = np.array([950.0, 19.9, 189.0, 45.0])
unidades = np.array([2, 10, 3, 5])
print("precios:", precios, precios.dtype, precios.shape)
print("arange:", np.arange(0, 10, 2))
print("linspace:", np.linspace(0, 1, 5))

# --- Operaciones elemento a elemento ----------------------------------------
importes = unidades * precios
print("importes:", importes)
print("con IVA:", np.round(importes * 1.21, 2))
print("¿mayor de 500?", importes > 500)

# --- Agregaciones -----------------------------------------------------------
print("total:", importes.sum(), "media:", importes.mean(), "máximo:", importes.max())
print("posición del máximo:", importes.argmax())

# --- Matrices y ejes --------------------------------------------------------
# Filas: vendedores. Columnas: trimestres.
ventas = np.array([
    [12, 15, 9, 20],
    [8, 11, 14, 10],
    [5, 7, 6, 9],
])
print("por vendedor (axis=1):", ventas.sum(axis=1))
print("por trimestre (axis=0):", ventas.sum(axis=0))
print("segundo trimestre:", ventas[:, 1])

# --- Máscaras ---------------------------------------------------------------
print("importes grandes:", importes[importes > 500])
print("entre 100 y 1000:", importes[(importes > 100) & (importes < 1000)])
print("etiquetas:", np.where(importes > 500, "grande", "normal"))

# --- Vistas: un corte no copia ----------------------------------------------
original = np.array([1, 2, 3, 4])
trozo = original[:2]
trozo[0] = 99
print("el original ha cambiado:", original)

# --- Por qué se vectoriza ---------------------------------------------------
N = 2_000_000
lista = list(range(N))
array = np.arange(N)

inicio = time.perf_counter()
total_lista = sum(x * 2 for x in lista)
tiempo_lista = time.perf_counter() - inicio

inicio = time.perf_counter()
total_array = (array * 2).sum()
tiempo_array = time.perf_counter() - inicio

print(f"bucle de Python: {tiempo_lista:.3f} s   NumPy: {tiempo_array:.3f} s   "
      f"NumPy es {tiempo_lista / tiempo_array:.0f} veces más rápido")
