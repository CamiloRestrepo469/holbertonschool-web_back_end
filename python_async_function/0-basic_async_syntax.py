#!/usr/bin/env python3
""" The basics of async  """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """ asynchronous coroutine that takes in an integer argument
        (max_delay, with a default value of 10) named wait_random that waits
        for a random delay between 0 and max_delay (included and float value)
        seconds and eventually returns it.  """
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float

# ```python
# """ The basics of async  """
# ```
# Esta línea es un comentario de triple comilla que sirve como docstring para el módulo. Proporciona una descripción general del propósito del módulo.

# ```python
# import random
# import asyncio
# ```
# Estas líneas importan los módulos `random` y `asyncio`. `random` se utiliza para generar números aleatorios, y `asyncio` es una librería para programación asíncrona en Python.

# ```python
# async def wait_random(max_delay: int = 10) -> float:
# ```
# Aquí se define una función asíncrona llamada `wait_random` que acepta un argumento entero llamado `max_delay` con un valor predeterminado de 10. La función devuelve un valor de tipo `float`.

# ```python
#     """ asynchronous coroutine that takes in an integer argument
#         (max_delay, with a default value of 10) named wait_random that waits
#         for a random delay between 0 and max_delay (included and float value)
#         seconds and eventually returns it.  """
# ```
# Este es el docstring de la función `wait_random`, que proporciona una descripción de lo que hace la función. Indica que es una "corutina asincrónica" que espera un tiempo de retraso aleatorio entre 0 y `max_delay` segundos, y finalmente devuelve ese valor.

# ```python
#     random_float = random.uniform(0, max_delay)
# ```
# Se genera un número de punto flotante aleatorio utilizando la función `random.uniform()`. Este número estará entre 0 y `max_delay` (incluido).

# ```python
#     await asyncio.sleep(random_float)
# ```
# Aquí se utiliza la función `asyncio.sleep()` para pausar la ejecución de la corutina durante `random_float` segundos. La palabra clave `await` se utiliza para indicar que se está esperando asincrónicamente la finalización de esta operación de pausa.

# ```python
#     return random_float
# ```
# Finalmente, la función devuelve el valor de `random_float` como resultado de la corutina.

# Este fragmento de código se refiere a conceptos de programación asincrónica y corutinas en Python, donde se utilizan las capacidades de `asyncio` para gestionar tareas que pueden ejecutarse de manera asíncrona. La función `wait_random` simula una espera de tiempo variable y asincrónica antes de devolver un valor aleatorio.

