#!/usr/bin/env python3
""" Import wait_random from the previous python file that you’ve written and
    write an async routine called wait_n that takes in 2 int arguments:
    max_delay and n. You will spawn wait_random n times with the specified
    max_delay. wait_n should return the list of all the delays (float values).
    The list of the delays should be in ascending order without using sort()
    because of concurrency. """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ Let's execute multiple coroutines at the same time with async  """
    delays: List[float] = []
    all_delays: List[float] = []
    for i in range(n):
        delays.append(wait_random(max_delay))
    for delay in asyncio.as_completed(delays):
        earliest_result = await delay
        all_delays.append(earliest_result)
    return all_delays


# Esta es la docstring del módulo. Proporciona una descripción de alto nivel de lo que hace el código. En este caso, explica que el objetivo es importar la función `wait_random` de otro archivo y escribir una rutina asíncrona llamada `wait_n` que toma dos argumentos enteros: `max_delay` y `n`. La función crea varias corutinas `wait_random` con un retraso máximo dado y devuelve una lista de los retrasos en orden ascendente sin usar `sort()` debido a la concurrencia.

# ```python
# import asyncio
# from typing import List
# wait_random = __import__('0-basic_async_syntax').wait_random
# ```
# Se importa el módulo `asyncio` y se importa el tipo de dato `List` del módulo `typing`. Luego se importa la función `wait_random` de otro archivo usando el método `__import__()`.

# ```python
# async def wait_n(n: int, max_delay: int) -> List[float]:
# ```
# Se define una función asíncrona llamada `wait_n` que acepta dos argumentos enteros: `n` y `max_delay`. La función devuelve una lista de valores de punto flotante.

# ```python
#     """ Let's execute multiple coroutines at the same time with async  """
# ```
# Esta es la docstring de la función `wait_n`, que proporciona una breve descripción de lo que hace la función.

# ```python
#     delays: List[float] = []
#     all_delays: List[float] = []
# ```
# Se declaran dos listas vacías para almacenar los retrasos.

# ```python
#     for i in range(n):
#         delays.append(wait_random(max_delay))
# ```
# Se utiliza un bucle para crear `n` corutinas `wait_random` con un retraso máximo de `max_delay` y se agrega cada corutina a la lista `delays`.

# ```python
#     for delay in asyncio.as_completed(delays):
#         earliest_result = await delay
#         all_delays.append(earliest_result)
# ```
# Aquí, se utiliza `asyncio.as_completed()` para esperar hasta que cada una de las corutinas en `delays` se complete. Cuando una corutina se completa, su resultado se agrega a la lista `all_delays`.

# ```python
#     return all_delays
# ```
# Finalmente, se devuelve la lista `all_delays` que contiene los retrasos en orden ascendente.

# Este código utiliza el módulo `asyncio` para crear y manejar múltiples corutinas asincrónicas en paralelo y recopilar sus resultados en un orden específico. La función `wait_n` toma un número `n` y un retraso máximo `max_delay`, crea `n` corutinas `wait_random`, las ejecuta en paralelo y devuelve una lista ordenada de los resultados.