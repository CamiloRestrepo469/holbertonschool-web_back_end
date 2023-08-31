#!/usr/bin/env python3
""" Import wait_random from 0-basic_async_syntax.
    Write a function (do not create an async function, use the regular function
    syntax to do this) task_wait_random that takes an integer max_delay and
    returns a asyncio.Task. """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ Tasks """
    task = asyncio.create_task(wait_random(max_delay))
    return task

# ```python
# import asyncio
# wait_random = __import__('0-basic_async_syntax').wait_random
# ```
# Se importa el módulo `asyncio`, y luego se importa la función `wait_random` de otro archivo usando el método `__import__()`.

# ```python
# def task_wait_random(max_delay: int) -> asyncio.Task:
#     """ Tasks """
#     task = asyncio.create_task(wait_random(max_delay))
#     return task
# ```
# Se define una función llamada `task_wait_random` que acepta un argumento entero llamado `max_delay`. Dentro de esta función, se crea una tarea asincrónica usando `asyncio.create_task()`. La tarea se crea ejecutando la función `wait_random(max_delay)`, que esperará un tiempo aleatorio asincrónicamente y luego devolverá ese tiempo. La función `task_wait_random` devuelve la tarea creada.

# Esta función `task_wait_random` se encarga de crear una tarea asincrónica basada en la función `wait_random`, que a su vez puede ser ejecutada en paralelo junto con otras tareas usando el módulo `asyncio`.
