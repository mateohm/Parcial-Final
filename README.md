# Parcial Final

## Primer Punto

En este punto se diseñó una función encargada de producir, como salida, una gramática de atributos capaz de soportar las operaciones básicas de un lenguaje tipo SQL.
La idea central del modelado fue:

- Definir la estructura sintáctica de sentencias SELECT, INSERT, UPDATE y DELETE.

- Incorporar atributos heredados y sintetizados para controlar la semántica del lenguaje.

- Incluir reglas semánticas para:

     - Validación de existencia de tablas.

     - Comprobación de columnas.

     - Verificación de tipos en expresiones.

     - Reglas para la cláusula WHERE.

     - Correspondencia entre columnas y valores en INSERT.

El resultado es una gramática completa que no solo representa la sintaxis de un lenguaje SQL simple, sino que también integra restricciones semánticas reales que permiten detectar errores durante la evaluación de las consultas.

## Segundo Punto

Aquí se desarrolló una gramática formal (BNF) complementada con atributos para representar un lenguaje que permita declarar matrices y realizar la operación dot(A,B).

Las decisiones principales para este punto fueron:

- Interpretar “matrices de diferentes dimensiones” como matrices con distinta forma, pero con el mismo número total de elementos, permitiendo así la operación de producto punto a través de una representación aplanada.

- Diseñar una gramática que reconozca:

    - Literales de matrices.

    - Listas de filas y columnas.

    - Números enteros y flotantes.

    - La operación dot(expr, expr).

- Definir atributos como:

    - rows, cols, size

    - elems (lista de elementos en orden fila-mayor)

    - value para el resultado del dot

- Incorporar reglas semánticas que validan:

    - La consistencia del número de columnas por fila.

    - La compatibilidad de tamaños entre matrices para la operación dot.

    - El cálculo correcto del producto punto.

El resultado es una gramática formal robusta con un conjunto claro de reglas semánticas que garantizan el comportamiento deseado del lenguaje.

## Tercer Punto 

Se trasladó la gramática del punto 2 a un archivo ANTLR (MatrixDot.g4) para su implementación práctica en Python.

El desarrollo incluyó:

- Lexer + Parser en ANTLR

    - Definición de tokens básicos: números, corchetes, comas, punto y coma, palabra clave dot.

    - Construcción de reglas sintácticas equivalentes a la gramática diseñada en el punto 2.

- Implementación de un Visitor en Python

Se implementó un visitor encargado de:

- Crear objetos Matrix con sus atributos (filas, columnas, elementos).

- Verificar errores semánticos, como matrices irregulares o de tamaño incompatible.

- Ejecutar la operación dot sumando el producto elemento por elemento.

- Retornar el resultado numérico final.

La combinación de ANTLR + Visitor permite ejecutar expresiones como:

```
dot([[1,2,3],[4,5,6]], [[7,8],[9,10],[11,12]]);
```

Retornando el resultado correcto del producto punto.


