// En el archivo 0-constants.js

// Función para instanciar variables usando 'const'
export function taskFirst() {
    const task = 'I prefer const when I can.';
    return task;
  }
  
  // Función para obtener una parte de la cadena
  export function getLast() {
    return ' is okay';
  }
  
  // Función para instanciar variables usando 'let'
  export function taskNext() {
    let combination = 'But sometimes let';
    combination += getLast();
  
    return combination;
  }
  