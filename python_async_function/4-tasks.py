#!/usr/bin/env python3
""" Take the code from wait_n and alter it into a new function task_wait_n.
    The code is nearly identical to wait_n except task_wait_random is being
    called. """
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ Tasks """
    delays: List[float] = []
    all_delays: List[float] = []
    for i in range(n):
        delays.append(task_wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        all_delays.append(earliest_result)
    return all_delays

# ```python
# import asyncio
# from typing import List
# task_wait_random = __import__('3-tasks').task_wait_random
# ```
# Se importa el módulo `asyncio` y el tipo de dato `List` del módulo `typing`. Luego, se importa la función `task_wait_random` de otro archivo usando el método `__import__()`.

# ```python
# async def task_wait_n(n: int, max_delay: int) -> List[float]:
#     """ Tasks """
#     delays: List[float] = []
#     all_delays: List[float] = []
#     for i in range(n):
#         delays.append(task_wait_random(max_delay))
#     for delay in asyncio.as_completed(delays):
#         earliest_result = await delay
#         all_delays.append(earliest_result)
#     return all_delays
# ```
# Se define una función asíncrona llamada `task_wait_n` que acepta dos argumentos enteros: `n` y `max_delay`. La función devuelve una lista de valores de punto flotante.

# Dentro de la función, se crea una lista llamada `delays` para almacenar las tareas asincrónicas. Luego, se utiliza un bucle para crear `n` tareas asincrónicas llamando a la función `task_wait_random(max_delay)` y agregando cada tarea a la lista `delays`.

# Luego, se utiliza `asyncio.as_completed()` para esperar hasta que cada tarea se complete. Cuando una tarea se completa, su resultado se agrega a la lista `all_delays`.

# Finalmente, la función devuelve la lista `all_delays` que contiene los resultados de las tareas en el orden en que se completaron.

# En resumen, este código toma el concepto de la función `wait_n` y lo adapta a tareas asincrónicas utilizando la función `task_wait_random`. Las tareas se ejecutan en paralelo y se obtienen sus resultados en el orden de finalización.