#!/usr/bin/env python3
""" From the previous file, import wait_n into 2-measure_runtime.py.
    Create a measure_time function with integers n and max_delay as arguments
    that measures the total execution time for wait_n(n, max_delay), and
    returns total_time / n. Your function should return a float.
    Use the time module to measure an approximate elapsed time. """
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Measure the runtime """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n

# ```python
# import asyncio
# import time
# wait_n = __import__('1-concurrent_coroutines').wait_n
# ```
# Se importan los módulos `asyncio` y `time`. Luego, se importa la función `wait_n` de otro archivo usando el método `__import__()`.

# ```python
# def measure_time(n: int, max_delay: int) -> float:
#     """ Measure the runtime """
#     start_time = time.time()
#     asyncio.run(wait_n(n, max_delay))
#     end_time = time.time()
#     total_time = end_time - start_time
#     return total_time / n
# ```
# Se define una función llamada `measure_time` que acepta dos argumentos enteros: `n` y `max_delay`. La función mide el tiempo total de ejecución al guardar el tiempo de inicio y el tiempo de finalización en segundos usando el módulo `time`. Luego, ejecuta la función `wait_n(n, max_delay)` utilizando `asyncio.run()`. Después de que `wait_n` se complete, se registra el tiempo de finalización y se calcula el tiempo total de ejecución. Finalmente, se devuelve el tiempo total dividido por `n` como un valor de tipo float.

# Esta función `measure_time` se utiliza para medir el tiempo promedio de ejecución de la función `wait_n` con un número dado de repeticiones (`n`) y un retraso máximo (`max_delay`).
