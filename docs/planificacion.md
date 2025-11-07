# Planificación del Juego del Ahorcado

## Análisis del Problema

### Entrada

- Palabra a adivinar (generada automáticamente, min. 5 letras, desde API o lista local)
- Letras propuestas por el jugador (vía input)
- Dificultad seleccionada (elige número de intentos)


### Salida

- Estado parcial de la palabra (_ y letras acertadas)
- Intentos restantes
- Letras ya usadas
- Mensajes informativos y de error
- Mensaje de victoria o derrota


### Proceso

1. Obtener/la palabra secreta (API o lista local, mín. 5 letras)
2. Solicitar nivel de dificultad (asigna intentos según opción)
3. Inicializar estado del juego (guiones, letras usadas, variables)
4. Mientras queden intentos y la palabra no esté adivinada:
    - Mostrar estado actual del juego
    - Solicitar nueva letra (y validar)
    - Actualizar letras usadas e intentos según acierto o error
    - Permitir intento de adivinanza completa de palabra (o saltar turno)
    - Comprobar si se ha completado la palabra
5. Mostrar mensaje final (victoria o derrota)

## Pseudocódigo

```
INICIO
    OBTENER palabra_aleatoria (API o lista local, min. 5 letras)
    ELECCIÓN de dificultad → intentos
    INICIALIZAR: letras_usadas = [], guiones = "_" * longitud, adivinado = FALSO

    MIENTRAS intentos > 0 Y NO adivinado HACER
        MOSTRAR estado (guiones, intentos, letras_usadas)
        SOLICITAR letra válida y no repetida
        ACTUALIZAR estado de palabra y letras_usadas
        SI letra NO está en palabra ENTONCES
            RESTAR un intento
        SI "_" NO_ESTÁ_EN guiones ENTONCES
            adivinado = VERDADERO
        SINO
            PERMITIR intentar adivinar la palabra (o saltar turno)
            SI palabra completa acertada ENTONCES
                adivinado = VERDADERO

    SI adivinado ENTONCES
        ESCRIBIR "¡Felicidades! ..."
    SINO
        ESCRIBIR "Has perdido. La palabra era:", palabra
FIN
```


## Variables Necesarias

| Variable | Tipo | Propósito |
| :-- | :-- | :-- |
| palabra | str | Palabra a adivinar en mayúsculas |
| guiones | list | Estado parcial de la palabra (_ o letra acertada) |
| letra | str | Letra introducida por jugador |
| letras_usadas | list | Lista de letras usadas |
| intentos | int | Intentos restantes |
| adivinado | bool | Indica si la palabra ha sido completada |
| dificultad | int | Nivel de dificultad elegido (define intentos) |

## Estructuras de Control Necesarias

### Bucles While

1. **Bucle principal**: mientras haya intentos y no se haya adivinado la palabra
2. **Validación de letra**: repetir hasta obtener letra válida

### Condicionales If

1. Comprobar acierto/error de letra
2. Comprobar si hay espacios sin rellenar ("_")
3. Validar si letra ya usada
4. Comprobar si usuario adivina palabra completa
5. Mostrar mensaje adecuado tras victoria o derrota

### Bucles For

- Para actualizar guiones al acertar letra(s) en palabra


## Funciones Útiles de Python

### String

- `upper()`, `isalpha()`, `len()`, `in`


### List

- `append()`, `in`, asignación de elementos


### Built-in

- `input()`, `print()`, `enumerate()`, `random.choice()`


## Consejos para la Implementación

1. Mantén funciones breves y con propósito único (obtener_palabra, comprobar_letra, etc.)
2. Usa try/except para peticiones a API y posibles errores de entrada
3. Proporciona mensajes de error y ayuda clara al usuario
4. Prueba cada función por separado y después el flujo completo
5. Documenta cada función y cada bloque principal del programa