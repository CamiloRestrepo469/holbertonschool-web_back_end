#!/usr/bin/env python3

import asyncio
import random

# Definimos una función asincrónica llamada wait_random.
# max_delay es el argumento que determina el tiempo máximo de espera (por defecto 10).
async def wait_random(max_delay=10):
    # Generamos un retraso aleatorio entre 0 y max_delay (valor decimal).
    delay = random.uniform(0, max_delay)
    
    # Pausamos la ejecución de la función asincrónica durante "delay" segundos.
    await asyncio.sleep(delay)
    
    # Devolvemos el valor del retraso generado.
    return delay

# Bloque principal
if __name__ == "__main__":
    # Ejecutamos la función wait_random sin argumentos y mostramos el resultado.
    print(asyncio.run(wait_random()))
    
    # Ejecutamos la función wait_random con max_delay = 5 y mostramos el resultado.
    print(asyncio.run(wait_random(5)))
    
    # Ejecutamos la función wait_random con max_delay = 15 y mostramos el resultado.
    print(asyncio.run(wait_random(15)))
