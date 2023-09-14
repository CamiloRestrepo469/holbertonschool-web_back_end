
### Cómo definir una Clase

Una clase en programación es como un plano o una plantilla que define la estructura y el comportamiento de un objeto. Para definir una clase en JavaScript, puedes utilizar la palabra clave `class`, seguida del nombre de la clase y un bloque de código que contiene las propiedades y métodos de la clase. Aquí tienes un ejemplo:

```javascript
class Persona {
  constructor(nombre, edad) {
    this.nombre = nombre;
    this.edad = edad;
  }
  
  saludar() {
    console.log(`Hola, mi nombre es ${this.nombre} y tengo ${this.edad} años.`);
  }
}
```

En este ejemplo, hemos definido una clase llamada `Persona` con un constructor que inicializa las propiedades `nombre` y `edad`, y un método `saludar` que muestra un mensaje.

### Cómo agregar métodos a una clase

Puedes agregar métodos a una clase simplemente definiéndolos dentro del bloque de la clase. Los métodos son funciones que pueden realizar acciones específicas basadas en las propiedades de la clase. En el ejemplo anterior, `saludar` es un método de la clase `Persona`.

### Por qué y cómo agregar un método estático a una clase

Un método estático es un método que se llama en la clase misma, en lugar de en una instancia de la clase. Son útiles cuando deseas realizar una acción que no depende de las propiedades de una instancia en particular. Para agregar un método estático a una clase en JavaScript, puedes usar la palabra clave `static`. Aquí tienes un ejemplo:

```javascript
class Utilidades {
  static sumar(a, b) {
    return a + b;
  }
}
```

En este caso, hemos definido un método estático llamado `sumar` en la clase `Utilidades` que puede sumar dos números sin necesidad de crear una instancia de la clase.

### Cómo extender una clase desde otra

La herencia es un concepto importante en la programación orientada a objetos. Puedes extender una clase desde otra utilizando la palabra clave `extends`. Esto te permite crear una nueva clase que hereda todas las propiedades y métodos de la clase padre. Aquí tienes un ejemplo:

```javascript
class Estudiante extends Persona {
  constructor(nombre, edad, curso) {
    super(nombre, edad);
    this.curso = curso;
  }
}
```

En este ejemplo, la clase `Estudiante` extiende la clase `Persona`, por lo que hereda el constructor y el método `saludar`, y además, tiene su propia propiedad `curso`.

### Metaprogramación y símbolos

La metaprogramación se refiere a la capacidad de un programa para examinar o modificar su propia estructura o comportamiento en tiempo de ejecución. Los símbolos en JavaScript son una característica que permite crear identificadores únicos y ocultos que se pueden utilizar en metaprogramación para evitar colisiones de nombres de propiedades. Los símbolos se crean utilizando la función `Symbol()`. Pueden ser útiles para agregar propiedades privadas a un objeto o clase, entre otras aplicaciones avanzadas.
